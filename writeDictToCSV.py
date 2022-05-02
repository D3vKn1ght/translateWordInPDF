import numpy as np


class Dict:
    def __init__(self):
        self.dictionary = {}
        self.nameDict = 'dict.npy'
        self.load()

    def save(self):
        np.save(self.nameDict, self.dictionary)
        print("Ghi xong dict.npy")

    def load(self):
        self.dictionary = np.load(self.nameDict, allow_pickle='TRUE').item()
        print("Co", len(self.dictionary), "tu trong dict")

    def writeCSV(self):
        if self.dictionary:
            with open('dict.csv', 'w', encoding="utf-8") as f:
                for key, value in self.dictionary.items():
                    f.write(key + ',' + value + '\n')
            print("Ghi xong dict.csv")


dct = Dict()
# txt = ""
# for x in dct.dictionary:
#     txt += str(x)+" : "+str(dct.dictionary[x])+"\n"
# with open("dict.txt", "w", encoding="utf-8") as f:
#     f.write(txt)

dct.writeCSV()
