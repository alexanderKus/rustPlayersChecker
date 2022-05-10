from bs4 import BeautifulSoup as sp
import sys
sys.path.append('..')
from src.playerOnline import get_players


def test_get_players():
    url = 'http://0.0.0.0:8000/html_for_testing.html'
    players = get_players(url)
    assert ['alex', '123', 'sara07'] == players
    

