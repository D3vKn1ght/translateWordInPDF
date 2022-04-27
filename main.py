import fitz  # this is pymupdf
from google_trans_new.google_trans_new import google_translator
import re
import numpy as np
import time
import random
import os
import glob
translator = google_translator()
dct = {}
dem = 0
nameDict = 'dict.npy'
# Load
# np.save(nameDict, dct)   #Neu bao loi thi chay cau lenh nay truoc
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
        word = word.lower().strip()
        if word in dct:
            print(word, "da co trong tu dien")
            continue
        try:
            trans = translator.translate(
                word, lang_src='en', lang_tgt='vi')
            trans = trans.lower().strip()
            dem += 1
        except Exception as e:
            trans = word
            print("ERROR: ", e)
            continue
        if trans == word:
            continue
        print("NEW:", word, ":", trans)
        dct[word] = trans
        if dem % 10 == 0:
            np.save(nameDict, dct)
            print("SAVE IN DICT")
            time.sleep(random.randint(10, 30))
