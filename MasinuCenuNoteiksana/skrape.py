import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time


URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
LAPAS = "MasinuCenuNoteiksana/lapas/"
DATI = "MasinuCenuNoteiksana/dati/"

def saglaba(url, datne):
    rezultats = requests.get(url)
    print(rezultats.status_code)
    if rezultats.status_code == 200:
        with open(datne, 'w', encoding='utf-8') as fails:
            fails.write(rezultats.text)
    return

# saglaba(URL, LAPAS+"pirma.html")

def dabut_info(datne):
    dati_diesel = []
    dati_petrol = []
    dati_hybrid = []
    dati_electric = []
    with open(datne, "r", encoding="utf-8") as f:
        html = f.read()
    
    zupa = bs(html, 'html.parser')

    galvena_dala = zupa.find(id='page_main')

    tabulas = galvena_dala.find_all('table')

    rindas = tabulas[2].find_all('tr')
    for rinda in rindas[1:-1]:
        lauki = rinda.find_all('td')

        auto = {}
        if lauki[1].find('a')['href'] != " ":
            auto['sludinajuma_saite'] = "https://www.ss.lv/"+lauki[1].find('a')['href']+" "
        else:
            auto['sludinajuma_saite'] = " "

        if lauki[1].find('img')['src'] != " ":
            auto['bilde'] = lauki[1].find('img')['src']+" "
        else:
            auto['bilde'] = " "

        if lauki[2].get_text() != " ":
            apraksts_temp = lauki[2].find('a').get_text()
            apraksts_temp = apraksts_temp.replace("\t", "").replace("\r", "").replace("\n", "")
            auto['apraksts'] = apraksts_temp
        else:
            auto['apraksts'] = " "

        if lauki[3].get_text() != " ":
            auto['marka'] = lauki[3].get_text()
        else:
            auto['marka'] = " "

        if lauki[4].get_text() != " ":
            auto['gads'] = lauki[4].get_text()
        else:
            auto['gads'] = " "
        if lauki[5].get_text != " ":
            temp = lauki[5].get_text()
            if temp[-1] == 'D':
                auto['tips'] = 'Dīzelis'
                auto['tilpums'] = temp[:-1]
            elif  temp[-1] == 'E':
                auto['tips'] = 'Elektro'
                auto['tilpums'] = temp[:-1]
            elif  temp[-1] == 'H':
                auto['tips'] = 'Hibrīds'
                auto['tilpums'] = temp[:-1]
            else:
                auto['tips'] = 'Benzīns'
                auto['tilpums'] = temp  
        else: 
            auto['tips'] = " "
            auto['tilpums'] = " "

        if lauki[6].get_text() != "-":
            auto['nobraukums'] = lauki[6].get_text().replace(" tūkst.", "000")
        else:
            continue

        if lauki[7].get_text() != " ":
            auto['cena'] = lauki[7].get_text().replace("  €", "").replace(",", "")
        else:
            auto['cena'] = " "

        if auto['tips'] == 'Dīzelis':
            dati_diesel.append(auto)
        elif auto['tips'] == 'Benzīns':
            dati_petrol.append(auto)
        elif auto['tips'] == 'Hibrīds':
            dati_hybrid.append(auto)
        else:
            dati_electric.append(auto)
           
    return dati_diesel, dati_petrol, dati_hybrid, dati_electric

def saglaba_datus(dati, type):
    with open(DATI+"sslv_{}.csv".format(type), "w", encoding='utf-8') as f:
        lauku_nosaukumi = ['sludinajuma_saite','bilde', 'apraksts', 'marka', 'gads', 'tips', 'tilpums', 'nobraukums', 'cena']
        w = csv.DictWriter(f, fieldnames= lauku_nosaukumi)
        w.writeheader()
        for auto in dati:
            w.writerow(auto)
    return



def atvilkt_lapas(skaits):
    for i in range(1,skaits+1):
        saglaba("{}page{}.html".format(URL, i), "{}lapa{}.html".format(LAPAS, i))
        time.sleep(1)
    return


def dabut_info_daudz(skaits):
    dati_diesel = []
    dati_petrol = []
    dati_hybrid = []
    dati_electric = []
    for i in range(1, skaits+1):
        info_diesel, info_petrol, info_hybrid, info_electric = dabut_info("{}lapa{}.html".format(LAPAS,i))
        dati_diesel += info_diesel
        dati_petrol += info_petrol
        dati_hybrid += info_hybrid
        dati_electric += info_electric

    return dati_diesel, dati_petrol, dati_hybrid, dati_electric

atvilkt_lapas(5)
info_diesel, info_petrol, info_hybrid, info_electric = dabut_info_daudz(5)
saglaba_datus(info_diesel, "diesel")
saglaba_datus(info_petrol, "petrol")
saglaba_datus(info_hybrid, "hybrid")
saglaba_datus(info_electric, "electric")