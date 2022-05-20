from cgitb import grey
import sys
import random
from tkinter import *
racine=Tk()
class Solitaire:
    def __init__(self,n=racine):
        ##Initialisation de nos objets nécessaires pour jouer
        self.deck=piledecarte()
        self.tpA=tableauPile()
        self.tpB=tableauPile()
        self.tpC=tableauPile()
        self.tpD=tableauPile()
        self.tpE=tableauPile()
        self.tpF=tableauPile()
        self.tpG=tableauPile()
        self.tableau=[self.tpA,self.tpB,self.tpC,self.tpD,self.tpE,self.tpF,self.tpG]
        self.objectif_coeur=objectifPile(suite.coeur)
        self.objectif_carreau=objectifPile(suite.carreau)
        self.objectif_pique=objectifPile(suite.pique)
        self.objectif_trefle=objectifPile(suite.trefle)
        self.tirage=tirage()
        self.ecarter_carte=ecarter()
        self.temp=transition()
        self.distribuerCarte()

        #Grille
        self.ligneHaut = 2
        self.cadre= Frame(Tk(),height=640,width=640,bg=grey)

        Label(self.cadre, text="Solitaire d'Antoine et Thibault",bg="grey").grid(column=0,row=0,columnspan=15)
        
    


class Deck:
    def __init__(self):
        self.statut = "Rien"
        self.nom = None

    def empiler(self,carte):
        self.append(carte)

    def depiler(self):
        self.cont.pop()





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
