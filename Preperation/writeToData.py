from random import randint as r


def write():
    bloodTypes = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    w = open("data.txt", "w")
    for i in range(1000):
        w.write(bloodTypes[r(0, len(bloodTypes) - 1)] + "\n")
    w.close()


def readAndCount():
    r = open("data.txt", "r")
    dict = {"A+": 0, "A-": 0, "B+": 0, "B-": 0,
            "AB+": 0, "AB-": 0, "O+": 0, "O-": 0}
    for line in r:
        line = line.strip()
        if(line in dict):
            dict[line] += 1
    print(dict)

# write()
readAndCount()