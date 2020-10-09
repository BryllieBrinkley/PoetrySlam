import random

a_file = open("poem.txt")

filename = a_file.readlines()
# for line in filename:
#     print(line)
lines_list = filename

def get_file_lines(filename):
  for line in filename:
    print(str(line) + ",")

# get_file_lines(filename)

def lines_printed_backwards(lines_list):
  lines_list.reverse()
  print(str(lines_list) + ",")

# lines_printed_backwards(lines_list)


def lines_printed_random(lines_list):
  for i in range(len(lines_list)):
    random_idx = random.randrange(len(lines_list))
    print(lines_list[random_idx])
    del lines_list[random_idx]

# lines_printed_random(lines_list)

 # for my custom function i decided to print the "area" of the poem. It's the number of lines in the poems(height) multiplied by the amount of words in the poem(width).

def lines_printed_custom(lines_list):
  height = len(lines_list)
  file = open("poem.txt", "rt")
  data = file.read()
  words = data.split()
  width = len(words)
  area = height * width
  print(area)

# lines_printed_custom(lines_list)