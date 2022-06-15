

Developpement organisation de rangament des fichiers


2 dossier : 
    - IHM
        -
        - fichier tampon qui contient des images selectionner avec toutes leurs informations
    - memory
        - x dossiers (classer par groupe de mot)
            - fichier classé qui contiennent la date et la frequence de reussite
            - image contenue du fichier classé
        

organisation fichier classé :

(possiblité de rajout de colonne avec nom image lang)

  num_ligne | nom img fr | nom img lang |    année    |  mois   |  jour   |  heure  | minute  |   freq  |freq grande erreur||
  0 à inf   |	nom	     | nom img lang | 9999 à 0000 | 12 à 01 | 31 à 01 | 23 à 00 | 59 à 01 | 99 à 00 |       0 à 9      ||
      10    |   chien    |     Inu      |    2022     |   06    |    14   |    23   |    22   |     5   |       2          || # exemple

organisation fichier tampon :

(possiblité de rajout de colonne avec nom image lang)

    num_ligne    |	nom	img lang  |	nom	img lang  |   heure    |  minute | frequence | freq grande erreur |  nb_réussit |  nb_échec  |
      0 à inf    |	    nom	      |	nom	img lang  |   23 à 00  | 59 à 01 |  99 à 00  |       0 à 9        |    0 à 9    |    0 à 9   |
        10       |	    Inu	      |	nom	img lang  |     23     |    48   |     5     |         0          |       0     |      0     | # exemple



dev du systeme de frequence :

    - valeur de freq est comprise entre 0 à 99
        
    Algo de freq :
        -  0 = jamais fait 
        -  1 = 1 jour   +1
        -  2 = 2 jour   +1
        -  3 = 3 j      +1
        -  4 = 5 j      +2
        -  5 = 7 j      +2
        -  6 = 9 j      +2
        -  7 = 15 j     +6
        -  8 = 21 j     +6
        -  9 = 27 j     +6

    On en déduit une récurence :

    3 ligne X*1.4
    