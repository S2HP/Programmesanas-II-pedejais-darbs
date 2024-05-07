class Cilveks:
    def __init__(self, vards, vecums, dzimums, nauda):
        self.age = vecums
        self.name = vards
        self.sex = dzimums
        self.money = nauda

    def dzimsanas_diena(self):
        self.age += 1

    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards

    def nopelnīt(self, jauna_naudas_summa):
        self.money += 1

    def pastastit_par_sevi(self):
        if self.sex == "s":
            dz = "sieviete"
        elif self.sex == "v":
            dz = "vīrietis"
        else:
            dz = self.sex
        print(("Mani sauc {}, man ir {} gadi, es esmu {}, man pieder {} eiro.").format(self.name, self.age, dz, self.money))


persona1 = Cilveks("Jānis", 18, "vīrietis", 653)
persona1.pastastit_par_sevi()
persona1.dzimsanas_diena()
persona1.pastastit_par_sevi()
persona1.nopelnīt(30)

turpinat = "T"
cilveki = []
while turpinat == "T":
    vards = input("Ievadiet cilvēka vārdu: ")
    vecums = int(input("Ievadiet cilvēka vecumu: "))
    dzimums = input("Ievadiet cilvēka dzimumu (s vai v): ")
    nauda = int(input("Ievadiet naudas summu: "))
    cilveki.append(Cilveks(vards, vecums, dzimums, nauda))
    turpinat = input("Ja vēlies pievienot vēl vienu cilvēku, nospied 'T': ")

for viens in cilveki:
    viens.pastastit_par_sevi()
    