from google_trans_new.google_trans_new import google_translator

translator = google_translator()
Pronounce = translator.translate(
    'Pronounce', lang_src='en', lang_tgt='vi')
print(Pronounce)
