N = 500
K = 1
group = []

for i in range(1, N+1):
    group.append(i)


def remove(lista):

    osoitin = K - 1

    while len(lista) > 1:

        lista.pop(osoitin)
        osoitin += K - 1
        if osoitin > len(lista):
            osoitin = osoitin - len(lista)

        if osoitin == len(lista):
            osoitin = 0


    return lista


group = remove(group)

print(group)
