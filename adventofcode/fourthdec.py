def getranges1():
    with open("fourthdec.txt") as f:
        content = f.read()
        a = content.split("\n")
        counter = 0
        for x in a:
            a, b = x.split(",")
            min1, max1 = a.split("-")
            min2, max2 = b.split("-")

            if int(min1) >= int(min2) and int(max1) <= int(max2):
                counter += 1
            elif int(min1) <= int(min2) and int(max1) >= int(max2):
                counter += 1

        print(counter)


def getranges2():
    with open("fourthdec.txt") as f:
        content = f.read()
        a = content.split("\n")
        counter = 0
        for x in a:
            a, b = x.split(",")
            min1, max1 = a.split("-")
            min2, max2 = b.split("-")

            val1 = int(min1)
            val2 = int(max1)
            val3 = int(min2)
            val4 = int(max2)

            for i in range(val1, (val2+1)):
                if i in range(val3, (val4+1)):
                    counter += 1
                    break

        print(counter)

if __name__ == '__main__':
    getranges1()
    getranges2()
