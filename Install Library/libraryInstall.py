import subprocess

libraries_to_install = ['opencv-python', 'gtts', 'Pillow', 'tk']

for library in libraries_to_install:
    subprocess.check_call(['pip', 'install', library])
