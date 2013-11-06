mot='table'
a=input('entrer une lettre ')
l_mot=list(mot)
print(l_mot)
if a in l_mot:
    b=input('entrer une autre lettre ')
else:
    compteur=10
    while compteur<=10 :
    print('reponse fausse ')
    b=input('entrer une autre reponse ' )
    

