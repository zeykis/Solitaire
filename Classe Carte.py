class Carte:
    def __init__(self,couleur,valeur,symbole):
        self.couleur = Couleur.c
        self.valeur = Valeur.v
        self.symbole = Symbole.s
class Couleur:
    def __init__(self,c):
        self.c = c
    nc=['coeur','trèfle','pique','carreau']
class Valeur:
    def __init__(self,v):
        self.v = v
    nv=['as',2,3,4,5,6,7,8,9,10,'Valet','Dame','Roi']
class Symbole:
    def __init__(self,s):
        self.s = s
    ns=["coeur","trèfle","carreau","pique"]
