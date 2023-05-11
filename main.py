import fitz  # this is pymupdf
from googletranslate import translate
from translatepython.translate import Translator
import re
import numpy as np
import time
import random
import os
import glob
myMemoryTranslate = Translator(to_lang="vi")
dct = {}
dem = 0
nameDict = 'dict.npy'
# Load
# np.save(nameDict, dct)  # Neu bao loi thi chay cau lenh nay truoc
dct = np.load(nameDict, allow_pickle='TRUE').item()
if os.path.isdir('pdf'):
    print('Exists folder pdf')
else:
    print('Folder pdf does not exist')
    os.mkdir('pdf')
for pathFile in glob.glob('pdf/*.pdf'):
    print("FILE:", pathFile)
    text = ""
    with fitz.open(pathFile) as doc:
        for page in doc:
            text = text+" "+page.get_text().lower()
    result = re.findall("[a-z]{3,15}", text)
    result = set(result)
    print("Da doc", len(result), "tu")
    for word in result:
        check = False
        add = 0
        word = word.lower().strip()
        if word in dct:
            print(word, "da co trong tu dien")
            continue
        trans = ""
        value = "<div>"
        try:
            resultGoogle = translate( word, dest='vi',  src='en' )
            resultGoogle = resultGoogle.lower().strip()
            check = True
        except Exception as e:
            resultGoogle = word
            print("Google translate error: ", e)
            continue
        if resultGoogle != "" and resultGoogle != word:
            add += 1
            value += "<b>- Google :</b><br />&emsp;+ {0}<br/>".format(
                resultGoogle.lower().strip().capitalize())
            trans = trans+"Google: "+resultGoogle + "\t"
        else:
            continue

        # try:
        #     resultBing = bingTranslate.translate(word)
        #     resultBing = resultBing.lower().strip()
        #     check = True
        # except Exception as e:
        #     resultBing = word
        #     print("Bing translate error: ", e)
        # if resultBing != "" and resultBing != word:
        #     add += 1
        #     value += "<b>- Bing :</b><br />&emsp;+ {0}<br/>".format(
        #         resultBing.lower().strip().capitalize())
        #     trans = trans+"Bing: " + resultBing+"\t"

        try:
            resultMyMemory = myMemoryTranslate.translate(word)
            resultMyMemory = resultMyMemory.lower().strip()
            check = True
        except Exception as e:
            resultMyMemory = word
            print("MyMemory translate error: ", e)
        if resultMyMemory != "" and resultMyMemory != word:
            add += 1
            value += "<b>- MyMemory :</b><br />&emsp;+ {0}<br/>".format(
                resultMyMemory.lower().strip().capitalize())
            trans = trans+"Mymemory: "+resultMyMemory
        value += "</div>"

        dem += 1
        if check == False or add < 2:
            continue

        print("NEW:", word, ":", trans)
        dct[word] = value
        if dem % 10 == 0:
            np.save(nameDict, dct)
            print("SAVE IN DICT")
            print("Hien co ", len(dct), "tu")
            # if dem % 30 == 0:
            #     timeNgu = random.randint(20, 30)
            #     print("Sleep ", timeNgu, "s")
            #     time.sleep(timeNgu)
np.save(nameDict, dct)
print("SAVE IN DICT")
print("Hien co ", len(dct), "tu")
