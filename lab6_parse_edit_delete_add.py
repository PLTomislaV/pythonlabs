import csv

with open("E:\Python/addresses.csv", 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)

    lines = [line for line in reader]

    print(headers)

    for line in lines:
        print(line)

    while True:
        print("For deleting the line instert: 'D'")
        print("For editing a line insert: 'E'")
        print("For adding a new line insert: 'A'")
        decision1 = input()
        if decision1 == 'D':
            print("Please insert the number of line You want to delete.")
            desision2 = input("Header line ie.:'name',surname'... being the line number '0':")
            try:
                decision22 = int(desision2)
            except:
                print("IT's not anumber my dude....")
                break

            if decision22 <= len(lines):
                new_lines = []
                new_lines.append(headers)
                for i in range(0,len(lines)):
                    print(i)
                    if i == decision22:
                        print("line deleted")
                    else:
                        new_lines.append(lines[i])


            else:
                print("number out of range dude....")
                break
            break

        elif decision1 == 'E':

            print("Please insert the number of line You want to edit.")
            desision2 = input("Header line ie.:'name',surname'... being the line number '0':")
            try:
                decision22 = int(desision2)
            except:
                print("IT's not anumber my dude....")
                break

            if decision22 <= len(lines):
                print("Please insert the number of entry You want to edit.")
                decision3 = input("First entry 'name' being the number '0' , max being: {}:".format(len(lines[decision22])))
                try:
                    decision33 = int(decision3)
                except:
                    print("IT's not anumber my dude....")
                    break
                if decision33 <= len(lines[decision22]):
                    new_content = input("Please input Your input:")
                    new_lines = []
                    new_lines.append(headers)
                    for i in range(0, len(lines)):
                        print(i)
                        if i == decision22:
                            lines[i][decision33] = new_content
                            print("content edited")
                        new_lines.append(lines[i])
                        break

                else:
                    print("number out of range dude....")
                    break


        if decision1 == 'A':
            new_lines = []
            new_lines.append(headers)
            new_line = []
            for content in range(0,len(headers)):
                a = input("Please input each data separately, firstly 'name' then press enter and second 'surname' etc..")
                print(headers)
                new_line.append(a)

            for line in lines:
                new_lines.append(line)

            new_lines.append(new_line)
            print("new line added")
            break
        else:
            print("WRONG INPUT...")
            break

    with open("E:\Python/new_addresses.csv", 'w') as new_file:
        writer = csv.writer(new_file)
        for line in new_lines:
            writer.writerow(line)
