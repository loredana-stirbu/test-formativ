from datetime import datetime
from math import prod
total=7
produs1=('Paine','29/03/2021','10/04/2022',10)
produs2=('Maioneza','02/11/2022','02/12/2022',25)
produs3=('Salam','15/06/2022','15/09/2023',80)
produs4=('Ciocolata', '29/10/2022', '28/11/2022', 28)
produs5=('Lapte', '31/10/2022', '04/11/2022', 16)
produs6=('Branza', '27/10/2022' , '02/11/2022' , 12)
produs7=('Iaurt','29/10/2022', '03/10/2022',8)
lista_de_produse=[produs1,produs2,produs3,produs4,produs5,produs6,produs7]
today=datetime.today()
expirate=[]
red_50=[]
red_20=[]
valabil_un_an=[]
valabil_o_luna =[]

print('\n')
print("Data curenta:", today,'\n')
for produs in lista_de_produse:
    data_fabr=datetime.strptime(produs[1],'%d/%m/%Y')
    data_exp=datetime.strptime(produs[2],'%d/%m/%Y')
    zile_totale=(data_exp-data_fabr).days
    pana_la_expirare=(data_exp-today).days
    if(zile_totale>=365):
        valabil_un_an.append(produs[0])
    elif(zile_totale<=30):
        valabil_o_luna.append(produs[0])
    termen_25=0.25*zile_totale
    produs=list(produs)
    if(pana_la_expirare<0):
        produs.append(0)
        expirate.append(produs[0])
    elif(pana_la_expirare<=termen_25):
        produs.append(produs[3]-(produs[3]*0.5))
        red_50.append(produs[0])
    elif(pana_la_expirare<=zile_totale/2):
        produs.append(produs[3]-(produs[3]*0.2))
        red_20.append(produs[0])

print("In total sunt",total,"produse.")
print("Produse expirate:",expirate)
print("Produse reducere pret 50%:",red_50)
print("Produse reducere pret 20%:",red_20)
print("Produse valabile cel putin un an",valabil_un_an)
print("Produsee valabile cel mult o luna",valabil_o_luna)
