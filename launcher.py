import os
import sys

from pathlib import Path

# pip install tqdm
from tqdm import tqdm

# pip install requests
import requests


def sizeof_fmt(num: int | float) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%.1f %s" % (num, x)

        num /= 1024.0

    return "%.1f %s" % (num, 'TB')


url = 'https://github.com/Flipmixplay/SWMG/archive/refs/heads/main.zip'
# Streaming, so we can iterate over the response.
rs = requests.get(url, stream=True)

# Total size in bytes.
total_size = int(rs.headers.get('content-length', 0))
print('From content-length:', sizeof_fmt(total_size))

chunk_size = 1024 * 1024
num_bars = int(total_size / chunk_size)

file_name = os.path.basename(url)

with open(file_name, mode='wb') as f:
    for data in tqdm(rs.iter_content(chunk_size), total=num_bars, unit='MB', file=sys.stdout):
        f.write(data)
        
#Проверяем размер файла

file_data = open(file_name, mode='rb').read()
print('File data size:', sizeof_fmt(len(file_data)))        
