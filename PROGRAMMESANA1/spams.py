vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecums = [23,150,89,11]
dzimums = ["s", "s", "v", "v"]


for cilveks in visi:
    info = cilveks.split(" ")
    vardi.append(info[0])
    uzvardi.append(info[1])
    vecums1 = int(info[3].rstrip(","))
    vecums.append(vecums1)
    dzimums.append(info[4])
def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
        rindas = fails.readlines()
    return rindas

ierakstit("", "PROGRAMMESANA1/faili/cilveki.txt")

visi = nolasit("PROGRAMMESANA1/faili/cilveki.txt")
vardi = []
uzvardi = []
vecums = []
dzimums = []

for i in range( len(vardi) ):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    teksts = "{} {} - {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais)
    pierakstit(teksts, "PROGRAMMESANA1/faili/cilveki.txt" )

def sutit_vestules(vardi, uzvardi, vecums, dzimums):
    for i in range(0, len(vardi)):
        with open("PROGRAMMESANA1/vestules/vestule{}.txt".format(i), "w", encoding="utf-8") as f:
            if dzimums[i] == "sieviete":
                f.write("Sveika, {} {}! Tu esi laimējusi {}€!".format(vardi[i], uzvardi[i], vecums[i]*10))
            else:
                f.write("Sveiks, {} {}! Tu esi laimējis {}€!".format(vardi[i], uzvardi[i], vecums[i]*10))
        i+=1
               

sutit_vestules(vardi, uzvardi, vecums, dzimums)  