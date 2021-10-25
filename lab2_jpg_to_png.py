import os

path = "E:\Python"

for act_path, d_names, f_names in os.walk(path):
    for file in f_names:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.JPG'):
            or_name = act_path + '/' + file
            name = act_path + '/' + os.path.splitext(file)[0]
            os.rename(or_name, name + '.png')
