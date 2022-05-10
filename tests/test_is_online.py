from bs4 import BeautifulSoup as sp
import sys
sys.path.append('..')
from src.playerOnline import is_online


def test_is_online():
    active_players = ['alex', '123', 'sara07']
    player = 'alex'
    assert True == is_online(player, active_players)
    player = '123'
    assert True == is_online(player, active_players)
    player = 'sara07'
    assert True == is_online(player, active_players)
    player = 'alexsander'
    assert False == is_online(player, active_players)
    player = ''
    assert False == is_online(player, active_players)
