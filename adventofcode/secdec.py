def rock_paper_scissor():

    with open("ressource/secdecinput.txt") as f:
        content = f.read()
        value = content.split("\n")
        erg = 0
        for x in value:
            if x == "A X":
                erg += 3
            elif x == "A Y":
                 erg += 4
            elif x == "A Z":
                erg += 8
            elif x == "B X":
                erg += 1
            elif x == "B Y":
                erg += 5
            elif x == "B Z":
                erg += 9
            elif x == "C X":
                erg += 2
            elif x == "C Y":
                erg += 6
            elif x == "C Z":
                erg += 7

        print(erg)




if __name__ == '__main__':
    rock_paper_scissor()