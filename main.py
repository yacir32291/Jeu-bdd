import game
import random
import db_init
def afficher_menu():

    print("1. Lance le code")
    print("2. Voir les score")
    print("3. Quitter le programme")

personnages = [
    {"NAME": "Guerrier", "ATK": 15, "DEF": 10, "PV": 100 },   
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
def choisir_option_valide(min_val, max_val, message):
           while True:

            choix = input(message)
            
            # Vérifie que cest un nombre
            if not choix.isdigit():

                print("Veuillez saisir un nombre")

                continue
            
            
            # Vzrifie si nombre est entre min et max
            if int(choix) < min_val or int(choix) > max_val:

                print(f"Erreur: Saisir un nombre entre {min_val} et {max_val}")
            else:
                return choix

            
    
    # Liste des perso 
personnages = [
    {"NAME": "Guerrier", "ATK": 15, "DEF": 10, "PV": 100 },   
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



def afficher_equipe():
    hero = enumerate[personnages, 1]


def demander_nom():
     nom = input("Tapez votre nom :  \n" )
     print(f"equipe de {nom} cree\n")

def cree_equipe(personnages):
    # creer liste vide 
    equipe = []

#tant que la team est pas sup a 3
    while len(equipe) < 3:
        
#creer une fonction pour afficher lequipe et afficher lequipe
        afficher_equipe()
        choix = choisir_option_valide(1 ,len(personnages) )
# perso_choisi = liste de hero avec choix -1
        perso_choisi = (personnages[choix-1])

#ajouter a ma liste 
        equipe.append(perso_choisi)

#supprimer le perso de la liste
        personnages.remove(perso_choisi)

    return equipe
    



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

def  lancer_combat():

    # Comment lancer un combat


    # tant que lequipe est vivante 
    while 
        #choisir un monstre au hazaard
        monstres_aleatoir = random.choice(monstres)
        print("Le monstre qui a ete selectionner aléatoirement est : ", monstres_aleatoir)
        # faire commbattre lequipe avec un monstre choisi au hazard

          




def afficher_score():
    pass 


def jeu():
    #demander un nom  
    nom =  demander_nom()
   
    # creer equipe
    equipe = cree_equipe()

    # combattre
    score = lancer_combat(equipe)

    # afiicher le score
    afficher_score(nom, score)
    




# Menu 
def main():

    # Affiche le menu 
    afficher_menu()
    
    # Demande de choisir  une option
    option = choisir_option_valide(1, 3, "Choisissez une option : ")
            
    if option == '1':
        jeu()

                
    elif option == '2':
                
        print("Voici les scores")
                
                

    elif option == '3':
        print("Fin du programme \n Aurevoir"); 
        exit()
            

main()







# comment creer une equipe 


# creer liste vide 
'''# equipe = []'''

#tant que la team est pas sup a 3
'''while equipe < 3'''

#afficher lequipe 
''' creer une fonction pour afficher lequipe'''

# demander de tapper un numero valide 
''' jles deja fais en haut'''

# hero_choisi = liste de hero avec choix -1

#ajouter a ma liste 
''' equipe.append(perso_choisi)'''

#supprimer le perso de la liste 
''' equipe.pop(personnage)'''









'''

if option == '1':
            print("Code lance\n")
           #demander un nom  
            nom = input("Tapez votre nom :  \n" )
            # Renvoyez le nom
            print(f"equipe de {nom} cree\n")

            #lister les perso dispo 
            print("Voici les perso dispo \n") 
            print(personnages)


            def choisir_personnages():


            #cree une equipe sa veux die faire une nouvelle liste vide avec 3 perso 
                

                equipe = choisir_personnages([personnages])
               
                      
                perso_choisi = []
                perso_choisi.append(choisir_personnages)

                #JE SAIS PAS 

            # Enlever le perso choisie cest avec list.pop
            personnages.pop(perso_choisi)

            # Afficher lequipe des 3 perso quon a prit
            print(equipe)
            #lancer le combat 
            def lancer_combat():


                lancer_combat()
            



'''