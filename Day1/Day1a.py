source = open('Day1.txt', 'r')
sum = 0

def get_left_num(line):
    i = 0
    while i < len(line):
        if line[i].isdigit():
            return int(line[i])
        i += 1

def get_right_num(line):
    i = len(line) - 1
    while i >= 0:
        if line[i].isdigit():
            return int(line[i])
        i -= 1

while True:
    current_line = source.readline()

    if not current_line:
        break
    new_num = get_left_num(current_line) * 10 + get_right_num(current_line)
    print(f"{new_num} + {sum} = {new_num + sum}")
    sum += new_num
print(sum)