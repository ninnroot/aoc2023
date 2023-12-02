

def main():
    x = open("input.txt").readlines()
    red_max = 12
    green_max = 13
    blue_max = 14
    game_ids = []
    dic = {

    }
    for i in x:
        temp = {}
        for index, j in enumerate(i.split(":")[1].split(";")):
            temp[index] = []
            for k in j.split(","):
                temp[index].append({k.split(" ")[2].strip(): int(k.split(" ")[1])})

        dic[int(i.split(":")[0].split(" ")[1])] = temp

    for i in dic.keys():
        r = 0
        g = 0
        b = 0
        for j in dic[i].keys():
            for k in (dic[i][j]):
                if list(k.keys())[0] == "red" and list(k.values())[0] > r:
                    r = list(k.values())[0]
                if list(k.keys())[0] == "green" and list(k.values())[0] > g:
                    g = list(k.values())[0]

                if list(k.keys())[0] == "blue" and list(k.values())[0] > b:
                    b = list(k.values())[0]
        game_ids.append(r*g*b)

    print(game_ids)
    return sum(game_ids)

print(main())

