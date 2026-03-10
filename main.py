import game
import db_init

# Menu 
def main():


    # Affiche le menu 

        def afficher_menu():

            print("1. Lance le code")
            print("2. Voir les score")
            print("3. Quitter le programme")

        afficher_menu()
    
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
    
    # Demande de choisir  une option

        option = choisir_option_valide(1, 3, "Choisissez une option : ")
        
        if option == '1':
            print("Code lance")
           #demander un nom  
            nom = input("Tapez votre nom :  \n" )
            #lister les perso dispo 
            print("Voici les perso dispo \n") 
    
            print(personnages)

            #cree une equipe avec 3 perso 
            #lancer le combat 


        elif option == '2':
            
            print("Voici les scores")
            exit()

        elif option == '3':
            print("Aurevoir"); 
            exit()
        

main()





def game():

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

    #lancer le jeu
 
    def start_game():
     print("le jeu commence" )

    #demander un nom  
    nom = input("Tapez votre nom :  \n" )
     
    #lister les perso dispo 
    print("Voici les perso dispo \n") 
    
    print(personnages)

    

    #cree une equipe avec 3 perso 
    #lancer le combat 


def afficher_score():
    print("Votre score est ...")
    quit



def quitter_jeu():
    print("fini")
quit


game()






