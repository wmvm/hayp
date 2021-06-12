import csv
import pathlib

red = pathlib.Path("oldnew.map")
if red.exists():
    red = open("oldnew.map", "w")
else:
    red = open("oldnew.map", "x")

with open("Links.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        x = row[0].split("\n")
        for OLD_L in x:
            dom = 'https://www.haypost.am'
            dom2 = 'https://haypost.am'
            if dom or dom2 in OLD_L:
                OLD_L = OLD_L.replace(dom, "").strip()
                if OLD_L == "":
                    OLD_L = "/"
                NEW_l = row[1].replace(dom2, "").strip()
                OLD_L = OLD_L.replace(" ", "")
                NEW_l = NEW_l.replace(" ", "")
                t = (OLD_L+' ', NEW_l+';', "\n")
                red.writelines(t)

red.close()

