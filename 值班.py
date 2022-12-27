
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for a in range(7):
    for b in range(7):
        if a!=b:
            for c in range(7):
                if (c!=a) and (c!=b):
                    for d in range(7):
                        if (d!=a) and (d!=b) and (d!=c):
                            for e in range(7):
                                if (e!=a) and (e!=b) and (e!=c) and (e!=d):
                                    for f in range(7):
                                        if (f!=a) and (f!=b) and (f!=c) and (f!=d) and (f!=e):
                                            for g in range(7):
                                                if (g!=a) and (g!=b) and (g!=c) and (g!=d) and (g!=e) and (g!=f):
                                                    if (a == c+1) and (d == d==e+2) and (b == g-3) and (f > b) and (f < c) and (f==3):
    print("a 医生:",days[a],'\n')
    print("b 医生:",days[b],'\n')
    print("c 医生:",days[c],'\n')
    print("d 医生:",days[d],'\n')
    print("e 医生:",days[e],'\n')
    print("f 医生:",days[f],'\n')
    print("g 医生:",days[g],'\n')