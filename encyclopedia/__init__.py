def decode(lista):
    types = []
    for komad in (lista):
        jedan = []
        komad.split (" ")
        if komad == "":
            jedan.append(7)
        else:
            brojljestva = 0 
            for j in komad:
                if j == "#":
                    brojljestva += 1
                else:
                    break
            jedan.append(brojljestva)
        if jedan[0] == 0:
            Bold = []
            rijec = []
            word = komad[jedan[0]:].split("**")
            for v in range (len(word)):
                Bold2 = []
                Bold2.append (word[v])
                if v % 2 == 1:
                    Bold2.append("B")
                else:
                    Bold2.append("")
                Bold.append (rijec)
            jedan.append (Bold)

        else:
            jedan.append (komad[jedan[0]:])
        types.append(jedan)
    return types
