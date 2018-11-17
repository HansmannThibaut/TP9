# Pour la lecture, les instructions sous forme de commentaire

'''Regardez d'abord votre fichier texte: commentez sa première ligne pour ne pas avoir de message d'erreur lors de la lecture, puis coupez éventuellement des lignes ne servant à rien (régime permanent)'''


import numpy as np
# Lecture effective du fichier: temps et tension
mesures_t,mesures_u,= np.loadtxt('TP9, courbe Uc.txt',unpack=True)

'''Les commandes qui suivent vous permettent de visualiser vos mesures (si vous décommentez):'''
import matplotlib.pyplot as plt
plt.plot(mesures_t,mesures_u)
plt.grid()
plt.xlabel("t (s)")
plt.ylabel("u (V)")
plt.show()


''' mesures_t et mesures_u sont les listes de valeurs. Déterminer d'abord une liste donnant la dérivée pour afficher le portrait de phase'''

taille = len(mesures_u)
derivee_de_u=[]
i = 1
#création de la liste des dérivée
for i in range (taille):
    
    Du = (mesures_u[i]-mesures_u[i-1])/(mesures_t[i]-mesures_t[i-1])
    derivee_de_u.append(Du)
    
#mise en graphique    
'''plt.plot(mesures_u,derivee_de_u)
plt.grid()
plt.ylabel("du/dt")
plt.xlabel("u (V)")
plt.show()'''




''' A vous de jouer en definissant la fonction ou le code qui permet de déterminer la pseudopériode T des oscillations: afficher cette pseudopériode. Indication: utiliser les changements de signe de la tension'''

def pseudo_periode(a,b):
    '''a et b sont des listes avec a la listes mesurant la tension et b la liste de cette fonction en fonction du temps. Le but est de trouvé la pseudo période du système'''
    N= 0
    taille = len (a)
    #on regarde toutes les valeurs de la listes quand on atteint 0 on a le début de notre période
    for i in range(taille):
        if a[i] <= 0:
          debut = b[i-1]
          x = i
          break
    #on regarde a nouveau la liste pour savoir quand nous somme a nouveau dans les positifs
    for i in range(x,taille):
        if a[i] >= 0:
            y = i
            break
    #enfin on regarde la liste pour savoir quand on reppasse le zero on a notre fin de période
    for i in range(y,taille):
        if a[i] <= 0:
            fin = b[i-1]
            break
    #on fait la différence du début et de la fin 
    periode = fin - debut
           
    return periode

print (pseudo_periode(mesures_u,mesures_t))

''' A vous de jouer pour déterminer les valeurs des maxima successifs'''

def maximus_positif(a):
    '''a est une liste de tensions '''
    
    positif = []
    maximus = []
    test = 0
    maxi = 0
    
    for i in a:
        
        if i >= 0:
            positif.append(i)
            test += 1
        else:
            if test != 0:
                test_2 = maxi
                maxi = max(positif)
                if test_2-maxi ==0:
                    break
                maximus.append(maxi)
                positif = []
                test = 0
        
    return maximus



''' puis d'en déduire la valeur du facteur de qualité sachant que les maxima suivent A*exp-(omega0*t/(2*Q))'''

