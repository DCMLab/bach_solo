#!/usr/bin/env python
"""Rename the converted MSCX files bearing the original file names from
Tobi's Notenarchiv."""
import os

def main():
    files = {'BWV_1001_1.mscx': 'BWV1001_01_Adagio.mscx',
     'BWV_1001_2.mscx': 'BWV1001_02_Fuga.mscx',
     'BWV_1001_3.mscx': 'BWV1001_03_Siciliano.mscx',
     'BWV_1001_4.mscx': 'BWV1001_04_Presto.mscx',
     'BWV_1002.mscx': 'BWV1002.mscx',
     'BWV_1003_1.mscx': 'BWV1003_01_Grave.mscx',
     'BWV_1003_2.mscx': 'BWV1003_02_Fuga.mscx',
     'BWV_1003_3.mscx': 'BWV1003_03_Andante.mscx',
     'BWV_1003_4.mscx': 'BWV1003_04_Allegro.mscx',
     'BWV_1004_1.mscx': 'BWV1004_01_Allemande.mscx',
     'BWV_1004_2.mscx': 'BWV1004_02_Courante.mscx',
     'BWV_1004_3.mscx': 'BWV1004_03_Sarabande.mscx',
     'BWV_1004_4.mscx': 'BWV1004_04_Gigue.mscx',
     'BWV_1004_5.mscx': 'BWV1004_05_Chaconne.mscx',
     'BWV_1005_1.mscx': 'BWV1005_01_Adagio.mscx',
     'BWV_1005_2.mscx': 'BWV1005_02_Fuga.mscx',
     'BWV_1005_3.mscx': 'BWV1005_03_Largo.mscx',
     'BWV_1005_4.mscx': 'BWV1005_04_Allegro_assai.mscx',
     'BWV_1006_1.mscx': 'BWV1006_01_Preludio.mscx',
     'BWV_1006_2.mscx': 'BWV1006_02_Loure.mscx',
     'BWV_1006_3.mscx': 'BWV1006_03_Gavotte_en_rondeau.mscx',
     'BWV_1006_4.mscx': 'BWV1006_04_Menuett.mscx',
     'BWV_1006_5.mscx': 'BWV1006_05_Bourée.mscx',
     'BWV_1006_6.mscx': 'BWV1006_06_Gigue.mscx',
     'BWV_1007_k2.mscx': 'BWV1007.mscx',
     'BWV_1008.mscx': 'BWV1008.mscx',
     'BWV_1009_k.mscx': 'BWV1009.mscx',
     'BWV_1010.mscx': 'BWV1010.mscx',
     'BWV_1011.mscx': 'BWV1011.mscx',
     'BWV_1012.mscx': 'BWV1012.mscx',
     'BWV_1013.mscx': 'BWV1013.mscx'}

    for k, v in files.items():
        if os.path.isfile(k):
            os.rename(k, v)
            print(f"{k} => {v}")
        else:
            print(k + " not found")

if __name__ == '__main__':
    main()
