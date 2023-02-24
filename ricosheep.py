from fltk import *
def menu(taille_fenetre):
    ''' Affiche le menu du jeu et permet a l'utilisateur de choisir le mode de jeu '''
    x_0, y_0 = taille_fenetre
    lst=[]
    cree_fenetre(x_0,y_0)
    #rectangle(0,0,x_0,y_0,'black','white')
    texte(300,20,'Ricosheep' ,'green','c')
    texte(80, 200 , ' Jouer ','black' ,'c', taille = 18)
    lst.append(image(40 ,100 , 'Media/sheep.png' , ancrage='nw'))
    texte(300, 280,' Solveur','black','c' , taille= 18)
    lst.append(image(260,170,'Media/grass.png' , ancrage='nw'))
    texte(520 ,185,' Quitter ','black', 'c',taille= 18)
    lst.append(image(480,212,'Media/bush.png',ancrage='nw'))
    x ,y= appuie()
    bool= False
    while(bool == False ) :
        if( x > 480 and x <550) and(y > 200 and y < 300):
            return None
        elif( x > 40 and x < 125) and (y> 104 and y < 176):
            return True
        elif ( x > 265 and x < 350) and (y> 215 and y < 264):
            return 'SOL'

def appuie():
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == "ClicDroit":
            return(abscisse(ev), ordonnee(ev))
        elif tev == "ClicGauche":
            return(abscisse(ev), ordonnee(ev))
        elif tev == 'Quitte':
            break
        else:  
            pass
        mise_a_jour()
def ecriture():
    """fonction qui permet d'ecrire a partir du clavier et renvoyer le mot"""
    mots = ''
    text = ''
    while True:
        ev = donne_ev()
        if type_ev(ev) == 'Touche':
            if touche(ev) == 'Return':
                efface(text)
                return mots
            elif touche(ev) == 'BackSpace':
                if len(mots) > 0:
                    efface(text)
                    mots = mots[: len(mots )-1]
                    text = texte(50, 100 , f'{mots}' , taille = 15)

            else:
                efface(text)
                if (touche(ev) == 'period'):
                    mots += '.'
                elif ( touche(ev) == 'underscore'):
                    mots+='_'
                else :
                    mots+= touche(ev)
                    if(( touche(ev) == 'Caps_Lock' )):
                        mots= mots.removesuffix(touche(ev))
                text = texte(50, 100, f'{mots}' , taille = 15)   
        mise_a_jour()
def input_graph():
    """fonction qui permet de faire une saisie controler des noms des fichiers de grille existante """
    lst=['big1.txt','big2.txt', 'big3.txt', 'huge.txt' ,'map1.txt' ,'map2.txt', 'map3.txt' ,"losable.txt",'test_move.txt',
    'one_sheep.txt' ,'onegrass.txt' ,'one_sheep2.txt' , 'wide1.txt','wide2.txt','wide3.txt' , 'wide4.txt']
    rep= menu((600,300))
    if(rep) or (rep == 'SOL '):
        ferme_fenetre()
        cree_fenetre(350,150)
        tx= texte(20,20,'Nom du fichier de votre grille','black','nw',taille=15)
        txx =''
        rectangle(45,100,180,122)
        mots=ecriture()
        while not (mots in lst ):
            efface(txx)
            efface(tx)
            txx = texte(20,20,'Ce fichier est introuvable' ,'Red', taille= 15)
            tx = texte(20,50,'Choissisez un nom de fichier deja existant' ,'Black', taille= 10)
            mots=ecriture()
        return mots, rep
    elif( rep == None):
        return None , rep
def cadrillage(taille_fenetre , plateau ,moutons):
    '''permet de dessiner la grille'''
    x_0, y_0 = taille_fenetre
    x = len(plateau[0])
    y= len(plateau)
    cree_fenetre(x_0, y_0)
    for i in range(x):
        for j in range(y):
            rectangle(i*80,j*80 ,80 *(i+1),80 *(j+1))
    ligne(80*(x),0,80*(x),80*(y) , couleur='Black')
def placement(plateau , moutons):
    """ Permet de placer les motouns a leurs places"""
    mise_a_jour()
    lst = []
    for i in range(len(plateau)):
        lst.append([None]* len(plateau[i]))
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if( (i,j) in moutons ):
                lst[i][j] = image( (80 *j) +10 , (80*i)+10 , 'Media/sheep.png' , ancrage='nw')
            else :
                if( plateau[i][j] == 'B'):
                    lst[i][j] = image( (80 *j) +10 , (80*i)+10 , 'Media/bush.png' , ancrage='nw')
                elif(plateau[i][j] == 'G'):
                    lst[i][j] = image( (80 *j) +10 , (80*i)+10 , 'Media/grass.png' , ancrage='nw')
    mise_a_jour()
    return lst
def direction():
    while True:
        ev = donne_ev()
        if type_ev(ev) == 'Touche':
            if(touche(ev) in dic ) or( touche(ev) == 'R') or (touche(ev) == 'Escape' ):
                return touche(ev)
        mise_a_jour()

def affiche_mots(nomfichier) :
    '''Fonction qui permets a partir d'un nom de fichiers de renvoyer la liste du plateau et la liste des moutons'''
    plateau=[]
    moutons=[]
    f=open(nomfichier,'r')
    s= f.read()
    lst=s.split('\n')
    for i in range(len(lst)):
        if(lst[i] != ''):
            s = lst[i]
            lst2=[]
            for j in range(len(s)) :
                if(s[j] == '_'):
                    lst2.append(None)
                elif(s[j]== 'S'):
                    lst2.append(None)
                    moutons.append((i,j))
                elif(s[j] == 'B') or (s[j] =='G'):
                    lst2.append(s[j])
                else:
                    return None
            plateau.append(lst2)
    return( plateau,moutons) 
def soucis( plateau):
    lst=[]
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if( plateau[i][j] == 'B' ):
                lst.append((i,j))
    return lst
def jouer(plateau , moutons , direction):
    bis= list(moutons)
    lst = soucis(plateau)
    if(direction == 'Left'):
        for i in range(len(moutons)):
            lig = moutons[i][0]
            col = moutons[i][1]
            while  ( col >= 0)  and  ( not( (lig,col) in lst ) ):
                col-=1
            lst.append((lig,col+1))   
            moutons[i] = (lig , col + 1 )
    elif (direction == 'Right'):
        for i in range(len(moutons) - 1 , -1,-1):
            lig = moutons[i][0]
            col = moutons[i][1]
            while  ( col < len(plateau[lig]))  and  ( not( (lig,col) in lst ) ):
                col+=1
            lst.append((lig,col-1))   
            moutons[i] = (lig , col-1 )
    elif(direction == 'Up'):
        for i in range(len(moutons)):
            lig = moutons[i][0]
            col = moutons[i][1]
            while  ( lig >= 0 )  and  ( not( (lig,col) in lst ) ):
                lig -=1
            lst.append((lig + 1,col))   
            moutons[i] = (lig + 1, col)
    elif(direction == 'Down'):
        for i in range(len(moutons)-1 , -1 ,-1):
            lig= moutons[i][0]
            col = moutons[i][1]
            while( lig < len(plateau) ) and ( not( (lig,col) in lst ) ):
                lig+=1
            lst.append((lig - 1 , col))
            moutons[i] = (lig - 1 , col)
    return bis
def victoire(plateau , moutons ):
    mb=0
    lst=[]
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if(plateau[i][j] == 'G'):
                mb+=1
                lst.append((i,j))
    nb=0
    for i in range(len(moutons)):
        if (moutons[i] in lst ):
            nb+=1
    return mb == nb
def dessin():
    cadrillage(taille_fenetre,plateau , moutonsbis)
    return( placement(plateau,moutonsbis))
def _solveur(plateau , moutons, visite ):
    m= tuple(moutons)
    if(victoire(plateau , moutons)) :
        return []
    elif(m in visite):
        return None
    else:
        visite.add(m)
        biis= list(moutons)
        for i in dic :
            jouer(plateau , moutons, i)
            S = _solveur(plateau , moutons, visite)
            if(S is not None):
                return [i] + S
            else:
                moutons = list(biis)

def solveur(plateau , moutons):
    visite = set()
    return _solveur(plateau , moutons , visite)
nom , rep = input_graph()
while(nom != None ):
    lst=[]
    ferme_fenetre()
    plateau , moutons = affiche_mots( 'Media/' + nom)
    moutonsbis = list(moutons)
    dic=['Left','Right','Up','Down']
    if(rep == 'SOL'):
        print(solveur(plateau , moutons))
        break
    else:
        taille_fenetre= (len(plateau[0]) *81 , len(plateau) * 81 )
        lst = dessin() 
        vic = victoire(plateau,moutons)
        while(vic != True ):
            dice= direction()
            if( dice in dic ):
                bis= jouer(plateau,moutons,dice)
                for i in range(len(bis)):
                    k,j = bis[i]
                    efface(lst[k][j])
                lst = placement(plateau,moutons)
            elif( dice == 'R'):
                ferme_fenetre()
                moutons = list(moutonsbis) # pour recuperer les position initiale des moutons
                lst = dessin()
            elif(dice == 'Escape'):
                break
            vic = victoire(plateau,moutons)
        if(vic):
            texte(taille_fenetre[0] // 2 , taille_fenetre[1] // 2 , 'YOU WIN','black' ,'c')
            attend_clic_gauche()
        ferme_fenetre()
        nom , rep =input_graph()
   