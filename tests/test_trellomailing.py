import trellomailing as tm
import pytest

filename = "tests/test_board.json"
notfilename = "abcdefg.json"
notjsonfilename = "tests/latex_me.tex"

non_address_cards = ["Card Template", "Here is a test about this board card", "And here is another", "(This board really is for tests!)"]

@pytest.fixture
def full_card_list():
    return tm.get_card_list(filename)
    

def test_read_json_file():
    with pytest.raises(FileNotFoundError):
        tm.read_json_file(notfilename)
        
    with pytest.raises(ValueError):
        tm.read_json_file(notjsonfilename)
        
    assert type(tm.read_json_file(filename)) == dict

    return 1


def test_get_card_list_exceptions():
    with pytest.raises(ValueError):
        tm.get_card_list()
        
    assert type(tm.get_card_list(filename)) == list
        
    return 1


def test_remove_cards(full_card_list):
    assert len(tm.remove_cards(full_card_list, ["Card Template"])) == 9
    
    assert len(tm.remove_cards(full_card_list, non_address_cards)) == 6
    
    return 1
