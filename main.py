from pymongo import MongoClient

def stop(msg) :
    input(msg)

# version cloud : mongodb+srv://admin:123@projet-sgbd.nj5db3r.mongodb.net/?appName=Projet-sgbd
# version local : mongodb://localhost:27017/

version = input("Souhaitez-vous utiliser le cloud ou rester en local ?\n")
if version == "cloud" :
    client = MongoClient("mongodb+srv://admin:123@projet-sgbd.nj5db3r.mongodb.net/?appName=Projet-sgbd")
elif version == "local" : 
    client = MongoClient("mongodb://localhost:27017/")

db = client["bd"] # creer ou selectionner base de données
users = db["users"] # creer ou selectionner une collection

new_user = {
    "username": "salah",
    "email": "salah@example.com",
    "age": 18
}
stop("inserer les données de l'utilisateur")
result = users.insert_one(new_user)
print("Utilisateur inséré avec l'identifiant:", result.inserted_id)

stop("trouver un utilisateur")
user = users.find_one({"username" : "salah"})
if user:
    print("Utilisateur trouvé:", user)
else:
    print("Utilisateur introuvable")
stop("mise à jour des données utilisateur")
result = users.update_many({"username" : "salah"},{"$set":{"email" : "salah@gmail.com"}})
print("Correspondance:", result.matched_count)
print("Modifié:", result.modified_count)
user = users.find_one({"username" : "salah"})
if user:
    print("Utilisateur trouvé:", user)
else:
    print("Utilisateur introuvable")
stop("supprimer l'utilisateur")
result = users.delete_many({"age" : 18})
print("Supprimé :",result.deleted_count)
user = users.find_one({"username" : "salah"})
if user:
    print("Utilisateur trouvé:", user)
else:
    print("Utilisateur introuvable")