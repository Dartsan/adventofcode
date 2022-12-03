from string import ascii_lowercase
from string import ascii_uppercase


def getprio1() -> int:
    with open("ressource/thirddec.txt") as f:
        content = f.read()
        a = content.split("\n")

        sum = 0
        for x in a:
            teil1 = x[:len(x) // 2]
            teil2 = x[len(x) // 2:]
            for c in teil1:
                if c in teil2:
                    sum += getsum(c)
                    # print(f"Der gemeinsame Buchstabe lautet: {c} und die derzeitige Summe: {sum}")

                    break

        return sum


def getprio2() -> int:
    with open(
            "/Users/olivertanzer/Library/CloudStorage/OneDrive-Personal/Uni/1.Semester/Software Design/Python "
            "Projecte/pythonProject/adventofcode/ressource/thirddec.txt") as f:
        content = f.read()
        a = content.split("\n")

        first = list()
        sec = list()
        third = list()

        sum = 0
        for i in range(0, len(a), 3):
            first.append(a[i])

        for i in range(1, len(a), 3):
            sec.append(a[i])

        for i in range(2, len(a), 3):
            third.append(a[i])

        for i in range(len(first)):
            for c in first[i]:
                if c in sec[i] and c in third[i]:
                    #  print(f"Der gemeinsame buchstabe von allen drei lautet: {c}")
                    sum += getsum(c)
                    break

        return sum


def getsum(letter: str) -> int:
    sum = 0
    if letter in ascii_lowercase:
        sum = 0
        for c in ascii_lowercase:
            sum += 1
            if c == letter:
                break
    elif letter in ascii_uppercase:
        sum = 26
        for c in ascii_uppercase:
            sum += 1
            if c == letter:
                break
    return sum


if __name__ == '__main__':
    print(getprio1())
    print(getprio2())
