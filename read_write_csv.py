#coding:utf-8 

#############
"""
lecture et organisation des fichier .x
03/11/2022
derniere modif : 03/11/2022
crea : bettaH

lien utile de tkinter
http://pascal.ortiz.free.fr/contents/tkinter/tkinter/index.html
"""
#############

import csv
import os

#path_Carte = os.path.join(os.path.dirname(os.getcwd()), "japan_carte")

#print(os.path.abspath(__file__))
path = os.getcwd()
path_Carte = os.path.join(path,"Carte")


print(path_Carte)


liste_info = []
Liste_num = []
Liste_nom_Fr = []
Liste_nom_Jap = []
Liste_annee = []
Liste_mois = []
Liste_jour = []
Liste_heure = []
Liste_minute = []
Liste_frequence = []
Liste_freq_grand_erreur = []

with open(os.path.join(path_Carte,"Liste_Carte.csv")) as test:
    Liste_carte = csv.reader(test, delimiter=',', quotechar='|')

    for row in Liste_carte:
        #print(', '.join(row))
        liste_info.append(row)
        #print(row)
        
    
print("yo\n")
print(liste_info)
print(liste_info[19][2])

len_file = len(liste_info)
#print(len(liste_info))

for i in range(len_file):
    #print(liste_info[i][2])
    Liste_nom_Fr.append(liste_info[i][2])
    Liste_nom_Jap.append(liste_info[i][3])
    Liste_annee.append(liste_info[i][4])
    Liste_mois.append(liste_info[i][5])
    Liste_jour.append(liste_info[i][6])
    Liste_heure.append(liste_info[i][7])
    Liste_minute.append(liste_info[i][8])
    Liste_frequence.append(liste_info[i][9])
    Liste_freq_grand_erreur.append(liste_info[i][10])
    Liste_num.append(liste_info[i][1])

#print(Liste_nom_Fr)
#print(Liste_nom_Jap)


## etude du numero de carte

print(Liste_num)
print(len_file)
print(Liste_num[len_file-1])

write_new_num = str(len_file-1)

print(write_new_num)

print(type(Liste_num[len_file-1]))
print(type(write_new_num))


"""

test = []

test = '0' ,write_new_num , 'test'

liste_info.append(test)


### permet une ecriture total du fichier qui à ete modifier

with open(os.path.join(path_Carte,"Liste_Carte.csv"), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(liste_info)

"""