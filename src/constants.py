# api key: RGAPI-7c02d45f-63af-4b31-b73f-4f43ece052d4

import key

URL = {
	'base': 'https://na1.api.riotgames.com/lol/',
	'summoner': 'summoner/v3/summoners/by-name/',
	'spectator': 'spectator/v3/active-games/by-summoner/',
	'champion': 'platform/v3/champions/',
	'api_key': '?api_key=' + key.api_key
}

REGIONS = {
	'north_america': 'na1'
}

