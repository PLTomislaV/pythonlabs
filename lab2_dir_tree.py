import os

path = "E:"

for act_path, d_names, f_names in os.walk(path):
    print(act_path, d_names, f_names)
