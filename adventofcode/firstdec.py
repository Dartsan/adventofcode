def firstexample():
    with open("ressource/firstdecinput.txt") as f:
        content = f.read()
        a = content.split("\n")

        teilerg = 0
        ergebnisliste = list()
        for i in a:
            if i.isnumeric():
                teilerg += int(i)

            else:
                ergebnisliste.append(teilerg)
                teilerg = 0

        ergebnisliste.append(teilerg)
        ergebnisliste.sort(reverse=True)
        summe = ergebnisliste[0] + ergebnisliste[1] + ergebnisliste[2]
        print(summe)

if __name__ == '__main__':
    print("Das ist die Aufgabe für den 1. Dezember")
    print("*******************Teil1*****************")
    firstexample()