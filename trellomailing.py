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


#if __name__ == "__main__":
    #read_json_file("../tests/latex_me.tex")
