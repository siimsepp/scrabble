#!/usr/bin/env python3

# Projekti eesmärgiks on luua programm, mis soovitab kasutajale sõnu, mida Scrabble'i eestikeelses versioonis kasutada.
# Programm oskab arvutada sõnade väärtust ning arvestab laual kujunenud olukorda, mida kasutaja saab HTML-vormi abil kirjeldada.
# Kasutaja saab määrata, mis tähed on tal käes ning millist tähte lauast ta soovib kasutada. Samuti saab kasutaja määrata,
# mitu tähte saab sisestada enne lauas olevat tähte ning mitu pärast.
# Samuti ka seda, kas ja kus asuvad sõnade ja tähtede mitmekordistajad.

import collections
import json
import sys


def sonad_failist():
    # Tõmbab andmed failist ja teeb neist listi, mis sisaldab eestikeelseid sõnu.
    with open('lemmad.txt', encoding='utf-8') as f:
        andmed = f.read().split('\n')
    return andmed


def tahed_sonastikuna(sona):
    # Tagastab sõnastiku, mille võtmed on parameetri 'sona' tähed ning väärtused vastava tähe esinemisarv sõnas.
    tahed = [n for n in sona]
    tahtede_sonastik = {}
    for taht in tahed:
        if taht in tahtede_sonastik:
            tahtede_sonastik[taht] += 1
        else:
            tahtede_sonastik[taht] = 1
    return tahtede_sonastik


def kas_alamsonastik(sonastik1, sonastik2):
    # Tagastab True, kui esimene sõnastik sisaldub teises. Töötab ka siis, kui väärtused on erinevad. Esimese sõnastiku sama võtme väärtus
    # peab olema väiksem või võrdne teise sõnastiku sama võtme väärtusega.
    if not set(sonastik1.keys()).issubset(set(sonastik2.keys())):
        return False
    else:
        for taht in sonastik1.keys():
            if sonastik1[taht] > sonastik2[taht]:
                return False
    return True


def sobivad_sonad(tahed_sonana):
    # Leiab failist sõnad, mille kõik tähed on mängijal olemas. Tagastab sõnad listina.
    sonade_loend = []
    for sona in sonad_failist():
        if kas_alamsonastik(tahed_sonastikuna(sona), tahed_sonastikuna(tahed_sonana)):
            sonade_loend.append(sona)
    return sonade_loend


def scrabble_tahtede_vaartused():
    # Tagastab sõnastiku eestikeelses Scrabble'is kasutatavatest tähtedest ja nende väärtustest.
    return {'a': 1, 'b': 4, 'd': 2, 'e': 1, 'f': 8, 'g': 3, 'h': 4, 'i': 1, 'j': 4, 'k': 1, 'l': 1, 'm': 2, 'n': 2, 'o': 1, 'p': 4, 'r': 2, 's': 1, 'š': 10, 'z': 10, 'ž': 10, 't': 1, 'u': 1, 'v': 3, 'õ': 4, 'ä': 5, 'ö': 6, 'ü': 5}


def kas_sona_mahub(sona):
    # Kas tähtedest moodustatav sõna ka tegelikult laua peale ära mahub. See sõltub sellest, millised piirid
    # kasutaja ette andis (mitu tähte enne ja pärast laual olevat tähte saab lauale paigutada).
    sona_max_pikkus = mitu_enne + mitu_parast + 1
    if taht_laual not in sona:
        return False
    elif sona_max_pikkus < len(sona):
        return False
    else:
        # anna laual oleva tahe indeksid sonas
        taht_laual_indeksid_sonas = [
            i for i, x in enumerate(sona) if x == taht_laual]
        for indeks in taht_laual_indeksid_sonas:
            # indeks näitab mitu tähte peab enne mahtuma
            if indeks <= mitu_enne:
                tahti_sonas_parast_laual_olevat_tahte = len(sona) - indeks - 1
                if tahti_sonas_parast_laual_olevat_tahte <= mitu_parast:
                    return True
    return False


def listi_korrutis(jarjend):
    korrutis = 1
    for n in jarjend:
        korrutis *= n
    return korrutis


def sonade_vaartuste_sonastik():
    sonad_vaartused_sonastik = {}
    for sona in sobivad_sonad(tahed_kaes + taht_laual):
        if kas_sona_mahub(sona):
            # Laual oleva tähe indeksid sõnas
            for indeks in [i for i, x in enumerate(sona) if x == taht_laual]:
                tahti_enne = indeks
                tahti_parast = len(sona) - indeks - 1
                if indeks == 0:
                    # kordistaja tähendab tähe kordistajat
                    kordistajad = [1] + kordistajad_parast[:tahti_parast]
                    # Sõna kordistaja puhul on oluline kordistajate korrutis, sest on võimalik, et ühte sõnasse satub mitu kordistajat.

                    sona_kordistajad = listi_korrutis(
                        sona_kordistajad_parast[:tahti_parast])

                    # sona_kordistajad = int(np.prod(
                    #     [1] + sona_kordistajad_parast[:tahti_parast]))
                else:
                    kordistajad = kordistajad_enne[-1*tahti_enne:] + \
                        [1] + kordistajad_parast[:tahti_parast]

                    sona_kordistajad = listi_korrutis(
                        sona_kordistajad_enne[-1*tahti_enne:] + sona_kordistajad_parast[:tahti_parast])

                    # sona_kordistajad = int(np.prod(
                    #     sona_kordistajad_enne[-1*tahti_enne:] + [1] + sona_kordistajad_parast[:tahti_parast]))
                # Tähtede eest saadavad punktid
                punktid = []
                for taht in sona:
                    punktid.append(scrabble_tahtede_vaartused()[taht])
                # print(indeks, sona, kordistajad, sona_kordistajad)
                # print('Punktid: ', punktid)
                tahtede_vaartus_kordistajatega = [
                    a * b for a, b in zip(kordistajad, punktid)]
                sona_vaartus_kokku = sum(
                    tahtede_vaartus_kordistajatega) * sona_kordistajad
                # print(tahtede_vaartus_kordistajatega)
                # print('Sõna väärtus kokku:', sona_vaartus_kokku)

                # Mõnikord saab sama sõna moodustada erinevat moodi. Näiteks kui käes on sama täht, mis lauas.
                # Seetõttu on järgnevad neli rida vajalikud, et sõnastikku saaks see variant sõnast, mille eest saab kõige rohkem punkte.
                if sona not in sonad_vaartused_sonastik:
                    sonad_vaartused_sonastik[sona] = sona_vaartus_kokku
                elif sonad_vaartused_sonastik[sona] < sona_vaartus_kokku:
                    sonad_vaartused_sonastik[sona] = sona_vaartus_kokku
    return sonad_vaartused_sonastik


def loeJSON():
    with open('scrabble_sisend.json', 'r', encoding='UTF-8') as f:
        andmed_sisse = json.load(f)
    tahed_kaes = andmed_sisse[0]['tahed_kaes']
    taht_laual = andmed_sisse[1]['taht_laual']
    kohti_enne = int(andmed_sisse[2]['kohti_enne'])
    kohti_parast = int(andmed_sisse[3]['kohti_parast'])
    kordistajad_enne = andmed_sisse[4]['tahe_kord_enne']
    kordistajad_parast = andmed_sisse[5]['tahe_kord_parast']
    sona_kordistajad_enne = andmed_sisse[6]['sona_kord_enne']
    sona_kordistajad_parast = andmed_sisse[7]['sona_kord_parast']
    return (tahed_kaes, taht_laual, kohti_enne, kohti_parast, kordistajad_enne, kordistajad_parast, sona_kordistajad_enne, sona_kordistajad_parast)


def kirjutaJSON(andmed):
    # andmed_kirjutamiseks = sonade_vaartuste_sonastik()
    json.dump(dict(andmed), open(
        'scrabble_tulemus.json', 'w', encoding='UTF-8'))


andmed_sisse = loeJSON()

tahed_kaes = andmed_sisse[0]
taht_laual = andmed_sisse[1]
mitu_enne = andmed_sisse[2]
mitu_parast = andmed_sisse[3]
kordistajad_enne0 = andmed_sisse[4]
kordistajad_parast0 = andmed_sisse[5]
sona_kordistajad_enne0 = andmed_sisse[6]
sona_kordistajad_parast0 = andmed_sisse[7]

kordistajad_enne = [int(n) for n in kordistajad_enne0]
kordistajad_parast = [int(n) for n in kordistajad_parast0]
sona_kordistajad_enne = [int(n) for n in sona_kordistajad_enne0]
sona_kordistajad_parast = [int(n) for n in sona_kordistajad_parast0]


# Leiab kümme suurima punktide arvuga võtit sõnastikust.
loendur = collections.Counter(sonade_vaartuste_sonastik())
suurimate_punktidega = loendur.most_common(10)

kirjutaJSON(suurimate_punktidega)


for n in suurimate_punktidega:
    print(f'{n[0]}: {n[1]}')
print(suurimate_punktidega)
