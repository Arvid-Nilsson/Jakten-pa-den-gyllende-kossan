import rooms as r

Room = 0

while True:
    if Room == 0:
        Room = r.Room0()
    elif Room == 1:
        Room = r.Room1()
    elif Room == 2:
        Room =r.Room2()
    elif Room == 3:
        Room = r.Room3()