import os

folder = 'E:\WTaS'

cFiles = 0
cDirs = 0

for dirs, files in os.walk(folder):
    for directories in dirs:
        cDirs += 1
    for Files in files:
        cFiles += 1

print('Total n. of files:', cFiles, '\nTotal n. direcoties:', cDirs)

