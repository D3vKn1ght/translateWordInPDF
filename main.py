import fitz  # this is pymupdf
from google_trans_new.google_trans_new import google_translator
from translatepython.translate import Translator
from Bing_Translate import BingTranslate
import re
import numpy as np
import time
import random
import os
import glob
googleTranslate = google_translator()
myMemoryTranslate = Translator(to_lang="vi")
bingTranslate = BingTranslate()
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
        try:
            resultGoogle = googleTranslate.translate(
                word, lang_src='en', lang_tgt='vi')
            resultGoogle = resultGoogle.lower().strip()
            check = True
        except Exception as e:
            resultGoogle = word
            print("Google translate error: ", e)
            continue
        if resultGoogle != word:
            add += 1

        try:
            resultBing = bingTranslate.translate(word)
            resultBing = resultBing.lower().strip()
            check = True
        except Exception as e:
            resultBing = word
            print("Bing translate error: ", e)
            continue
        if resultBing != word:
            add += 1

        try:
            resultMyMemory = myMemoryTranslate.translate(word)
            resultMyMemory = resultMyMemory.lower().strip()
            check = True
        except Exception as e:
            resultMyMemory = word
            print("MyMemory translate error: ", e)
            continue
        if resultMyMemory != word:
            add += 1
        if check == False or add < 2:
            continue
        trans = "Google: "+resultGoogle+"\tBing: " + \
            resultBing+"\tMymemory: "+resultMyMemory
        print("NEW:", word, ":", trans)

        value = "<div>"
        if resultGoogle != "":
            value += "<b>- Google :</b><br />&emsp;+ {0}<br/>".format(
                resultGoogle.lower().strip().capitalize())
        if resultBing != "":
            value += "<b>- Bing :</b><br />&emsp;+ {0}<br/>".format(
                resultBing.lower().strip().capitalize())
        if resultMyMemory != "":
            value += "<b>- MyMemory :</b><br />&emsp;+ {0}<br/>".format(
                resultMyMemory.lower().strip().capitalize())
        value += "</div>"
        dct[word] = value
        dem += 1
        if dem % 10 == 0:
            np.save(nameDict, dct)
            print("SAVE IN DICT")
            time.sleep(random.randint(5, 10))
