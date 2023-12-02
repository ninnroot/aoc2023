
def main1():
    x = open("input.txt").readlines()
    calibration_values = []
    for i in x:
        v = []
        for j in i:
            if j.isdigit():
                v.append((j))
        print(v)
        calibration_values.append((v)[0]+(v)[-1])

    return sum([int(i) for i in calibration_values])

def main2():
    x = open("input.txt").readlines()
    spelled_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    calibration_values = []

    for i in x:
        digits = []
        temp = i
        for index, d in enumerate(spelled_digits):
            if i.find(d) != -1:
                y = [(str(index), i.find(d))]
                i=i.replace(d, "",1)
                while i.find(d) != -1:
                    y.append((str(index), i.find(d)))
                    i=i.replace(d, "",1)
                for a in y:
                    digits.append(a)
            i = temp
        for index, j in enumerate(temp):
            if j.isdigit():
                digits.append((j, index))
        digits = [i[0] for i in sorted(digits, key=lambda x: x[-1])]
        if len(digits) == 1:
            digits.append(digits[0])
        calibration_values.append((digits)[0]+(digits)[-1])
    return sum([int(i) for i in calibration_values])


print(main2())
