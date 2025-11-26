
def create_user(collection,user) :
    result = collection.insert_one(user)
    return result

def find_user(collection,user) :
    user = collection.find_one(user)
    return user

def update_user(collection,filter,modif) : 
    result = collection.update_many(
        filter,      
        {"$set": modif}  
    )
    return result


def delete_user(collection,filter) :
    result = collection.delete_many(filter)
    return result