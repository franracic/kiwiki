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
            if brojljestva == 0:
                if komad[0] == "-":
                    brojljestva = 8

            jedan.append(brojljestva)
        if jedan[0] == 0:
            Bold = []
            word = komad[jedan[0]:].split("**")
            for v in range (len(word)):
                if v % 2 == 1:
                    B = ("B")
                else:
                    B = ("")

                Bold3 = word[v].split("*")
                for k in range (len(Bold3)):
                    if k % 2 == 1:
                        I = ("I")
                    else:
                        I = ("")
                    Bold5 = Bold3[k].split("[")
                    for f in range (len(Bold5)):
                        if f>0:
                            PL = ("PL")
                        else:
                            PL = ("")
                        Bold4 = Bold5[f].split("](")
                        for f2 in range (len(Bold4)):
                            Bold2 = []
                            if f2 % 2 == 1:
                                L = ("L")
                                LL = ""
                                Bold2.append (Bold4[f2][:Bold4[f2].index(")"):])
                            else:
                                if PL == "PL":
                                    LL = Bold4[f2+1][:Bold4[f2+1].index(")")]
                                else:
                                    LL = ""
                                L = ("")
                                Bold2.append (Bold4[f2])
                            
                            Bold2.append (B)
                            Bold2.append (I)
                            Bold2.append (L)
                            Bold2.append (PL)
                            Bold2.append (LL)
                            Bold.append (Bold2)
            jedan.append (Bold)

        else:
            if brojljestva == 8:
                jedan.append (komad[1:])
            else:
                jedan.append (komad[jedan[0]:])
        types.append(jedan)
    return types
