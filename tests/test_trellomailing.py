import trellomailing as tm
import pytest

filename = "tests/test_board.json"
notfilename = "abcdefg.json"
notjsonfilename = "tests/latex_me.tex"


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

