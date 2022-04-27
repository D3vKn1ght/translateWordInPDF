import os
import glob
if os.path.isdir('pdf'):
    print('Exists folder pdf')
else:
    print('Folder pdf does not exist')
    os.mkdir('pdf')
for pathFile in glob.glob('pdf/*.pdf'):
    print(pathFile)
