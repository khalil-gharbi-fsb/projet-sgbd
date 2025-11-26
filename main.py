from pymongo import MongoClient
from lib.functions import *

# version cloud : mongodb+srv://admin:123@projet-sgbd.nj5db3r.mongodb.net/?appName=Projet-sgbd
client = MongoClient("mongodb://localhost:27017/")

db = client["bd"] # creer ou selectionner base de données
users = db["users"] # creer ou selectionner une collection

new_user = {
    "username": "alice",
    "email": "alice@example.com",
    "age": 18
}

result = create_user(users,new_user)
print("Utilisateur inséré avec l'identifiant:", result.inserted_id)


user = find_user(users,{"username" : "alicee"})
if user:
    print("Utilisateur trouvé:", user)
else:
    print("Utilisateur introuvable")
result = update_user(users,{"username" : "alice"},{"email" : "alice@gmail.com"})
print("Correspondance:", result.matched_count)
print("Modifié:", result.modified_count)
result = delete_user(users,{"age" : 18})
print("Supprimé :",result.deleted_count)