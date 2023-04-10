alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def haeufigkeitsverteilung(string):
    buchstaben_anzahl = 0
    absolute_haeufigkeiten = []
    relative_haeufigkeit = []
    most_common_letters_in_substring = []
    # absolute haeufigkeit
    for x in alphabet:
        absolute_haeufigkeiten.append((x, string.count(x)))
    # Anzahl Buchstaben im Chiffrattext
    for (x, y) in absolute_haeufigkeiten:
        buchstaben_anzahl += y
    # relative haeufigkeit
    for (x, y) in absolute_haeufigkeiten:
        relative_haeufigkeit.append((x, (y / buchstaben_anzahl) * 100))
    sorted_relative_haeufigkeit = sorted(relative_haeufigkeit, key=lambda z: z[1], reverse=True)
    print(sorted_relative_haeufigkeit[:4])
    # for x in range(4):
    #     print(sorted_relative_haeufigkeit[x])

    # for (x, y) in sorted_relative_haeufigkeit:  # gibt die absteigend sortierte relative haeufigkeitaus
    #     print(x, y)
    # gibt die nach Alphabet sortierte haeufigkeit & relative haeufigkeit aus
    # for ((x, y), (a, b)) in zip(absolute_haeufigkeiten, relative_haeufigkeit1):
    #     print(str(x) + "\t" + str(y) + "\t\t" + str("{:.2f}".format(b)) + '%')


def vigenere(klartext, schluessel, verschluessel_bool):  # verschlüsselt klartext mit schluessel und gibt chiffrat zurück
    klartext = klartext.upper()
    schluessel = schluessel.upper()
    ascii_klartext = []
    ascii_schluessel = []
    ascii_chiffrat = []
    chiffrat = ''
    for letter in klartext:
        ascii_klartext.append(ord(letter))
    for letter in schluessel:
        ascii_schluessel.append(ord(letter) - 65)
    schluesselindex = 0
    if verschluessel_bool == 1:
        for zahl in ascii_klartext:
            ascii_chiffrat_char = zahl + ascii_schluessel[schluesselindex]
            if ascii_chiffrat_char > 90:
                ascii_chiffrat_char -= 26
            ascii_chiffrat.append(ascii_chiffrat_char)
            schluesselindex += 1
            if not schluesselindex < len(schluessel):
                schluesselindex = 0
    else:
        for zahl in ascii_klartext:
            ascii_chiffrat_char = zahl - ascii_schluessel[schluesselindex]
            if ascii_chiffrat_char < 65:
                ascii_chiffrat_char += 26
            ascii_chiffrat.append(ascii_chiffrat_char)
            schluesselindex += 1
            if not schluesselindex < len(schluessel):
                schluesselindex = 0
    for zahl in ascii_chiffrat:
        chiffrat += chr(zahl)
    return chiffrat


def a1():
    with open('C:/Users/LarsN/Documents/HBRS/AngewandteKryptographie/P1/chiffrat1.txt', 'r') as c1:
        chiffrat1 = c1.read()

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    buchstabenAnzahl = 0
    haeufigkeit1 = []
    relhaeufigkeit1 = []

    # absolute haeufigkeit
    for x in alphabet:
        haeufigkeit1.append((x, chiffrat1.count(x)))

    # Anzahl Buchstaben im Chiffrattext
    for (x, y) in haeufigkeit1:
        buchstabenAnzahl = buchstabenAnzahl + y
    # relative haeufigkeit
    for (x, y) in haeufigkeit1:
        relhaeufigkeit1.append((x, (y / buchstabenAnzahl) * 100))
    # sorted Relative Haeufigkeit
    # sortedRelHaeufigkeit1 = sorted(relhaeufigkeit1, key=lambda z: z[1], reverse=True)

    # dechiffrieren
    #   dechiffrat1 = dechiffrat1.replace('', '')
    dechiffrat1 = chiffrat1
    dechiffrat1 = dechiffrat1.replace('C', 'e')
    dechiffrat1 = dechiffrat1.replace('Q', 't')
    # print(dechiffrat1) # -> tLe -> the
    dechiffrat1 = dechiffrat1.replace('L', 'h')
    # print(dechiffrat1) # Pt'K & Pt PK  --> it's & it is
    dechiffrat1 = dechiffrat1.replace('P', 'i')
    dechiffrat1 = dechiffrat1.replace('K', 's')
    # print(dechiffrat1)  # test tB -> to
    dechiffrat1 = dechiffrat1.replace('B', 'o')
    # print(dechiffrat1)  # thSt & S & Ss --> S = a
    dechiffrat1 = dechiffrat1.replace('S', 'a')
    # print(dechiffrat1)  # aGGess = access & Gases = cases | thaE & iE --> E = n
    dechiffrat1 = dechiffrat1.replace('G', 'c')
    dechiffrat1 = dechiffrat1.replace('E', 'n')
    # print(dechiffrat1)
    # Oo Re neeO to Xan encMZDtion? --> do we need to ban encryption? Ooes not XecoYe YoMe --> Does not Become more
    dechiffrat1 = dechiffrat1.replace('O', 'd')
    dechiffrat1 = dechiffrat1.replace('R', 'W')
    dechiffrat1 = dechiffrat1.replace('X', 'b')
    dechiffrat1 = dechiffrat1.replace('M', 'r')
    dechiffrat1 = dechiffrat1.replace('Z', 'y')
    dechiffrat1 = dechiffrat1.replace('D', 'p')
    # print(dechiffrat1)
    # WhiTe, betWeen, secVre, is this a diTeYYa betWeen secVre, priHate -> W = w, V = u, T = l, Y = m, H = v
    dechiffrat1 = dechiffrat1.replace('W', 'w')
    dechiffrat1 = dechiffrat1.replace('V', 'u')
    dechiffrat1 = dechiffrat1.replace('T', 'l')
    dechiffrat1 = dechiffrat1.replace('Y', 'm')
    dechiffrat1 = dechiffrat1.replace('H', 'v')
    # print(dechiffrat1)
    # eFplained = explained, oIten = often, warninA is used liUe = warning is used like, AoinA darU = going dark
    # Justice = justice, Irom = from
    dechiffrat1 = dechiffrat1.replace('A', 'g')
    dechiffrat1 = dechiffrat1.replace('F', 'x')
    dechiffrat1 = dechiffrat1.replace('U', 'k')
    dechiffrat1 = dechiffrat1.replace('J', 'j')
    dechiffrat1 = dechiffrat1.replace('I', 'f')
    # print(dechiffrat1)  # Nimmermann = zimmermann
    dechiffrat1 = dechiffrat1.replace('N', 'z')

    # schlüssel
    deSchlüssel = [('C', 'e'), ('Q', 't'), ('L', 'h'), ('P', 'i'), ('K', 's'), ('B', 'o'), ('S', 'a'), ('G', 'c'),
                   ('E', 'n'), ('O', 'd'), ('R', 'W'), ('X', 'b'), ('M', 'r'), ('Z', 'y'), ('D', 'p'), ('W', 'w'),
                   ('V', 'u'), ('T', 'l'), ('Y', 'm'), ('H', 'v'), ('A', 'g'), ('F', 'x'), ('U', 'k'), ('J', 'j'),
                   ('I', 'f'), ('N', 'z')]  # print
    schluessel = []
    for (x, y) in deSchlüssel:
        schluessel.append((y, x))

    print('a)')
    for ((x, y), (a, b)) in zip(haeufigkeit1, relhaeufigkeit1):
        print(str(x) + "\t" + str(y) + "\t\t" + str("{:.2f}".format(b)) + '%')
    print('b)')
    print(dechiffrat1)
    print('c)')
    print(schluessel)
    print('d)')
    print('"Hanna" - 2023-01-27 | https://tutanota.com/blog/posts/going-dark')


def a2():
    with open('C:/Users/LarsN/Documents/HBRS/AngewandteKryptographie/P1/chiffrat2.txt', 'r') as c2:
        chiffrat_2 = c2.read()
    raw_chiffrat_2 = ''.join(filter(str.isalpha, chiffrat_2))
    # a+b)
    buchstaben_anzahl = 0
    haeufigkeit2 = []
    relhaeufigkeit2 = []
    # absolute haeufigkeit
    for x in alphabet:
        count = 0
        for y in chiffrat_2:
            count = chiffrat_2.count(x)
        haeufigkeit2.append((x, count))
    # Anzahl Buchstaben im Chiffrattext
    for (x, y) in haeufigkeit2:
        buchstaben_anzahl = buchstaben_anzahl + y
    # relative haeufigkeit
    for (x, y) in haeufigkeit2:
        relhaeufigkeit2.append((x, (y / buchstaben_anzahl) * 100))

    # ------------------------------------------------------------
    # sorted Relative Haeufigkeit (ungenutzt)
    # sortedRelHaeufigkeit2 = sorted(relhaeufigkeit2, key=lambda z: z[1], reverse=True)
    # ------------------------------------------------------------

    def koinzidenzindex_rechner(stringlist):
        koinzidenzindex_liste = []
        substring_most_common_letters = []
        # for i in range(len(stringlist)):
        #     haeufigkeitsverteilung(stringlist[i])

        for i in range(len(stringlist)):
            substring_buchstaben_anzahl = len(stringlist[i])
            substring_haeufigkeit = []
            for letter in alphabet:  # absolute haeufigkeit
                substring_haeufigkeit.append((letter, stringlist[i].count(letter)))
            zaehler = 0  # zaehler berechnung
            for (letter, anzahl) in substring_haeufigkeit:
                zaehler += (anzahl * (anzahl - 1))
            nenner = (substring_buchstaben_anzahl * (substring_buchstaben_anzahl - 1))
            koinzidenzindex_liste.append(zaehler / nenner)
            haeufigkeitsverteilung(stringlist[i])
            print('---------------------------')
        return koinzidenzindex_liste

    # koinzidenzindex_rechner string Generator
    def substrings(chiffrat, blocklength):
        substringlist = []
        temp_i = 0
        while blocklength > temp_i:
            substringlist.append(chiffrat[temp_i::blocklength])
            temp_i = temp_i + 1
        return substringlist

    # koinzidenzindex_rechner(substrings(raw_chiffrat_2, 5))  # [:30:]          # NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG
    print(koinzidenzindex_rechner(substrings(raw_chiffrat_2, 10)))  # [:30:]     # NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG

    print(raw_chiffrat_2)

    # vigenere_schluessel_index = [ord('J') - ord('E'), ord('P') - ord('E'), ord('Y') - ord('E'), ord('O') - ord('E'),
    #                              ord('G') - ord('E')]
    # print(vigenere_schluessel_index)
    # vigenere_schluessel = ''
    # for zahl in vigenere_schluessel_index:
    #     vigenere_schluessel += chr(zahl + 65)
    # print(vigenere_schluessel)
    # print(vigenere(raw_chiffrat_2, vigenere_schluessel, 0))

    # print('a)')
    # for ((x, y), (w, z)) in zip(haeufigkeit2, relhaeufigkeit2):
    #     print(str(x) + "\t" + str(y) + "\t\t" + str("{:.2f}".format(z)) + '%')


a2()

# print(vigenere('WhyCryptographyIsHarderThanItLooks', 'ROME', 1))
# print(vigenere('NVKGIMBXFUDEGVKMJVMVUSDXYOZMKZASBG', 'ROME', 0))
#
# print(vigenere('WhyCryptographyIsHarderThanItLooks', 'nnnn', 1))
# print(vigenere('JULPELCGBTENCULVFUNEQREGUNAVGYBBXF', 'nnnn', 1))
# UFWAPWNRMEPYNFWGQFYPBCPRFYLGRJMMIQ
