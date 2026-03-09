from pymongo import MongoClient

# Connexion à MongoDB 
client = MongoClient('mongodb://localhost:27017/')
db = client['game_db']


# Insertion des personnages
personnages = [
    {"NAME": "Guerrier", "ATK": 15, "DEF": 10, "PV": 100},
    {"NAME": "Mage", "ATK": 20, "DEF": 5, "PV": 80},
    {"NAME": "Archer", "ATK": 18, "DEF": 7, "PV": 90},
    {"NAME": "Voleur", "ATK": 22, "DEF": 8, "PV": 85},
    {"NAME": "Paladin", "ATK": 14, "DEF": 12, "PV": 110},
    {"NAME": "Sorcier", "ATK": 25, "DEF": 3, "PV": 70},
    {"NAME": "Chevalier", "ATK": 17, "DEF": 15, "PV": 120},
    {"NAME": "Moine", "ATK": 19, "DEF": 9, "PV": 95},
    {"NAME": "Berserker", "ATK": 23, "DEF": 6, "PV": 105},
    {"NAME": "Chasseur", "ATK": 16, "DEF": 11, "PV": 100}
]

# Insertion des personnages dans la collection "personnages"
db.personnages.insert_many(personnages)
print(" Personnages insérés avec succès!")

# Insertion des monstres
monstres = [
    {"NAME": "Gobelin", "ATK": 10, "DEF": 5, "PV": 50},
    {"NAME": "Orc", "ATK": 20, "DEF": 8, "PV": 120},
    {"NAME": "Dragon", "ATK": 35, "DEF": 20, "PV": 300},
    {"NAME": "Zombie", "ATK": 12, "DEF": 6, "PV": 70},
    {"NAME": "Troll", "ATK": 25, "DEF": 15, "PV": 200},
    {"NAME": "Spectre", "ATK": 18, "DEF": 10, "PV": 100},
    {"NAME": "Golem", "ATK": 30, "DEF": 25, "PV": 250},
    {"NAME": "Vampire", "ATK": 22, "DEF": 12, "PV": 150},
    {"NAME": "Loup-garou", "ATK": 28, "DEF": 18, "PV": 180},
    {"NAME": "Squelette", "ATK": 15, "DEF": 7, "PV": 90}
]

# Insertion des monstres dans la collection "monstres"
db.monstres.insert_many(monstres)
print(" Monstres insérés avec succès!")


# Initialisation des scores 
print(" Base de données initialisée avec succès!")