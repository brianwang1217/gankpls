import constants as const
import requests
import key
import sys


URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/bwub?api_key=" + key.api_key

def get_name(summoner_name):
	return summoner_name

name = get_name(sys.argv[1])
player_id = '42019034'

url_summoner = const.URL['base'] + const.URL['summoner'] + name + "?api_key=" + key.api_key
url_spectate = const.URL['base'] + const.URL['spectator'] + player_id + "?api_key=" + key.api_key

print(url_spectate)
r = requests.get(url_spectate)
data = r.json()
print(data)

#if __name__ == "__main__":

