#  Score counter function accumulates points of the player. The player
#  accumulates points as they claim train routes during the game and it
#  needs to be collated
#
#  Written by Brian 15-04-2018

import math
import random

#  routeScoresList all possible routes between adjacent cities
#  and stores its score value in a dictionary
#
#  Start with left most city to right most city for each route
#  to keep consistent left to right direction route naming convention.
#
#  Each variable is two city names, each city is capitalised
#  by first letter only, spaces are excluded.
routeScoresList = {
    'BroomeDarwin':7,
    'KarrathaBroome':4,
    'NewmanBroome':5,
    'KarrathaNewman':2,
    'NewmanLeonora':3,
    'MtmagnetNewman':3,
    'SharkbayMtmagnet':2,
    'MtmagnetLeonora':2,
    'PerthMtmagnet':2,
    'AugustaPerth':1,
    'AugustaAlbany':2,
    'AlbanyEsperance':3,
    'EsperanceBordervillage':4,
    'LeonoraEsperance':5,
    'EsperanceAlicesprings':6,
    'HallscreekAlicesprings':5,
    'BroomeHallscreek':3,
    'DarwinAlicesprings':7,
    'DarwinNhulunbuy':3,
    'NhulunbuyBurketown':4,
    'AlicespringsBurketown':5,
    'BurketownKarumba':1,
    'AlicespringsCooberpedy':5,
    'BordervillageAdelaide':6,
    'CooberpedyAdelaide':3,
    'AdelaidePortland':4,
    'CooberpedyMtisa':7,
    'KarumbaMtisa':4,
    'PortlandMelbourne':2,
    'KarumbaCapeyork':6,
    'CapeyorkCooktown':2,
    'CooktownMackay':2,
    'CapeyorkMackay':6,
    'MtisaMackay':3,
    'MackayBundaberg':4,
    'MtisaBourke':4,
    'BourkeBundaberg':5,
    'BundabergBrisbane':2,
    'MilduraBourke':3,
    'MelbourneMildura':3,
    'HobartMelbourne':4,
    'MelbourneCanberra':3,
    'MelbourneSydney':7,
    'CanberraSydney':3,
    'BourkeSydney':4,
    'SydneyBrisbane':4
}

#  For each player give them a starting array that will contain their completed routes.
#  But assume for now, 1 player.
players = [] #players should be named player1, player2 etc.
player1Routes = []
player2Routes = []
player3Routes = []
player4Routes = []
player5Routes = []  
scores = []

#  Add players to game
def addPlayers(name: str):
    players.append(name)

#  Assigns completed route (string such as CanberraSydney) to player's routelist array
def recordCompletedRoute(route: str, playerRouteList: list):
    # Note: Need to check if route is valid based on routeScoresList
    if route in routeScoresList.keys():
        playerRouteList.append(route)
        print('Route has been successfully entered into the player''s completed routes')
    else:
        print('Route entered is invalid or misspelled')
    
#  Calculates total score of the player based on their completed routes list/array
def scoreCounter(playerRouteList: list):
    score = 0
    for x in playerRouteList:
        score = score + routeScoresList[x]
    return score

#  Displays all end scores of each player
def endScoreDisplay(players):
    for i in range(0,len(players)-1):
        playerScore = scoreCounter(eval(players[i] + 'Routes'))
        print(players[i] + ' final score is ' + playerScore)
    





    
    


    


    

