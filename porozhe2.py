mokhatabin = []

while True :
    
    shomare = input("shomare mokhatab:  ")
    
    nam =   input("nam mokhatab: ")
    
    mokhatab = { 
        "nam" : nam,
        "shomare" : shomare
    }
    
    mokhatabin.append(mokhatab)

    javab = input("mokhatab jadid mikhayn ?:   (Y/N)")

    if javab == "N":
         break

print(mokhatabin)



