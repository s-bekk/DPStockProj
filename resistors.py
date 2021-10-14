R1 = 0
R2 = 0
Rc = 0
Re = 0
Rs = 1000
B = 100
Vcc = 10
Rl = 50
RW = 0
Icqideal = Vcc/(RW+Re+Rc+Rc)
for R1 in range(1,100000):
    for R2 in range(1, 100000):
        for Rc in range(1, 100000):
            for Re in range(1, 100000):
                Vth = Vcc*(R2/(R1 + R2))
                Rth = (R1*R2)/(R1+R2)
                IB = (Vth - 0.8)/(Rth+((1+B)*Re)) 
                ICQ = B*IB
                IE = (1+B)*IB
                VCEQ = Vcc - (ICQ*Rc) - (IE*Re)
                r_pi = (B*0.026)/ICQ
                RB = (Rth*r_pi)/(Rth+r_pi)
                RW = (Rc*Rl)/(Rc+Rl)
                if ICQ == Icqideal:
                    Vo = B*RW
                    i_o = Vo/Rl
                    Vs = ((Rs+RB)/RB)*r_pi
                    i_in = Vs/(Rs+RB)
                    Ai = abs(i_o/i_in)
                    Pd = VCEQ*ICQ
                    if Ai < 70 or Ai > -70:
                        if (Pd < 3) and (Pd > 0):
                            print("The Small Signal Current Gain is: ", Ai)
                            print("ICQ: ", ICQ)
                            print("VCEQ: ", VCEQ)
                            print("Resistor Values:")
                            print("R1: ", R1)
                            print("R2: ", R2)
                            print("Rc: ", Rc)
                            print("Re: ", Re)





