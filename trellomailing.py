import json

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
    '''Remove cards from the list based on the names.'''
    
    if card_names_to_remove == []:
        return card_list
    
    
    
    pass
    
def strip_cards(card_list, keep_keys=['name','desc']):
    '''Pare down the card dictionarys, keeping only the keys we're interested in'''
    
    pass


def write_data(filename, card_list, latex_header=default_latex_header):
    '''Takes a pared down card list and prints it to a file with the given LaTeX header. Document should then be compiled with pdflatex.'''
    
    pass
