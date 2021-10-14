R1 = 27000
R2 = 15000
Rc = 2200
Re = 1200
Rs = 1000
B = 150
Vcc = 10
Rl = 50
Vth = Vcc*(R2/(R1 + R2))
Rth = (R1*R2)/(R1+R2)
IB = (Vth - 0.8)/(Rth+((1+B)*Re))
ICQ = B*IB
IE = (1+B)*IB
VCEQ = Vcc - (ICQ*Rc) - (IE*Re)
r_pi = (B*0.026)/ICQ
RB = (Rth*r_pi)/(Rth+r_pi)  # Rth || r_pi
RW = (Rc*Rl)/(Rc+Rl)
Vo = B*RW
i_o = Vo/Rl
Vs = ((Rs+RB)/RB)*r_pi
i_in = Vs/(Rs+RB)
# Ai = i_o/i_in
Ai = B*(Rc/(Rc+Rl))*(Rth/(Rth+r_pi))
Pd = VCEQ*ICQ
print("The Small Signal Current Gain is: ", Ai)
print("ICQ: ", ICQ)
print("VCEQ: ", VCEQ)
print("Pd: ", Pd)
print("Resistor Values:")
print("R1: ", R1)
print("R2: ", R2)
print("Rc: ", Rc)
print("Re: ", Re)
