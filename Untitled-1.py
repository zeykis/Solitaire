
import random
from symtable import Symbol
from tkinter import *

racine=Tk()
class Solitaire:
    def __init__(self):
        #Initialisation de nos objets nécessaires pour jouer
        self.deck=Deck()
        self.tpA=tableauPile()
        self.tpB=tableauPile()
        self.tpC=tableauPile()
        self.tpD=tableauPile()
        self.tpE=tableauPile()
        self.tpF=tableauPile()
        self.tpG=tableauPile()
        self.tableau=[self.tpA,self.tpB,self.tpC,self.tpD,self.tpE,self.tpF,self.tpG]
        self.objectif_coeur=OPile(Symbole.Coeur)
        self.objectif_carreau=OPile(Symbole.Carreau)
        self.objectif_pique=OPile(Symbole.Pique)
        self.objectif_trefle=OPile(Symbole.Trefle)
        self.tirage=tirage_pile()
        self.ecarter_carte=Pile_renvoi()
        self.obj_temp = Echange (None)
        self.cartevide=Carte("Vide",Symbole.Vide2,0,".")
        self.cartevide2=Carte("Vide2",Symbole.Vide,0,"_")
        self.boutonvide2=Carte("Vide2",Symbole.Vide,0,"-------")
        self.distribuerCarte()

        #Grille
        self.ligneHaut = 2
        self.cadre= Frame(Tk(),height=640,width=640,bg="grey")
        self.cadre.pack()

        Label(self.cadre, text="Solitaire d'Antoine et Thibault",bg="grey").grid(column=0,row=0,columnspan=15)

        #Création des boutons 
        self.boutonA=Button(self.cadre,text="Choisir",name="_A",command=self.changerButtonA)
        self.boutonB=Button(self.cadre,text="Choisir",name="_B",command=self.changerButtonB)
        self.boutonC=Button(self.cadre,text="Choisir",name="_C",command=self.changerButtonC)
        self.boutonD=Button(self.cadre,text="Choisir",name="_D",command=self.changerButtonD)
        self.boutonE=Button(self.cadre,text="Choisir",name="_E",command=self.changerButtonE)
        self.boutonF=Button(self.cadre,text="Choisir",name="_F",command=self.changerButtonF)
        self.boutonG=Button(self.cadre,text="Choisir",name="_G",command=self.changerButtonG)
        self.tableau_button=[self.boutonA,self.boutonB,self.boutonC,self.boutonD,self.boutonE,self.boutonF,self.boutonG]

        # Création des cartes de la table de jeu
        self.c_A=self.retourner_etiquette_carte1(self.tpA.carte_dessus(),self.cadre)
        self.c_B=self.retourner_etiquette_carte1(self.tpB.carte_dessus(),self.cadre)
        self.c_C=self.retourner_etiquette_carte1(self.tpC.carte_dessus(),self.cadre)
        self.c_D=self.retourner_etiquette_carte1(self.tpD.carte_dessus(),self.cadre)
        self.c_E=self.retourner_etiquette_carte1(self.tpE.carte_dessus(),self.cadre)
        self.c_F=self.retourner_etiquette_carte1(self.tpF.carte_dessus(),self.cadre)
        self.c_G=self.retourner_etiquette_carte1(self.tpG.carte_dessus(),self.cadre)
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
            A_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            A_label.grid(column=colonne,row=2)
            self.p_A.append(A_label)
            B_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            B_label.grid(column=colonne,row=3)
            self.p_B.append(B_label)
            C_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            C_label.grid(column=colonne,row=4)
            self.p_C.append(C_label)
            D_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            D_label.grid(column=colonne,row=5)
            self.p_D.append(D_label)
            E_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            E_label.grid(column=colonne,row=6)
            self.p_E.append(E_label)
            F_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            F_label.grid(column=colonne,row=7)
            self.p_F.append(F_label)
            G_label=self.retourner_etiquette_carte1(self.cartevide,self.cadre)
            G_label.grid(column=colonne,row=8)
            self.p_G.append(G_label)

        # Boutons pour les cartes nécessaire a la completion du jeu
        self.oB_Pique = Button(self.cadre, text="Placer", command=self.placePique)
        self.oB_Coeur = Button(self.cadre, text="Placer", command=self.placecCoeur)
        self.oB_Trefle = Button(self.cadre, text="Placer", command=self.placeTrefle)
        self.oB_Carreau = Button(self.cadre, text="Placer", command=self.placeCarreau)
        self.oButtons = [self.oB_Pique, self.oB_Coeur, self.oB_Trefle, self.oB_Carreau]

        # Emplacement d'objectifs
        self.emp_Pique = self.retourner_etiquette_objectif(self.objectif_pique.carte_dessus(), Symbole.Pique, self.cadre)
        self.emp_Coeur = self.retourner_etiquette_objectif(self.objectif_coeur.carte_dessus(), Symbole.Coeur, self.cadre)
        self.emp_Trefle = self.retourner_etiquette_objectif(self.objectif_trefle.carte_dessus(), Symbole.Trefle, self.cadre)
        self.emp_Carreau = self.retourner_etiquette_objectif(self.objectif_carreau.carte_dessus(), Symbole.Carreau, self.cadre)
        self.obj_carte = [self.emp_Pique, self.emp_Coeur, self.emp_Trefle, self.emp_Carreau]

        Label(self.cadre, text="Ecarter", bg="white").grid(row=self.ligneHaut, column=14)
        self.b_ecarter = Button(self.cadre, text="Choisir", command=self.onClick_ecarter)
        self.p_ecarter = self.retourner_etiquette_objectif(self.ecarter_carte.carte_dessus(), Symbole.Vide, self.cadre)

        Label(self.cadre,text="Pile Tirage",bg="white").grid(row=self.ligneHaut,column=15)
        self.b_tirage = Button(self.cadre, text="Tirer", command=self.onClick_tirage)


        # Boutons du tableau
        compteur_bouton=self.ligneHaut
        for b in self.tableau_button:
            b.grid(row=compteur_bouton,column=0)
            compteur_bouton+=1

        # Tableau des cartes
        compteur_carte=self.ligneHaut
        for c in self.tableau_button:
            c.grid(row=compteur_carte,column=1)
            compteur_carte+=1

        # Emplacement des boutons d'objectifs
        compteur_objectif=self.ligneHaut+3
        for g in self.oButtons:
            g.grid(row=compteur_objectif,column=15)
            compteur_objectif+=1

        # Emplacement des objectifs
        compteur_emp_obj=self.ligneHaut+3
        for ceo in self.obj_carte:
            ceo.grid(row=compteur_emp_obj,column=14)
            compteur_emp_obj+=1

        # Emplacement ecarter
        self.b_ecarter.grid(row=(self.ligneHaut+1),column=14)
        self.p_ecarter.grid(row=(self.ligneHaut+2),column=14)

        # Emplacement bouton tirage
        self.b_tirage.grid(row=(self.ligneHaut+1),column=15)

        # Assignement des boutons d'écartement de la carte a l'objet bouton ecarter
        self.ecarter_carte.button=self.b_ecarter
        self.ecarter_carte.etiquette=self.p_ecarter

        # Assignement du boutons de tirage de la carte a l'objet bouton tirer
        self.tpA.button=self.boutonA
        self.tpB.button=self.boutonB
        self.tpC.button=self.boutonC
        self.tpD.button=self.boutonD
        self.tpE.button=self.boutonE
        self.tpF.button=self.boutonF
        self.tpG.button=self.boutonG
        self.tpA.etiquette=self.c_A
        self.tpB.etiquette=self.c_B
        self.tpC.etiquette=self.c_C
        self.tpD.etiquette=self.c_D
        self.tpE.etiquette=self.c_E
        self.tpF.etiquette=self.c_F
        self.tpG.etiquette=self.c_G
        self.tpA.etiquette_pile=self.p_A
        self.tpB.etiquette_pile=self.p_B
        self.tpC.etiquette_pile=self.p_C
        self.tpD.etiquette_pile=self.p_D
        self.tpE.etiquette_pile=self.p_E
        self.tpF.etiquette_pile=self.p_F
        self.tpG.etiquette_pile=self.p_G

        # Assignement emplacements d'objectifs
        self.objectif_coeur.button=self.oB_Coeur
        self.objectif_coeur.etiquette=self.emp_Coeur
        self.objectif_pique.button=self.oB_Pique
        self.objectif_pique.etiquette=self.emp_Pique
        self.objectif_trefle.button=self.oB_Trefle
        self.objectif_trefle.etiquette=self.emp_Trefle
        self.objectif_carreau.button=self.oB_Carreau
        self.objectif_carreau.etiquette=self.emp_Carreau

    def retourner_etiquette_carte1(self,carte,cadre):
        return Label(cadre,text="{0}{1}".format(carte.lettre,carte.symbole),fg=carte.couleur,bg="white")
    
    def retourner_etiquette_objectif(self,carte,symbole,cadre):
        if carte is not None:
            return Label(cadre,text="{0}{1}".format(carte.lettre,symbole),fg=carte.couleur,bg="white")
        else:
            symbolecarte=Carte("Vide2",symbole,0,".")
            return Label(cadre, text=u"{0} ".format(symbolecarte.symbole), fg=symbolecarte.couleur, bg="White")

    def placePique(self):
        self.Echange_Objectif(self.objectif_pique)

    def placecCoeur(self):
        self.Echange_Objectif(self.objectif_coeur)

    def placeTrefle(self):
        self.Echange_Objectif(self.objectif_trefle)

    def placeCarreau(self):
        self.Echange_Objectif(self.objectif_carreau)

    def Echange_Objectif(self, obj_symbole):
        if self.obj_temp.etat == Etat_echange.Inactif:
            return False        
        self.obj_temp.arrive = obj_symbole
        if self.obj_temp.valider(cPile.Pile_carte):
            self.obj_temp.echange2(cPile.Pile_carte)
            self.obj_temp.finir_echange()
            self.finir_echange_interface()
            self.Actualisation_interface()

    def etiquette_pile(self, cs):
        cp = Carte("Vide", cs.symbole, 0, ".") if len(cs.cartes) == 0 else cs.cartes[len(cs.cartes)-1]
        if len(cs.cartes) == 0:
            etq_prep = u"{0} ".format(cp.symbole)
        else:
            etq_prep = u"{0}{1} ".format(cp.lettre, cp.symbole)
        cs.label["text"] = etq_prep
        cs.label["fg"] = cp.couleur
        cs.label["bg"] = Couleur.Blanc

    def onClick_tirage(self):
        if self.obj_temp.etat == Etat_echange.Actif:
            return False
        comptePileTirage=len(self.tirage.cartes)
        if comptePileTirage==0:
            self.tirage.cartes=self.ecarter_carte.cartes[::-1]
            self.ecarter_carte.cartes=[]
        if len(self.tirage.cartes)>0:
            self.ecarter_carte.cartes.append(self.tirage.cartes.pop())
        self.Actualisation_interface()

    def onClick_ecarter(self):
        if self.ecarter_carte.button["text"] == "Choisir":
            self.Choisir_ecarter()
        elif self.ecarter_carte.button["text"] == "Annuler":
            self.obj_temp.finir_echange()
            self.finir_echange_interface()

    def choisir_ecarter(self):
        if len(self.ecarter_carte.cartes)==0:
            return False
        self.obj_temp=Echange(self.ecarter_carte)
        self.obj_temp.FaireEchange(1)
        self.Activer_echange(self.b_ecarter)
        self.ecarter_carte["bg"]= "Yellow"

    def changerButtonA(self):
        self.onClick_bouton(self.tpA)
    def changerButtonB(self):
        self.onClick_bouton(self.tpB)
    def changerButtonC(self):
        self.onClick_bouton(self.tpC)
    def changerButtonD(self):
        self.onClick_bouton(self.tpD)
    def changerButtonE(self):
        self.onClick_bouton(self.tpE)
    def changerButtonF(self):
        self.onClick_bouton(self.tpF)
    def changerButtonG(self):
        self.onClick_bouton(self.tpG)
    
    def onClick_Bouton(self,tp_pile):
        if tp_pile.button["text"]=="Select":
            self.bouton_choisir(tp_pile)
        elif tp_pile.button["text"]=="Placer":
            self.bouton_placer(tp_pile)
        else:
            self.obj_temp.finir_echange()
            self.obj_temp.finir_echange_interface()
    
    def bouton_choisir(self,tp_pile):
        if len(tp_pile.cartes) == 0:
            return False

        # Echange de carte
        self.obj_temp = Echange(tp_pile)
        self.obj_temp.FaireEchange(tp_pile.cartesenmvt)

        # Modifie les boutons
        self.Activer_echange(tp_pile.button)
        tp_pile.etiquette["bg"] = "Yellow"
        pass
    
    def bouton_placer(self,tp_pile):
        self.obj_temp.depart=tp_pile
        if self.obj_temp.valider(cPile.Tableau):
            self.obj_temp.echange2(cPile.Tableau)
            self.obj_temp.finir_echange()
            self.finir_echange_interface()
            self.Actualisation_interface()
    
    def changer_bouton(self,B):
        if B["text"]=="Placer":
            B.config(text="Choisir")
        else:
            B.config(text="Placer")
    
    def gui_openTransaction(self, fromButton):
        self.gB_A["text"] = "Annuler" if fromButton is self.gB_A else "Placer"
        self.gB_B["text"] = "Annuler" if fromButton is self.gB_B else "Placer"
        self.gB_C["text"] = "Annuler" if fromButton is self.gB_C else "Placer"
        self.gB_D["text"] = "Annuler" if fromButton is self.gB_D else "Placer"
        self.gB_E["text"] = "Annuler" if fromButton is self.gB_E else "Placer"
        self.gB_F["text"] = "Annuler" if fromButton is self.gB_F else "Placer"
        self.gB_G["text"] = "Annuler" if fromButton is self.gB_G else "Placer"
        self.gB_Discard["text"] = "Annuler" if fromButton is self.gB_Discard else "Choisir"

    def gui_closeTransaction(self):
        self.gB_A["text"] = "Choisir"
        self.gB_B["text"] = "Choisir"
        self.gB_C["text"] = "Choisir"
        self.gB_D["text"] = "Choisir"
        self.gB_E["text"] = "Choisir"
        self.gB_F["text"] = "Choisir"
        self.gB_G["text"] = "Choisir"
        self.gB_Discard["text"] = "Choisir"

    def Actualisation_interface(self):
        if True:
            if len(self.ecarter_carte.cartes)>0:
                self.mvtauto_pile(self.ecarter_carte)
        if True:
            for elt in self.tableau:
                if len(elt.cartes)>0:
                    self.mvtauto_pile(elt)
        carte_renvoyee=self.cartevide if len(self.ecarter_carte.cartes)==0 else self.ecarter_carte.carte_dessus()
        self.ecarter_carte.etiquette["text"]="{0}{1}" .format(carte_renvoyee.lettre,carte_renvoyee.symbole)
        self.ecarter_carte.etiquette["fg"]=carte_renvoyee.couleur
        self.ecarter_carte.etiquette["bg"]="White"

        # Actualisation des piles du tableau
        self.etiquette_pile(self.objectif_pique)
        self.etiquette_pile(self.objectif_trefle)
        self.etiquette_pile(self.objectif_coeur)
        self.etiquette_pile(self.objectif_carreau)

        # Actualisation du tableau
        for elt in self.tableau:
            self.Actualisation_tableau(elt)
        
        self.tirer=Label(self.cadre,text=str(len(self.tirage.cartes))).grid(row=(self.ligneHaut+2),column=15)
    
    def mvtauto_pile(self,cible_pile):
        checkSymbole=cible_pile.carte_dessus().symbole
        cible_pile.button.invoke()

        inf=13
        if self.objectif_coeur.carte_dessus() is not None and self.objectif_coeur.carte_dessus().valeur < inf: inf = self.objectif_coeur.carte_dessus().valeur
        if self.objectif_carreau.carte_dessus() is not None and self.objectif_carreau.carte_dessus().valeur < inf: inf = self.objectif_carreau.carte_dessus().valeur
        if self.objectif_trefle.carte_dessus() is not None and self.objectif_trefle.carte_dessus().valeur < inf: inf = self.objectif_trefle.carte_dessus().valeur
        if self.objectif_pique.carte_dessus() is not None and self.objectif_pique.carte_dessus().valeur < inf: inf = self.objectif_pique.carte_dessus().valeur
        if (self.objectif_coeur.carte_dessus() is None ) or (self.objectif_pique.carte_dessus() is None ) or (self.objectif_trefle.carte_dessus() is None ) or (self.objectif_carreau.carte_dessus() is None ): inf = 0
        
        if checkSymbole==Symbole.Coeur:
            self.obj_temp.arrive=self.objectif_coeur
        if checkSymbole==Symbole.Pique:
            self.obj_temp.arrive=self.objectif_pique
        if checkSymbole==Symbole.Trefle:
            self.obj_temp.arrive=self.objectif_trefle
        if checkSymbole==Symbole.Carreau:
            self.obj_temp.arrive=self.objectif_carreau
        
        if self.obj_temp.valider(cPile.Pile_carte) and self.obj_temp.cartes.valeur <= (inf+2):
            self.obj_temp.arrive.button.invoke()
        if self.obj_temp.statut==Etat_echange.Actif:
            cible_pile.button.invoke()
    
    def Actualisation_tableau(self, aCarte_Pile):
        carte_revelee = [self.Vide] if len(aCarte_Pile.cartes) == 0 else aCarte_Pile.cartes[-aCarte_Pile.cartesenmvt:]

        for pos in range(aCarte_Pile.cartesenmvt):
            aCarte = carte_revelee[pos]
            etq_prep = "{0}{1}".format(aCarte.lettre, aCarte.symbole)
            aCarte_Pile.etiquette[pos]["text"] = etq_prep
            aCarte_Pile.etiquette[pos]["fg"] = aCarte.couleur
            aCarte_Pile.etiquette[pos]["bg"] = Couleur.Blanc

        for pos in range(aCarte_Pile.cartesenmvt,13):
            aCarte = self.Vide
            etq_prep = "{0}{1}".format(aCarte.lettre, aCarte.symbole)
            aCarte_Pile.etiquette[pos]["text"] = etq_prep
            aCarte_Pile.etiquette[pos]["fg"] = aCarte.Couleur
            aCarte_Pile.etiquette[pos]["bg"] = Couleur.White
            
    def Actualisation_tab_etq(self,aCarte_Pile):
        aCarte = self.Vide2 if len(aCarte_Pile.cartes) == 0 else aCarte_Pile.cartes[len(aCarte_Pile.aCarte_Pile)-1]
        etq_prep = "{0}{1}".format(aCarte.lettre, aCarte.symbole)
        aCarte_Pile.etiquette["text"] = etq_prep
        aCarte_Pile.etiquette["fg"] = aCarte.Couleur
        aCarte_Pile.etiquette["bg"] = Couleur.White
    
    def distribuerCarte(self):
        for i in range(len(self.tableau)):
            for j in range(i+1):
                self.remplir_pile(self.tableau[i])
        self.tirage.cartes = self.deck.cartes

    def remplir_pile(self, p):
        p.cartes.append(self.deck.cartes.pop())

    def afficherPile(self, p):
        l = ""
        for i in p.cartes:
            l += "{0}{1}".format(i.lettre, i.symbole)
        return l

    def __str__(self):
        layout = "SOLITAIRE"
        layout += "\n---------\n"
        for i in range(len(self.tableau)):
            layout += self.afficherPile(self.tableau[i])
            layout += "\n"
        return layout


class Pile_de_cartes:
    def __init__(self):
        self.statut = "Rien"
        self.nom = None
        self.cartes=[]
        self.cartesenmvt = 1
        self.bouton = None
        self.etiquette = None

    def arrive_estVide(self):
        return (len(self.arrive)==0)

    def mmsymbole(self):
        return (self.cartes[0].symbole == self.arrive.symbole)

    def carte_dessus(self):
        return None if len(self.cartes) == 0 else self.cartes[-1]
    
    def couleuropp(self):      
        return (self.carte_dessus().couleur != self.arrive.carte_dessus().couleur)
   
    def prochaine_carte_pile(self):
        return (self.cartes[0]==(self.arrive.carte_dessus().valeur+1))

    def prochaine_carte_tableau(self):
        return (self.carte_dessus().valeur == (self.arrive.carte_dessus().valeur - 1))

    def estAs(self):
        return (self.cartes[0].valeur == 1)

    def estRoi(self):
        return (self.carte_dessus().valeur == 13)

class Echange(Pile_de_cartes):
    def __init__(self,depart):
        Pile_de_cartes.__init__(self)
        self.type=cPile.Echange
        self.depart = depart
        self.arrive = None
        self.etat = Etat_echange.Inactif

    def valider(self,cible):
        if cible == cPile.Pile:
            return self.valider_pile()
        else:
            self.valider_tableau()

    def valider_pile(self):
        if self.mmsymbole():
            if self.mmsym():
                return True if self.arrive_estVide() else False
            else:
                return True if self.prochaine_carte_pile() else False
        else:
            return False

    def valider_tableau(self):
        if self.arrive_estVide():
            return True if self.estRoi() else False
        else:
            return True if self.prochaine_carte_tableau() and self.couleuropp() else False

    def FaireEchange(self,c):
        if self.statut==Etat_echange.Inactif and len(self.arrive.cartes)>0:
            self.statut=Etat_echange.Actif
            tempensemble=self.arrive.cartes[::]
            for i in range (c):
                self.cartes.append(tempensemble.pop())

    def echange2(self,st):
        return self.effectuer_a_pile() if st == cPile.Pile else self.effectuer_a_tableau()
    
    def effectuer_a_pile(self):
        self.arrive.cartes.append(self.depart.cartes.pop())
        self.depart.cartesenmvt = self.depart.cartesenmvt - 1

        if self.depart.cartesenmvt<=0:
            self.depart.cartesenmvt = 0

        if len(self.depart.cartes) > 0 and self.depart.cartesenmvt == 0:
            self.depart.cartesenmvt = 1
            
        self.arrive.cartesenmvt = self.arrive.cartesenmvt + 1

    def effectuer_a_tableau(self):
        compte_cartes = len(self.cartes)
        for i in range(compte_cartes):
            self.arrive.cartes.append(self.cartes.pop())
            self.depart.cartes.pop()


        self.depart.cartesenmvt = self.depart.cartesenmvt - compte_cartes

        if self.depart.cartesenmvt < 0:
            self.depart.cartesenmvt = 0

        if len(self.depart.cartes) > 0:
            self.depart.cartesenmvt = 1

        self.arrive.cartesenmvt = self.arrive.cartesenmvt + compte_cartes

        if len(self.arrive.cartes) == 1:
            self.arrive.cartesenmvt = 1

    def finir_echange(self):
        self.statut = Etat_echange.Inactif
        self.cartes = []
        self.arrive=None
        self.depart=None

class OPile(Pile_de_cartes):
    def __init__(self,symbole):
        Pile_de_cartes.__init__(self)
        self.type=cPile.Pile_carte
        self.symbole = symbole

class Pile_renvoi(Pile_de_cartes):
    def __init__(self):
        Pile_de_cartes.__init__(self)
        self.type=cPile.Renvoyer_une_carte

class tirage_pile(Pile_de_cartes):
    def __init__(self):
        Pile_de_cartes.__init__(self)
        self.type=cPile.Tirage

class tableauPile(Pile_de_cartes):
    def __init__(self):
        Pile_de_cartes.__init__(self)
        self.type=cPile.Tableau
        self.etiquette_pile=None

class Deck:
    def __init__(self):
        self.cartes = []
        self.construireDeck()
        self.melange = False
        self.melangerDeck()
    def construireDeck(self):
        cartesNoms=["As","Deux","Trois","Quatre","Cinq","Six","Sept","Huit","Neuf","Dix","Valet","Dame","Roi"]
        carteValeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        carteLettres = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "R"]
        carteSymbole=[Symbole.Coeur,Symbole.Carreau,Symbole.Trefle,Symbole.Pique]
        for i in range(4):
            temp=carteSymbole[i]
            for j in range(13):
                nouvelle_carte = Carte(cartesNoms[j], temp, carteValeurs[j], carteLettres[j])
                self.cartes.append(nouvelle_carte)

    def print_deck(self):
        for cartes in self.cartes:
            print(cartes)

    def melangerDeck(self):
        for i in range(len(self.cartes)):
            position=random.randint(0,len(self.cartes)-1)
            temp=self.cartes[position]
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
    
    def __str__(self):
        return "{0}{1}".format(self.nom, self.symbole)

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
    Rouge="Red"
    Noir="Black"
    Blanc="White"
    Marron="Brown"

class Etat_echange:
    Actif = 1
    Inactif = 0

class cPile:
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
    jouer=Solitaire()
    racine.mainloop()