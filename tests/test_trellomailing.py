import trellomailing
import pytest

filename = "tests/test_board.json"
notfilename = "abcdefg.json"
notjsonfilename = "tests/latex_me.tex"


def test_read_json_file():
    '''Check that this raises exceptions as needed'''
    with pytest.raises(FileNotFoundError):
        trellomailing.read_json_file(notfilename)
        
    with pytest.raises(ValueError):
        trellomailing.read_json_file(notjsonfilename)

    return 1
