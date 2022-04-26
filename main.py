import fitz  # this is pymupdf
from google_trans_new.google_trans_new import google_translator
import re
import numpy as np

translator = google_translator()
dct = {}
dem = 0
nameDict = 'dict.npy'
read = "read.pdf"
# Load
try:
    dct = np.load(nameDict, allow_pickle='TRUE').item()
except Exception as e:
    print("ERROR: ", e)
    np.save(nameDict, dct)

with fitz.open(read) as doc:
    for page in doc:
        result = re.findall("[a-z]{3,15}", page.get_text().lower())
        result = set(result)
        for word in result:
            word = word.lower().strip()
            if word in dct:
                print(word, "da co trong dict")
                continue
            try:
                trans = translator.translate(
                    word, lang_src='en', lang_tgt='vi')
                trans = trans.lower().strip()
                dem += 1
            except Exception as e:
                trans=word
                print("ERROR: ", e)
                continue
            if trans == word:
                continue
            print(word, ":", trans)
            dct[word] = trans
            if dem % 10 == 0:
                np.save(nameDict, dct)
                print("save in dict")
