import sys
import random
from tkinter import *

racine=Tk()
class Solitaire:
    def __init__(self,n=racine):
        #Initialisation de nos objets nécessaires pour jouer
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
        self.cadre= Frame(Tk(),height=640,width=640,bg="grey")

        Label(self.cadre, text="Solitaire d'Antoine et Thibault",bg="grey").grid(column=0,row=0,columnspan=15)

        #Création des boutons 
        self.boutonA=Button(self.cadre,text="Choisir",name="A",command=self.tpA.changer)
        self.boutonB=Button(self.cadre,text="Choisir",name="B",command=self.tpB.changer)
        self.boutonC=Button(self.cadre,text="Choisir",name="C",command=self.tpC.changer)
        self.boutonD=Button(self.cadre,text="Choisir",name="D",command=self.tpD.changer)
        self.boutonE=Button(self.cadre,text="Choisir",name="E",command=self.tpE.changer)
        self.boutonF=Button(self.cadre,text="Choisir",name="F",command=self.tpF.changer)
        self.boutonG=Button(self.cadre,text="Choisir",name="G",command=self.tpG.changer)
        self.tableau=[self.boutonA,self.boutonB,self.boutonC,self.boutonD,self.boutonE,self.boutonF,self.boutonG]

        # Création des cartes de la table de jeu
        self.c_A=self.retourner_etiquette_carte(self.tpA.cartedudessus,self.cadre)
        self.c_B=self.retourner_etiquette_carte(self.tpB.cartedudessus,self.cadre)
        self.c_C=self.retourner_etiquette_carte(self.tpC.cartedudessus,self.cadre)
        self.c_D=self.retourner_etiquette_carte(self.tpD.cartedudessus,self.cadre)
        self.c_E=self.retourner_etiquette_carte(self.tpE.cartedudessus,self.cadre)
        self.c_F=self.retourner_etiquette_carte(self.tpF.cartedudessus,self.cadre)
        self.c_G=self.retourner_etiquette_carte(self.tpG.cartedudessus,self.cadre)
        self.tableau_carte=[self.c_A,self.c_B,self.c_C,self.c_D,self.c_E,self.c_F,self.c_G]

        # Piles des cartes de la table de jeu
        self.p_A=[self.c_A]
        self.p_B=[self.c_B]
        self.p_C=[self.c_C]
        self.p_D=[self.c_D]
        self.p_E=[self.c_E]
        self.p_F=[self.c_F]
        self.p_G=[self.c_G]
        self.tableau_pile=[self.p_A,self.p_B,self.p_C,self.p_D,self.p_E,self.p_F,self.p_G]
        for colonne in range (2,14):
            #Label(text="{0}{1}".format(".",2619),fg="white",bg="white")
            A_label=self.retourner_etiquette_carte(self.cadre)
            A_label.grid(column=colonne,row=2)
            self.p_A.append(A_label)
            B_label=self.retourner_etiquette_carte1(self.cadre)
            B_label.grid(column=colonne,row=3)
            self.p_B.append(B_label)
            C_label=self.retourner_etiquette_carte1(self.cadre)
            C_label.grid(column=colonne,row=4)
            self.p_C.append(C_label)
            D_label=self.retourner_etiquette_carte1(self.cadre)
            D_label.grid(column=colonne,row=5)
            self.p_D.append(D_label)
            E_label=self.retourner_etiquette_carte1(self.cadre)
            E_label.grid(column=colonne,row=6)
            self.p_E.append(E_label)
            F_label=self.retourner_etiquette_carte1(self.cadre)
            F_label.grid(column=colonne,row=7)
            self.p_F.append(F_label)
            G_label=self.retourner_etiquette_carte1(self.cadre)
            G_label.grid(column=colonne,row=8)
            self.p_G.append(G_label)
        # Boutons pour les cartes nécessaire a la completion du jeu
         self.boutton_coeur=Button(self.cadre,text="Placer",command=self.objectif_coeur.changer)
    def retourner_etiquette_carte1(self,carte,cadre):
        return Label(cadre,text="{0}{1}".format(carte.lettre,carte.symbole),fg=carte.couleur,bg="white")
    def 
           

'''empiler: ajouter une carte au deck, cartetop: enlève la carte du dessus du deck et la retourne 
couleuropp: renvoie True si la couleur de la carte du dessus du deck est la même que celle mentionnée 
mmsym: renvoie True si la carte du dessus et celle mentionnée ont le mm symbole
estAs/estRoi: renvoie True si la carte est un As/Roi'''

class Deck:
    def __init__(self):
        self.statut = "Rien"
        self.nom = None
        self.cont=[]

    def empiler(self,carte):
        return self.cont.append(carte)

    def cartetop(self):
        return self.cont.pop()

    def couleuropp(self,carte):      
        return self.cartetop.couleur != carte.couleur

    def mmsym(self,carte):
        return self.cartetop.symbole == carte.symbole

    def estAs(self):
        return self.cartetop.valeur == 'As'

    def estRoi(self):
        return self.cartetop.valeur == 'Roi'


class Carte:
    def __init__(self,couleur,valeur,symbole):
        self.couleur = Couleur.c
        self.valeur = Valeur.v
        self.symbole = Symbole.s

class Couleur:
    def __init__(self,c):
        self.c = c
    nc=['rouge','noir']

class Valeur:
    def __init__(self,v):
        self.v = v
    nv=['As',2,3,4,5,6,7,8,9,10,'Valet','Dame','Roi']

class Symbole:
    def __init__(self,s):
        self.s = s
    ns=["coeur","trèfle","carreau","pique"]
