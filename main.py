import game
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
    {"1": "Guerrier", "ATK": 15, "DEF": 10, "PV": 100 },   
    {"2": "Mage", "ATK": 20, "DEF": 5, "PV": 80},
    {"3": "Archer", "ATK": 18, "DEF": 7, "PV": 90},
    {"4": "Voleur", "ATK": 22, "DEF": 8, "PV": 85},
    {"5": "Paladin", "ATK": 14, "DEF": 12, "PV": 110},
    {"6": "Sorcier", "ATK": 25, "DEF": 3, "PV": 70},
    {"7": "Chevalier", "ATK": 17, "DEF": 15, "PV": 120},
    {"8": "Moine", "ATK": 19, "DEF": 9, "PV": 95},
    {"9": "Berserker", "ATK": 23, "DEF": 6, "PV": 105},
    {"10": "Chasseur", "ATK": 16, "DEF": 11, "PV": 100}
]


def demander_nom():
    nom = input("Tapez votre nom :  \n" )
    print(f"equipe de {nom} cree\n")

def cree_equipe():
    equipe = []


def  lancer_combat():
    combat = 

def afficher_score():
    score = 


def jeu():
    #demander un nom  
    nom = demander_nom()
   
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
            #demander un nom  
            
                # Renvoyez le nom

                #lister les perso dispo 

                #cree une equipe sa veux die faire une nouvelle liste vide avec 3 perso 

                # demander a choisir un perso
                    
                # Enlever le perso choisie cest avec list.pop et lafficher dans la nouvelle liste

                # Afficher lequipe des 3 perso quon a prit
                
                #lancer le combat 
                
    elif option == '2':
                
        print("Voici les scores")
                
                

    elif option == '3':
        print("Fin du programme \n Aurevoir"); 
        exit()
            

main()





# Comment cree une equipe 

# creer une liste vide 
'''# equipe = []'''

''' faire une boucle pour que sa me demande de le faire 3x'''

# ajouter a cette liste 1 perso qui a ete afficher au prealable 
'''# equipe.append(perso_choisie)'''

# supprimer le perso de la liste afficher et rechoisir x2 
'''# equipe.pop(personnage) '''

# equipe fini









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
            


elif option == '2':
            
            print("Voici les scores")
            exit()

elif option == '3':
            print("Fin du programme \n Aurevoir"); 
            exit()
        

main()
'''