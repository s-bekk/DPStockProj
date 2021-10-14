R1 = 0 #(kohms)            
Re = 0
R2 = 0
# count = 0
x = 100
y = 1000
for R1 in range(x, y):
    for R2 in range(x, y):
        for Re in range(x, y):
            # count += 1
            # print(count)
            Top = ((10*R2)/(R1+R2)) + 4.3
            Bottom = ((R1*R2)/(120*(R1+R2)))*(10 ^ 3) + ((121/120)*Re)*(10 ^ 3)
            ICQ = Top/Bottom
            if ICQ >= 160:
                print("ICQ: ", ICQ)
                print("Resistor Values:")
                print("R1: ", R1)
                print("R2: ", R2)
                print("Re: ", Re)

