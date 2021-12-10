import random
from colorama import init
init()
from colorama import Fore


liste = ["muscle","menthe","sangle","grille","dicton","famine","espace","griffe","billet","phrase"]

#--------------------------------------------------var------------------------------------------------------

nombreR = random.randint(0, 9)
MotATrouver = liste[nombreR]
Trouver = False
LettreCorrect = 0
vie = 8
Fin = False

#--------------------------------------------------corps du prog------------------------------------------------------

print(MotATrouver)
print("_ _ _ _ _ _")


while Fin != True:
    print (Fore.WHITE + "Il te reste", vie , "vies.")
    motjoueur = input("Quel mot ? ")
    for i in range (len(MotATrouver)):
        if motjoueur[i] == MotATrouver[i]:
            print(Fore.RED + motjoueur[i] ,  end=" ")
        else :
            for e in range (len(MotATrouver)):
                if motjoueur[i] == MotATrouver[e]:
                    if MotATrouver[e] == motjoueur[e]:
                        print(Fore.BLUE + motjoueur[i] ,  end=" ")
                    else :
                        print(Fore.YELLOW + motjoueur[i] ,  end=" ")
                    break
            else :
                print (Fore.BLUE + motjoueur[i] , end=" ")
    print(end='\n')
    LettreCorrect = 0
    vie -= 1

    #-----------------------------------------------mot trouver----------------------------------------------------

    for a in range (len(MotATrouver)):
        if motjoueur[a] != MotATrouver[a]:
            break
        else :
            LettreCorrect += 1

    #---------------------------------------------condition fin----------------------------------------------------

    if LettreCorrect == 6 or vie == 0 :
        Fin = True


#--------------------------------------------------print fin------------------------------------------------------

if LettreCorrect == 6 :
    print(Fore.WHITE + "bien jouer")
else :
    print(Fore.WHITE + "tu as perdu, le mot était" , Fore.RED + MotATrouver)