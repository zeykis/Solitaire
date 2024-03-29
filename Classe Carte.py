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
            A_label=self.retourner_etiquette_carte1(self.cadre)
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
           

class Pile_de_cartes:
    def __init__(self):
        self.statut = "Rien"
        self.nom = None
        self.cartes=[]
        self.cartesenmvt = 1
        self.bouton = None
        self.etiquette = None

    def empiler(self,carte):
        return self.cont.append(carte)

    def cartetop(self):
        return self.cont.pop()

    def couleuropp(self,carte):      
        return self.cartetop.couleur != carte.couleur

    def mmsym(self,carte):
        return (self.cartes[0].symbole==self.arrive.symbole)

    def estAs(self):
        return self.cartetop.valeur == 'As'

    def estRoi(self):
        return self.cartetop.valeur == 'Roi'

class Echange(Pile_de_cartes):
    def __init__(self,depart):
        Pile_de_cartes.__init__(self)
        self.type=Pile_cartes.Echange
        self.depart = depart
        self.arrive = None
        self.etat = Etat_echange.Inactif
    def valider(self,cible):
        if cible == Pile.Pile:
            return self.valider_pile()
        else:
            self.valider_tableau()
    def valider_pile(self):
        if self.mmsym():


class Deck:
    def __init__(self):
        self.cartes = []
        self.construireDeck()
        self.melange = False
        self.melangerDeck()

    def construireDeck(self):
        cartesNoms=["As","Deux"]
        carteValeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        carteLettres = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "R"]
        carteSymbole=[Symbole.Coeur]
        for i in range(4):
            temp=carteSymbole[i]
            for j in range(13):
                nouvelle_carte = Card(cartesNoms[j], temp, carteValeurs[j], carteLettres[j])
                self.cartes.append(nouvelle_carte)

    def print_deck(self):
        for cartes in self.cartes:
            print(cartes)

    def melangerDeck(self):
        for i in range(len(self.cartes)):
            position=random.randint(0,len(self.cartes)-1)
            temp=self.cards[position]
            self.cartes[position] = self.cartes[i]
            self.cartes[i] = temp
        self.melange = True






class Carte:
    def __init__(self,nom,symbole,valeur,lettre):
        self.nom=nom
        self.symbole=symbole
        self.valeur = valeur
        self.lettre = lettre
        self.Attribuer_Couleur()
        self.Attribuer_Symbole()

    def Attribuer_Couleur(self):
        if self.symbole==Symbole.Carreau or self.symbole==Symbole.Coeur:
            self.couleur=Couleur.Rouge
        if self.symbole==Symbole.Pique or self.symbole==Symbole.Trefle:
            self.couleur=Couleur.Noir
        if self.symbole==Symbole.Vide:
            self.couleur=Couleur.Blanc
        if self.symbole==Symbole.Vide2:
            self.couleur=Couleur.Marron

    def Attribuer_Symbole(self):
        if self.symbole == Symbole.Coeur:
            self.symbolenum = 2665
        if self.symbole == Symbole.Carreau:
            self.symbolenum = 2666
        if self.symbole == Symbole.Pique:
            self.symbolenum = 2660
        if self.symbole == Symbole.Trefle:
            self.symbolenum = 2663
        if self.symbole==Symbole.Vide:
            self.symbolenum = 2615
        if self.symbole==Symbole.Vide2:
            self.symbolenum = 2619
        self.symbole = chr(int(str(self.symbolenum), 16))

class Couleur:
    Rouge="Rouge"
    Noir="Noir"
    Blanc="Blanc"
    Marron="Marron"

class Etat_echange:
    Actif = 1
    Inactif = 0

class Pile:
    Pile_carte = "P"
    Tableau = "Tab"
    Tirage = "T"
    Renvoyer_une_carte = "R"
    Echange = "E"

class Symbole:
    Coeur="Coeur"
    Carreau="Carreau"
    Pique="Pique"
    Trefle="Trefle"
    Vide="Vide"
    Vide2="Vide"


if __name__=="__main__":
    jouer=Solitaire(racine)
    racine.mainloop()
