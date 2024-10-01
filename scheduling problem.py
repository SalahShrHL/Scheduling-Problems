########################   La liste des taches ##############################################
taches=[{"nom": "t1",
         "pi": 1,
         "ri":0,
         "di":2
        },
        {"nom": "t2",
         "pi": 5,
         "ri":13,
         "di":7
        },
        {"nom": "t3",
         "pi": 3,
         "ri":0,
         "di":8
        },
         {"nom": "t4",
         "pi": 7,
         "ri":0,
         "di":11
        },
         {"nom": "t5",
         "pi": 9,
         "ri":0,
         "di":13
        }
        ]

########################################## CMAX  ########################################################################

def CMAX(list_Taches):
        somme=0
        for t in taches:
            print(t["nom"])            
            somme=somme+t["pi"]
        cmax=somme
        print("\nCMAX = "+str(cmax))

CMAX(taches)
print("#"*50+"\n")

########################################## Cbar  ########################################################################
########       SPT    ##############
def SPT(list_Taches):
        return sorted(list_Taches, key=lambda i: i['pi'])
#######       Cbar   ###############
def Cbar(list_Taches):
        listeSPT=SPT(list_Taches)
        for c in listeSPT:
            print(c["nom"])
            
        somme_ci=0
        for c in listeSPT:
            somme_ci=somme_ci+c["pi"] 
            cbar=somme_ci/len(listeSPT)
        print("\nCbar = "+str(cbar))

Cbar(taches)
print("#"*50+"\n")
########################################## LMAX + TMAX (Régle EDD) ######################################################

########       EDD    ##############
def EDD(list_Taches):
        return sorted(list_Taches, key=lambda i: i['di'])




######       LMAX     ##################
def LMAX(list_Taches):
        listeEDD=EDD(list_Taches)
        for d in listeEDD:
            print(d["nom"])

        ci=listeEDD[0]["pi"]
        liste_li=[]
        for d in listeEDD:
            liste_li.append(ci-d["di"])
            ci=ci+d["di"] 
            
        
        lmax=max(liste_li)
        print("\nLMAX = "+str(lmax))
        

LMAX(taches)
print("#"*50+"\n")

 

#######     TMAX      ###################
def TMAX(list_Taches):
        listeEDD=EDD(list_Taches)
        for d in listeEDD:
            print(d["nom"])
        ci=listeEDD[0]["pi"]
        liste_ti=[]
        for d in listeEDD:
            liste_ti.append(max([ci-d["di"] , 0]))
            ci=ci+d["di"] 
            
        
        tmax=max(liste_ti)
        print("\nTMAX = "+str(tmax))

TMAX(taches)
print("#"*50+"\n")


###############################################################################################################

################################ U(bar) #######################################################################

def Ubar(list_Taches):
        esemble_ordonee=[]
        taches_éliminé=[]
        t=0

        listeEDD=EDD(list_Taches)
        for d in listeEDD:
            esemble_ordonee.append(d)
            t=t+d["pi"]
            if t>d["di"]:
                x=max(esemble_ordonee, key=lambda i: i['pi'])
                t=t-x["pi"]
                taches_éliminé.append(x)
                esemble_ordonee.remove(x)
        total=esemble_ordonee+taches_éliminé
        
        for tache in total:
            print(tache["nom"])

        liste_ui=[]
        ci=total[0]["pi"]
        for t in total:
            if ci>t["di"]:
                liste_ui.append(1)
            else:
                liste_ui.append(0)
            
            ci=ci+d["di"]

        somme=0
        for u in liste_ui:
            somme=somme+u
            Ubar=somme/len(liste_ui)
        
        print("\nUbar = "+str(Ubar))

Ubar(taches) 
print("#"*50+"\n")    

        
            


