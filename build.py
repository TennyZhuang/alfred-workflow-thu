#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[-1] not in ['.pyc', '.pyd', '.pyo']:
                file_path = os.path.join(root, file)
                ziph.write(file_path, file_path[file_path.index('/'):])

if __name__ == '__main__':
    zipf = zipfile.ZipFile('thu.alfredworkflow', 'w', zipfile.ZIP_DEFLATED)
    zipdir('src/', zipf)
    zipf.close()
