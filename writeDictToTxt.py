import numpy as np


class Dict:
    def __init__(self):
        self.dictionary = {}
        self.nameDict = 'dict.npy'
        self.load()

    def save(self):
        np.save(self.nameDict, self.dictionary)

    def load(self):
        self.dictionary = np.load(self.nameDict, allow_pickle='TRUE').item()


dct = Dict()
txt = ""
for x in dct.dictionary:
    txt += str(x)+" : "+str(dct.dictionary[x])+"\n"
with open("dict.txt", "w", encoding="utf-8") as f:
    f.write(txt)

print("Co", len(dct.dictionary), "tu trong dict")
