# -*- coding: utf-8 -*-

date = input('entre ta date de naissance (jj/mm)\n')
while 1:
    try:
        date = date.split("/")
        #Si la conversion à échouée date est toujours une string
        if isinstance(date, str):
            raise
        jj = int(date[0])
        mm = int(date[1])
        break
    except:
        print('try again')
        date = input('entre ta date de naissance\n')
print('jour :', jj, ' \n mois :', mm)
