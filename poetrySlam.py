a_file = open("/Users/admin/poem.txt")

lines = a_file.readlines()
for line in lines:
    print(line)