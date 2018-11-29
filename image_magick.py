import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, 'Source')
result_dir = os.path.join(current_dir, 'Result')
files_list = os.listdir(source_dir)

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

for i, file in enumerate(files_list):
    cmd = 'convert "' + os.path.join(source_dir, file) + '" -resize 200 "' + os.path.join(result_dir, file) + '"'
    subprocess.Popen(cmd)
