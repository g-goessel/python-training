date = input('entre ta date de naissance (jj/mm) \n')
while 1:
    try:
        date = date.split('/')
        if isinstance(date, str):
            raise
        jj = int(date[0])
        mm = int(date[1])
        break
    except:
        print('try again')
        date = input('entre ta date de naissance (jj/mm) \n')

print('jour :', jj, '\nmois :', mm)
