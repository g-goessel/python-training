# fichier de fonctions
#chaneg transforme chaque values en type
def change(type='int',*values):
    for i in values:
        #pour chaque valeur de 'values' on essaie de le convertir en "type"
        try:
            if type=='int':
                i=int(i)
            elif type=='str':
                i=str(i)
            elif type=='float':
                i=float(i)
            return i
        except:
            pass
