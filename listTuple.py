import math

#concepte de list
ma_list = list()
ma_list = [1, 2.5, "hello", (0, 5)]
ma_list.append((2, 8))
ma_list.append("welcome")
print(type(ma_list[3]))
print(ma_list)

for i, elt in enumerate(ma_list):
    print("\"{}\" est à la position \"{}\" .".format(elt, i))
    
ma_list.remove("welcome")
ma_list.insert(len(ma_list)-1, "bienvenue")
ma_list.pop()
print("index of 'hello' : {} ".format(ma_list.index("hello")))
ma_list2 = ["coucou", math.pi, math.sqrt(55), ('x','y')]

ma_list.extend(ma_list2)
del(ma_list2) #delete variable

liste = ["je", "hamza", "timera"]
ma_list.reverse()
print(" ".join(liste))

print(liste)
print(ma_list)

# les tuples

def decompose(entier, diviseur):
    p_e = entier // diviseur
    reste = entier % diviseur
    return p_e, reste
partie_entiere, reste = decompose(45,8)
print((partie_entiere, reste))

def a_function(nom, prenom, *comments): # la liste d'arguments aprés les stdr
    return nom,prenom,comments



def afficher_flotant(flotant):
    if type(flotant) is not float:
        raise TypeError("Le parametre attendu n'est pas un float")
    tmp = str(flotant)
    p_e, p_d = tmp.split('.')
    tmp = ",".join([p_e, p_d[:3]])  #juste 3 chiffre aprés la virgule
    return tmp

print(afficher_flotant(5.))
chaine = "hamza"
print(chaine[:3]) #affiche juste les 3 premier caracteres

def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""
    
    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

afficher(1,4,5,sep="-",fin=" FIN\n")

# Transformer une liste en parametre de fonction
liste = [9,8,7,4,5,62,1]
print(*liste) # == print(9,8,7,4,5,62,1) c'est la meme chose

# Compréhension de liste

