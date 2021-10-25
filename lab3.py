import os

path = "E:/Python/text/working"

# if we want to delete the word specified in what_to_replace
# we can simply put '' in replace_with vector

what_to_replace = ['is', 'in', 'we can put what we want in here']
replace_with = ['', '!', 'but the list SIZES of replace_with and what_to_replace MUST BE EQUAL!!!!']

for act_path, d_names, f_names in os.walk(path):
    for file in f_names:
        if os.path.splitext(file)[1].lower() in ('.txt', '.TXT'):
            fin = open(act_path + '/' + file, "rt")
            data = fin.read()
            fin.close()
            i = 0
            for word in what_to_replace:
                data = data.replace(word, replace_with[i])
                i = i+1

            fin = open(act_path + '/' + file, "wt")
            fin.write(data)
            fin.close()
