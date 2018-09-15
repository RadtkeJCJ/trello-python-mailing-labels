import json

default_latex_header = "default_latex_header.tex"

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


def write_data(filename, card_list, latex_header=default_latex_header):
    '''Takes a pared down card list and writes it to a file with the given LaTeX header. Document should then be compiled with pdflatex.'''
    
    pass
