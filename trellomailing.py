import json

default_latex_header = "default_latex_header.txt" #I'll eventually write code to make this up with any label, but for now this will do. 

def read_json_file(filename):
    '''Reads the json file and returns it without further ado'''
    
    try:
        with open(filename, "r") as read_file:
            data = json.load(read_file)
    except IOError:
        print("File not found. Check for typos?")
        raise FileNotFoundError
    except ValueError:
        print("Are you sure that's a JSON export?")
        raise ValueError
        return False
    
    return data


def get_card_list(filename=None,data=None,sort=False):
    '''Extracts a list of the cards (each as a dict) from given filename or JSON dict containing a trello board. Sort might do something in future iterations (like sort by labels or lists).'''
    
    if filename:
        data = read_json_file(filename)
    elif data:
        pass
    else:
        print("Please supply either a filename or specify the variable holding the data")
        raise ValueError
    
    
    #Key for cards is, unsurpisingly, 'cards' ... 
    return data['cards']


def remove_cards(card_list, card_names_to_remove=[]):
    '''Remove cards from the list based on the names. Exact matches required. This could be nicer.'''
    
    if card_names_to_remove == []:
        return card_list
    
    cards_to_return = []
    for i in range(len(card_list)):
        card=card_list[i]
        card_name = card['name']
        for remove_name in card_names_to_remove:
            keep = True
            if card_name == remove_name:
                keep = False
                break
        
        if keep:
            cards_to_return.append(card)
            
    return cards_to_return
    
    
def strip_cards(card_list, keep_keys=['name','desc']):
    '''Pare down the card dictionarys, keeping only the keys we're interested in'''
    
    #First identify the keys to be removed
    keys_to_remove = []
    for key in card_list[0].keys():
        if any([key == x for x in keep_keys]):
            pass
        else:
            keys_to_remove.append(key)
    
    cards_to_return = []
    for card in card_list:
        for key in keys_to_remove:
            del card[key] 
        cards_to_return.append(card)
        
    return cards_to_return


def process_card_desc(card_list,debug=False):
    '''This is really specific to the description field in my case. It strips out anything that isn't the address field in the description. Debug mode will continue running if it encounters a card it doesn't understand, so you can check a whole board at once'''
    
    for card in card_list:
        desc = card['desc']
        #First check it has the expected address field and only one address
        if desc.count("Address:") != 1:
            print("I don't understand this card:")
            print(card['name'])
            if debug == False:
                raise ValueError
        
        #Okay, find the address
        idx = desc.find("Address:")
        line_list = desc[idx:].splitlines()
        #First line needs to go. As does any line after the next line starting with **
        first_line = line_list.pop(0)
        
        address = []
        if len(first_line.strip()) != 10:
            print("Warning, invalid address format; data may be lost for card:")
            print(card['name'])
            print("Attempting fix - please check result")
            address.append(first_line.strip()[10:])
            
        for line in line_list:
            if line.startswith('**'):
                break
            address.append(line.strip())
        
        card['desc'] = '\n'.join(address)
    
    return card_list
                

def write_data(filename, card_list, latex_header=default_latex_header):
    '''Takes a pared down card list and writes it to a file with the given LaTeX header. Document should then be compiled with pdflatex.'''
    
    with open(latex_header, 'r') as f:
        preamble = f.read()
        
    ##I'll need to get the dict keys. 
    #try:
        #key_list = card_list[0].keys()
    #except IndexError:
        #print("Did you pass in an empty list of cards?")
        #raise ValueError
    key_list = ['name', 'desc']
    
    with open(filename, 'a') as f:
        f.write(preamble)
        
        for card in card_list:#Have to treat the last card slightly differently
            for key in key_list:
                f.write(card[key])
                f.write('\n')
            
        f.write('\end{labels}\n')
        f.write('\end{document}')
        
    
    return 0
