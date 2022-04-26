import fitz  # this is pymupdf

with fitz.open("test.pdf") as doc:
    # text = ""
    dem = 0
    for page in doc:
        print(dem, page.get_text())
        # text += page.get_text()

# print(text)
