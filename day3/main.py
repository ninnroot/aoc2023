
import re

special_chars = r"!@#$%^&*()_+=/-"
def main():
    x = open("input.txt").readlines()
    coors = []
    for y_pos, i in enumerate(x):
        temp = ""
        for x_pos, j in enumerate(i):
            if j.isdigit():
                temp+=j
            else:
                if temp:
                    coors.append({
                        "start": (x_pos-len(temp), y_pos),
                        "end": (x_pos-1, y_pos),
                        "number": temp
                    })
                temp=""

    for y_pos, i in enumerate(x):
        temp = ""
        for x_pos, j in enumerate(i):
            if j in special_chars:
                temp += j
            else:
                if temp:
                    coors.append({
                        "start": (x_pos - len(temp), y_pos ),
                        "end": (x_pos - 1, y_pos),
                        "char": temp
                    })
                temp = ""
    engine_parts = []
    for i in coors:
        if "char" in i.keys() and i["char"] == "*":
            touchings = []
            for j in coors:
                if "number" in j.keys():
                    if is_touching(j["start"], j["end"], i["start"]):
                        touchings.append(j["number"])
            if len(touchings) == 2:
                engine_parts.append(int(touchings[0])*int(touchings[1]))

    print(sum([int(i) for i in engine_parts]))

def get_surroundings(x, y):
    return [
        (x-1, y),
        (x-1, y-1),
        (x-1, y+1),
        (x+1, y),
        (x+1, y-1),
        (x+1, y+1),
        (x, y+1),
        (x, y-1),
    ]

def is_touching(start, end, self):
    surroundings = get_surroundings(self[0], self[1])
    touching = False
    if start in surroundings or end in surroundings:
        touching = True
        return touching
    body = []
    for i in range(start[0], end[0]):
        body.append((i, start[1]))
    for i in surroundings:
        if i in body:
            touching = True
            return touching
    return touching



main()

