
"""
Purpose: 
Date created: 2019-09-18

Contributor(s):
    Mark M.
"""

from os import path
import zipfile
import tempfile
import pandas as pd

full_zip_path = r'C:\path\to\zipfile.zip'

def process_zipfile():
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(full_zip_path, 'r') as zf:
                file_list = [i.filename for i in zf.infolist()]
                zf.extractall(temp_dir)
            filename = 'my-file-name.txt'
            df = pd.read_csv(path.join(temp_dir, filename), low_memory = False)
        try:
            zf.close()
        except:
            pass

        return df

    except FileNotFoundError:
        tmp_name = full_zip_path.split('\\')[-1]
        print(f'Could not find File in zipfile {tmp_name}')
        pass