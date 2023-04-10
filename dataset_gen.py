import os

import pandas as pd

l = []
d = {}
c = 1
for path in os.listdir("./logos"):
    for folder in os.listdir("./logos/" + path):
        for img in os.listdir("./logos/" + path + "/" + folder):
            d = {}
            imagePath = "./drive/MyDrive/logos/" + path + "/" + folder + "/" + img
            d["filepath"] = imagePath
            d["team_name"] = folder
            l.append(d)

df = pd.DataFrame(l)
df.to_csv("td1.csv", index=False)
