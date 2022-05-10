#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import argparse
from colorama import Fore


'''
Program checks if player is on the server.
'''


def get_players(url: str) -> list[str]:
    '''Get list of active player from given url'''
    html_doc = requests.get(url).content
    soup = BeautifulSoup(html_doc, 'html.parser')

    players = soup.find_all('a', class_='css-zwebxb')
    players_list = [p.string for p in players]

    return players_list


def is_online(player: str, active_players: list[str]) -> bool:
    '''Return Boolean if player is on the list of active_players'''
    return player in active_players


def check(url: str, player: str) -> None:
    '''Check is player is on the list with active players'''
    if len(player) <= 0:
        print(Fore.YELLOW + 'nickname cannot be empty')
        return

    active_players = get_players(url)
    if is_online(player, active_players):
        print(Fore.RED + player + Fore.WHITE + ' is online')
    else:
        print(Fore.GREEN + player + Fore.WHITE + ' is offline')


def main() -> int:
    parse = argparse.ArgumentParser()
    parse.add_argument('--url', type=str, required=True,
                       help='url to battlemetrics.com with correct server')
    parse.add_argument('--nick', type=str, required=True,
                       help='player nickname')
    args = parse.parse_args()
    
    check(args.url, args.nick)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
