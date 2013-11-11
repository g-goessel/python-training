def vraifaux(lettre):
  mot="table"
  if lettre in mot :
      return 1
  else :
      return 0
a=("lettre")
#K est le nombre d'erreures#
lettrestrouvees=[]
k=0
t=0
while k<=10 :
    a=input("entrer une lettre")
    if vraifaux(a):
        if a in lettrestrouvees:
            pass
        else :
           lettrestrouvees.append(a)
           t+=1
           if t==5 :
               print("Gagné")
               break
    else :
        k+=1
if k==11 :
 print("Perdu")
