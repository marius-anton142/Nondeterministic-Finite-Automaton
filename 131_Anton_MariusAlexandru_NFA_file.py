def bkt(k, stare, cuvant, drum):
    global lista_arce, stare_finala, corect
    drum += str(stare)
    if k == len(cuvant) and stare in stare_finala:
        o.write("DA")
        o.write('\n')
        o.write("Traseu: " + ' '.join(drum))
        o.write('\n')
        corect = 1
    for arc in lista_arce[stare]:
        if arc[1] == cuvant[k]:
            bkt(k+1, arc[0], cuvant, drum)
            
#input
f = open("date.txt")
aux = f.readline().split()
nr_stari = int(aux[0])
nr_arce = int(aux[1])

lista_arce = []
for i in range(nr_stari):
    lista_arce.append([0])
    lista_arce[i].clear()

for i in range(nr_arce):
    aux = f.readline().split()
    x = int(aux[0])
    y = int(aux[1])
    z = aux[2]
    lista_arce[x].append([y,z])
stare_initiala = int(f.readline())
stare_finala = []

aux = f.readline().split()

nr_stare_finala = int(aux[0])
for i in range(nr_stare_finala):
    x = int(aux[i+1])
    stare_finala.append(x)
nr_cuvinte = int(f.readline())
cuvinte = []

for i in range(nr_cuvinte):
    x = f.readline().splitlines()
    cuvinte.append(x)

f.close()

o = open("output.txt", 'w')
for cuvant in cuvinte:
    k = 0
    drum = ""
    corect = 0;
    bkt(0, stare_initiala, cuvant[0], drum)
    if corect == 0:
        o.write("NU")
        o.write('\n')
o.close()
