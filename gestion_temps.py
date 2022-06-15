

"""
gestion du temps 



"""

import time




print(time.ctime())  #temps actuelle
print(time.ctime(0)) #temps début
print(time.ctime(1556689999)) #temps choisit par nbr


print(time.time()) #temps passer depuis le temps debut en seconde 

print(time.localtime())
a = time.localtime()
print(a.tm_hour)
print(type(a.tm_mon))

# creation format de date 
"""
%d : jour
%m : mois
%Y : année
%y : année
%H : heure
%I : minute
%S : seconde
%p : AM/PM
%A : jour semaine
%a
%B : nom mois
%b

%Z : fuseau horaire
"""


my_time = time.strftime("%m,%H")
print(my_time)