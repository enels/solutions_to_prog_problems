def dot_product(lista, listb, n):
    # making sure the right number of element is passed as arg
    assert n == len(lista)
    assert n == len(listb)

    # empty list ot store the dot product
    listc = list()
    for index in range(n):
        # get the dot product
        listc.append(lista[index] * listb[index])

    return listc