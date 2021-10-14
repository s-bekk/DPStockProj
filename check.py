Rc = 0
Re = 0
Vcc = 20
Rl = 50
x = 1
ICQ = 105*(10 ^ -3)
for x in range(1, 10):
    Rc = x*(10 ^ 3)
    Re = (Vcc - ICQ*Rc - 0.55)/(ICQ ^ 2)
    if Re > 0:
        print("Re: ", Re)

# R1 = 19000
# R2 = 10000
# Rc = 2200
# Re = 5000
# Rs = 1000
# B = 150
# Vcc = 10
# Rl = 50
# Vth = Vcc*(R2/(R1 + R2))
# Rth = (R1*R2)/(R1+R2)
# IB = (Vth - 0.8)/(Rth+((1+B)*Re))
# ICQ = B*IB
# IE = (1+B)*IB
# VCEQ = Vcc - (ICQ*Rc) - (IE*Re)
# r_pi = (B*0.026)/ICQ
# RB = (Rth*r_pi)/(Rth+r_pi) # Rth || r_pi
# RW = (Rc*Rl)/(Rc+Rl)
# Vo = B*RW
# i_o = Vo/Rl
# Vs = ((Rs+RB)/RB)*r_pi
# i_in = Vs/(Rs+RB)
# Ai = i_o/i_in
# # Rdc = Rc + Re
# # Rac = RW+Rc
# Icqideal = Vcc/(RW+Re+Rc+Rc)
# Pd = VCEQ*ICQ
# print("Icqideal: ", Icqideal)
# print("The Small Signal Current Gain is: ", Ai)
# print("ICQ: ", ICQ)
# print("VCEQ: ", VCEQ)
# print("Pd: ", Pd)
# print("Resistor Values:")
# print("R1: ", R1)
# print("R2: ", R2)
# print("Rc: ", Rc)
# print("Re: ", Re)



# Rpa = (Rc*Rl)/(Rc+Rl)
















