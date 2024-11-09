import random

s = "AMİRAL BATTI OYUNU"
s = s.center(150, "-")
print(s)

while True:
    print("     Oyuna başlamak veya devam etmek için ===> 1",
          "     Oyundan çıkmak için                  ===> 2", sep="\n")
    action = int(input("İşlem seçiniz: "))
    match action:
        case 1:
            while True:
                dimension = int(input("Oyun alanı için kare matris boyutu giriniz: "))
                if dimension >= 10:
                    break

            while True:
                startPoints = {1: (), 2: (), 3: (), 4: ()}
                allStartPoints = []
                for key in startPoints:
                    y = random.randint(0, dimension - 1)
                    x = random.randint(0, dimension - 1)
                    point = (y, x)
                    if point in allStartPoints:
                        break
                    allStartPoints.append(point)
                    startPoints[key] = point

                local = random.randint(1, 2)
                path = [-1, 1]

                shipsPoint = {1:[()],2:[(),()],3:[(),(),()],4:[(),(),(),()]}

                key = 1
                allShipPoints = []
                control = 1
                while key < 5:
                    if control == 0:
                        break
                    y = startPoints[key][0]
                    x = startPoints[key][1]
                    point = (y, x)
                    ship = shipsPoint[key]
                    move = path[random.randint(0, 1)]
                    if local == 1:
                        for i in range(len(ship)):
                            ship[i] = point
                            allShipPoints.append(ship[i])
                            y += move
                            point = (y,x)
                            if point[0] < 0 or point[0] >= dimension - 1:
                                control = 0
                                break
                            if point in allShipPoints:
                                control = 0
                                break
                        local += 1
                    elif local == 2:
                        for i in range(len(ship)):
                            ship[i] = point
                            allShipPoints.append(ship[i])
                            x += move
                            point = (y,x)
                            if point[1] < 0 or point[1] >= dimension - 1:
                                control = 0
                                break
                            if point in allShipPoints:
                                control = 0
                                break
                        local -= 1
                    key += 1
                if control == 1:
                    break

            matrix = []
            for i in range(dimension):
                y = []
                for j in range(dimension):
                    y.append("?")
                matrix.append(y)

            print("     Gizli modda oynamak için ===> 1",
                  "     Açık modda oynamak için  ===> 2",sep="\n")
            choose = int(input("Oyun modu seçimi: "))
            match choose:
                case 1:
                    userRight = (dimension**2)//3
                    userShotPoint = {1: [], 2: [], 3: [], 4: []}
                    allUserPointList = []
                    while True:
                        print("  ".center(58, " "), end="")
                        for i in range(dimension):
                            print("{:2}".format(i), end=" ")
                        print()
                        for i in range(dimension):
                            print(" ".center(55, " "), end=" ")
                            print("{:2}".format(i), end=" ")
                            for j in range(dimension):
                                print("{:2}".format(matrix[i][j]), end=" ")
                            print()
                        print("Atış Hakkı: {}".format(userRight))
                        print(userShotPoint)
                        numberUserPoint = int(input("Tahmin edeceğiniz nokta sayısı giriniz: "))
                        userPointList = []
                        n = 0
                        while n < numberUserPoint:
                            y = int(input("{}. Sütün koordinatı: ".format(n + 1)))
                            x = int(input("{}. Satır koordinatı: ".format(n + 1)))
                            point = (y, x)
                            if point in userPointList:
                                print("".center(40, " "), end="")
                                print("Girdiğiniz noktalardan aynısını girmeye denemeyiniz lütfen tekrar deneyiniz...")
                                continue
                            allUserPointList.append(point)
                            userPointList.append(point)
                            n += 1
                        print()
                        for element in userPointList:
                            if element not in allShipPoints:
                                print("".center(40," "),end="")
                                print("Maalesef {} noktası gemilerin herhangi bir noktasına isabet etmiyor.".format(element))
                                y = element[0]
                                x = element[1]
                                matrix[y][x] = "*"
                            else:
                                for key in shipsPoint:
                                    if userShotPoint[key] == shipsPoint[key]:
                                        print("Tebrikler {}. filodaki bütün gemileri batırdınız!!! :)".format(key))
                                    if element in shipsPoint[key]:
                                        userShotPoint[key].append(element)
                                        userShotPoint[key].sort()
                                        y = element[0]
                                        x = element[1]
                                        matrix[y][x] = "x"
                                        print("".center(40, " "), end="")
                                        print("Tebrikler!!! {} noktası ile filodaki {}. geminin {}. noktasını vurdunuz."
                                                .format(element, key, shipsPoint[key].index(element)+1))
                                        if userShotPoint[key] == shipsPoint[key]:
                                            print("".center(40, " "), end="")
                                            print("Tebrikler {}. filodaki bütün gemileri batırdınız!!! :)".format(key))
                            userRight -= 1
                        if userRight == 0:
                            print("".center(40, " "), end="")
                            print("Üzgünüz tüm haklarınızı kullandığınız için oyununuz sonlandı... :(")
                            exit()
                        elif userShotPoint == shipsPoint:
                            print("".center(40, " "), end="")
                            print("Tebrikler girdiğiniz doğru koordinarlarla filodaki bütün gemileri batırmayı başardınız!!! :(")
                            userPoint = userRight
                            print("".center(40, " "), end="")
                            print("Amiral Battı oyunda puanınız: {}".format(userPoint))
                            break
                        print()
                case 2:
                    userRight = (dimension ** 2) // 3
                    userShotPoint = {1: [],2: [],3: [],4: []}
                    allUserPointList = []
                    for key in shipsPoint:
                        for Point in shipsPoint[key]:
                            matrix[Point[0]][Point[1]] = str(key)
                    while True:
                        print("  ".center(58, " "), end="")
                        for i in range(dimension):
                            print("{:2}".format(i), end=" ")
                        print()
                        for i in range(dimension):
                            print(" ".center(55, " "), end=" ")
                            print("{:2}".format(i), end=" ")
                            for j in range(dimension):
                                print("{:2}".format(matrix[i][j]), end=" ")
                            print()
                        print("Atış Hakkı: {}".format(userRight))
                        print(userShotPoint)
                        numberUserPoint = int(input("Tahmin edeceğiniz nokta sayısı giriniz: "))
                        userPointList = []
                        n = 0
                        while n < numberUserPoint:
                            y = int(input("{}. Sütün koordinatı: ".format(n + 1)))
                            x = int(input("{}. Satır koordinatı: ".format(n + 1)))
                            point = (y, x)
                            if point in userPointList:
                                print("".center(40, " "), end="")
                                print("Girdiğiniz noktalardan aynısını girmeye denemeyiniz lütfen tekrar deneyiniz...")
                                continue
                            allUserPointList.append(point)
                            userPointList.append(point)
                            n += 1
                        print()
                        for element in userPointList:
                            if element not in allShipPoints:
                                print("".center(40," "),end="")
                                print("Maalesef {} noktası gemilerin herhangi bir noktasına isabet etmiyor.".format(element))
                                y = element[0]
                                x = element[1]
                                matrix[y][x] = "*"
                            else:
                                for key in shipsPoint:
                                    if element in shipsPoint[key]:
                                        userShotPoint[key].append(element)
                                        userShotPoint[key].sort()
                                        y = element[0]
                                        x = element[1]
                                        matrix[y][x] = "x"
                                        print("".center(40, " "), end="")
                                        print("Tebrikler!!! {} noktası ile filodaki {}. geminin {}. noktasını vurdunuz."
                                                .format(element, key, shipsPoint[key].index(element)+1))
                                        if userShotPoint[key] == shipsPoint[key]:
                                            print("".center(40, " "), end="")
                                            print("Tebrikler {}. filodaki bütün gemileri batırdınız!!! :)".format(key))
                            userRight -= 1
                        if userRight == 0:
                            print("".center(40, " "), end="")
                            print("Üzgünüz tüm haklarınızı kullandığınız için oyununuz sonlandı... :(")
                            exit()
                        elif userShotPoint == shipsPoint:
                            print("".center(40, " "), end="")
                            print("Tebrikler girdiğiniz doğru koordinarlarla filodaki bütün gemileri batırmayı başardınız!!! :(")
                            userPoint = userRight
                            print("".center(40, " "), end="")
                            print("Amiral Battı oyunda puanınız: {}".format(userPoint))
                            break
                        print()
        case 2:
            exit()