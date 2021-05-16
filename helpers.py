import time
from pymongo import ReturnDocument

def get_or_create_user(collection, id):
    currentUser = collection.find_one({"_id": id})
    if currentUser:
        return currentUser
    else: 
        newUser = collection.find_one_and_update({"_id": id}, {"$set": { "points": 0, "points_given": {} } }, upsert=True, return_document=ReturnDocument.AFTER)
        return newUser

def update_timestamp(currentUser, currentUserId, targetMemberId, collection):
    currentUser['points_given'][targetMemberId] = time.time()
    collection.update_one({"_id": currentUserId}, { "$set": { 'points_given': currentUser['points_given'] } }, upsert=True)


def compute_winner(game):
    if game['player'] == 3:
        return "Player"
    elif  game['bot'] == 3:
        return "Bot"
    return False

def compute_score(bot_pick, player_pick, game):
    game = game
    if (bot_pick == player_pick):
        return game
    if bot_pick == "tijera" and player_pick == "papel" or bot_pick == "papel" and player_pick == "piedra" or bot_pick == "piedra" and player_pick == "tijera":
        game['bot'] += 1
    else:
        game['player'] += 1
    return game

def decir_puntaje(game):
    return f"Tienes {game['player']}/3 puntos -- El bot tiene {game['bot']}/3 puntos"