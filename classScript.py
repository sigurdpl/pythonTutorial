import classTest

zombie1 = classTest.Zombie('pete')
zombie1.walk('left')
zombie1.walk('right')
zombie2 = classTest.Zombie('badMike')
zombie2.walk('up')

zombieList = [zombie1, zombie2]
for zombie in zombieList:
    zombie.walk('left')
    print(zombie.name)

