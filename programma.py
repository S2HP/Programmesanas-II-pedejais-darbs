TEKSTI = "teksti/"
vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecums = ["23", "150", "89", "489514156489654568897"]
dzimums = ["s", "s", "v", "v"]
profesija = ["medmāsa", "medmāsa", "inženieris", "pilots"]



def ierakstit(teksts, faila_nosaukums):
    fails = open(TEKSTI+faila_nosaukums, "w", encoding="utf-8")
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(TEKSTI+faila_nosaukums, "a", encoding="utf-8")
    fails.write(teksts)
    fails.close()


def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as f:
        rindas = f.readlines()
    return rindas

#print(nolasit("faili/teksts.txt"))
#pierakstit("Sveiki, visi!\n", "teksts.txt")

ierakstit("", "cilveks.txt")
for i in range(len(vardi)):
    if dzimums[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    #teksts = vardi[0] + " " + uzvardi[0] + " - " + str(vecums[0]) + "\n"
    teksts = "{} {} - {}, {}, {} \n".format(vardi[i], uzvardi[i], vecums[i], rakstamais, profesija[i])
pierakstit(teksts, "cilveks.txt")

# Faili, kuru nosaukums ir cilveks0.txt
# saturs - Sveiki, {vards}! Jūs esat laimējusi {vecums} dolārus.
