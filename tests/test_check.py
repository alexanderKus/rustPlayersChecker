from bs4 import BeautifulSoup as sp
import sys
sys.path.append('..')
from src.playerOnline import is_online, get_players, check
from colorama import Fore


def test_check(capsys):
    url = 'http://0.0.0.0:8000/html_for_testing.html'

    player = 'alex'
    check(url, player)
    stdout, stderr = capsys.readouterr()
    assert (Fore.RED + player + Fore.WHITE + ' is online\n') == stdout

    player = '123'
    check(url, player)
    stdout, stderr = capsys.readouterr()
    assert (Fore.RED + player + Fore.WHITE + ' is online\n') == stdout
    
    player = 'sara07'
    check(url, player)
    stdout, stderr = capsys.readouterr()
    assert (Fore.RED + player + Fore.WHITE + ' is online\n') == stdout

    player = ''
    check(url, player)
    stdout, stderr = capsys.readouterr()
    assert (Fore.YELLOW +'nickname cannot be empty\n') == stdout

    player = 'aleksander'
    check(url, player)
    stdout, stderr = capsys.readouterr()
    assert (Fore.GREEN + player + Fore.WHITE + ' is offline\n') == stdout
