class Polc:
    def __init__(self, row:str):
        data = row.strip().split(';')
        self.raktar = data[0]
        self.polc = data[1]
        self.termeknev = data[2]
        self.darab = int(data[3])

    def ures_e(self):
        return self.darab == 0
    
class Eladas:
    def __init__(self, row:str):
        data = row.strip().split(';')
        self.termeknev = data[0]
        self.raktar = data[1]
        self.eladasok_szama = int(data[2])

class Rendeles:
    def __init__(self, row:str):
        data = row.strip().split(';')
        self.termeknev = data[0]
        self.darab = data[1]