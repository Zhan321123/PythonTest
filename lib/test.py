class Consider:
    def __init__(self, q, p):
        self.q = q
        self.p = p


table = {
    'A': [Consider(100, 0.3), Consider(75, 0.5), Consider(50, 0.2)],
    'B': [Consider(80, 0.2), Consider(60, 0.6), Consider(40, 0.2)],
    'C': [Consider(70, 0.1), Consider(45, 0.5), Consider(20, 0.4)]
}


def hml(l):
    l = map(str,l)
    result = " ".join(l)
    r = result.replace('0', 'H').replace('1', 'M').replace('2', 'L')
    return r


ag, bg, cg = table.values()

for ia, a in enumerate(ag):
    for ib, b in enumerate(bg):
        for ic, c in enumerate(cg):

            q = a.q + b.q + c.q
            p = a.p * b.p * c.p
            print(hml([ia, ib, ic]),q, p, q * p)
