ceci_est_un_test=1
while ceci_est_un_test:
    try:
         jour=int(input('entrer votre jour de naissance\n'))
         mois=int(input('entrer votre mois de naissance\n'))

         if mois==6:
            if jour>=22:
                print('cancer')
            else:
                print('gemeaux')
         if mois==7:
            if jour>=22:
                print('lion')
            else:
                print('cancer')
         ceci_est_un_test=0

    except:
        print('c\'est mal ecrit')
