import constants as const
import requests
import key
import sys


# argv[1]: summoner/status
# argv[2]: summoner name


# *** GLOBAL VARIABLES ***
# summoner information
summoner_name, summoner_id = '', ''

#42019034 bugged
#32943077 fixxion

# api urls
url_summoner, url_spectate, url_champion = '', '', ''

#game information
game_id, game_type = '', ''

summoner_team, enemy_team = [], [] 

ally_champs, enemy_champs = [], []

#print(url_spectate)
#r = requests.get(url_summoner)
#data = r.json()
#print(data)

#print(data['id'])

# global api variables
player_r, player_data = '', ''

spectate_r, spectate_data = '', ''

champ_r, champ_data = '', ''

champ_dict = dict()

# *** HELPER FUNCTIONS ***

# retrives summoner name and id
def set_up(summoner):
	global summoner_name 
	summoner_name = summoner

	global url_summoner
	url_summoner = const.URL['base'] + const.URL['summoner'] + summoner_name + const.URL['api_key']

	global player_r, player_data
	player_r = requests.get(url_summoner)
	player_data = player_r.json()

	global summoner_id 
	#print(player_data)
	summoner_id = player_data['id']

	global url_spectate
	url_spectate = const.URL['base'] + const.URL['spectator'] + str(summoner_id) + const.URL['api_key']

	global url_champion
	url_champion = const.URL['base'] + const.URL['champion'] + "5" + const.URL['api_key']

	global champ_r, champ_data, champ_dict
	champ_r = requests.get(url_champion)
	champ_data = champ_r.json()
	#print (champ_data)

	champ_dict = champ_data['champions']
	#print(champ_dict)


# name of summoner
def get_name():
	return summoner_name

# id of summoner
def get_id():
	return summoner_id

# error 404: not in game
def is_in_game(summoner_id):
	global spectate_r, spectate_data

	spectate_r = requests.get(url_spectate)
	spectate_data = spectate_r.json()

	if 'gameId' in spectate_data:
		global game_id
		game_id = spectate_data['gameId']
		return True
	return False

# team, champs, bans, etc.
def get_game_info():
	global game_id, game_type

	global summoner_team, enemy_team
	global ally_champs, enemy_champs

	player_dict = dict()

	if (is_in_game(get_id())):
		ally_team_id = find_ally_team()
		for player in spectate_data['participants']:
			if player['teamId'] == ally_team_id:
				player_info = dict()

				# name, player id, champ name
				player_info['name'] = player['summonerName']
				player_info['player_id'] = player['summonerId']
				player_info['champion'] = find_champ(player['championId'])

				player_dict[player_info['name']] = player_info

				summoner_team.append(player['summonerName'])
				ally_champs.append(find_champ(player['championId']))
			else:
				enemy_team.append(player['summonerName'])
				enemy_champs.append(find_champ(player['championId']))


		print(get_name() + " is in a " + spectate_data['gameMode'] + " game right now!")
		print(summoner_team)
		print(ally_champs)

		print(enemy_team)
		print(enemy_champs)
		return player_dict
	else:
		print(get_name() + " is not in game right now.")
		return

# return team id of searched player
def find_ally_team():
	for player in spectate_data['participants']:
		if player['summonerName'] == summoner_name:
			return player['teamId']
	return

# return name of champ, given id
def find_champ(champ_id):
	for key, val in champ_dict.items():
		if val == champ_id:
			return val['name']


if __name__ == "__main__":
	set_up(sys.argv[1])
	#print(get_id())
	#print(str(get_id()) + "\n" + str(is_in_game(get_id())))
	get_game_info()
	

