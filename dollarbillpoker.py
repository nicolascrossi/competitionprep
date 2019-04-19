serials = [
    '14912276',
    '99027737',
    '39217860',
    '59977643',
    '58276501',
    '77437751',
    '03999299',
    '12145671',
    '12340076',
    '98764115',
    '11223344'
]

for i in serials:
    map = {}
    for j in i:
        if j != '0':
            try:
                map[j] = map[j] + 1
            except:
                map[j] = 1
    keys = map.keys()
    highest = 0
    secondHighest = 0
    for k in keys:
        if map[k] >= highest:
            secondHighest = highest
            highest = int(map[k])
    #print(map)
    #print(highest, secondHighest)
    done = False
    if highest >= 5:
        done = True
        print("FIVE OF A KIND")
    elif highest == 4:
        done = True
        print("FOUR OF A KIND")
    elif highest == 3 and secondHighest == 2:
        done = True
        print("FULL HOUSE")
    if not done:
        for j in range(0, 5):
            run = True
            for k in range(1+j, 6+j):
                #print(k, str(k) in keys)
                if not str(k) in keys:
                    run = False
                    break
            if run:
                done = True
                print("STRAIGHT")
                break
    if not done:
        if highest == 3:
            print("THREE OF A KIND")
        elif highest == 2 and secondHighest == 2:
            print("TWO PAIR")
        elif highest == 2:
            print("PAIR")
        else:
            print(max(keys))