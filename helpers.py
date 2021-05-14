import time

def get_or_create_user(collection, id):
    currentUser = collection.find_one({"_id": id})
    if currentUser:
        return currentUser
    else: 
        collection.update_one({"_id": id}, {"$set": { "points": 0, "points_given": {} } }, upsert=True)
        newUser = collection.find_one({"_id": id})
        return newUser

def update_timestamp(currentUser, currentUserId, targetMemberId, collection):
    currentUser['points_given'][targetMemberId] = time.time()
    collection.update_one({"_id": currentUserId}, { "$set": { 'points_given': currentUser['points_given'] } }, upsert=True)