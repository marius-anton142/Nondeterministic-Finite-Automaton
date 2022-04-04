def bkt(k, stare, cuvant, drum):
    global lista_arce, stare_finala, corect
    drum += str(stare)
    if k == len(cuvant) and stare in stare_finala:
        print("DA")
        print("Traseu: " + ' '.join(drum))
        corect = 1
    for arc in lista_arce[stare]:
        if arc[1] == cuvant[k]:
            bkt(k+1, arc[0], cuvant, drum)
            
#input
nr_stari = int(input("nr stari = "))
nr_arce = int(input("nr arce = "))
lista_arce = []
for i in range(nr_stari):
    lista_arce.append([0])
    lista_arce[i].clear()
print("lista arce = ")
for i in range(nr_arce):
    x = int(input())
    y = int(input())
    z = input()
    lista_arce[x].append([y,z])
stare_initiala = int(input("stare initiala = "))
stare_finala = []
nr_stare_finala = int(input("nr stari finale = "))
print("stari finale = ")
for i in range(nr_stare_finala):
    x = int(input())
    stare_finala.append(x)
nr_cuvinte = int(input("nr cuvinte = "))
cuvinte = []
print("lista cuvinte =")
for i in range(nr_cuvinte):
    x = input()
    cuvinte.append(x)

for cuvant in cuvinte:
    k = 0
    drum = ""
    corect = 0;
    bkt(0, stare_initiala, cuvant, drum)
    if corect == 0:
        print("NU")
