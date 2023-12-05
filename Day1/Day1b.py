source = open('Day1.txt', 'r')
sum = 0
def find_text_num(line):
    a = line
    print(a)
    b = a.replace('one'  , 'one1one')
    print(b)
    c = b.replace('two'  , 'two2two')
    print(c)
    d = c.replace('three', 'three3three')
    print(d)
    e = d.replace('four' , 'four4four')
    print(e)
    f = e.replace('five' , 'five5five')
    print(f)
    g = f.replace('six'  , 'six6six')
    print(g)
    h = g.replace('seven', 'seven7seven')
    print(h)
    i = h.replace('eight', 'eight8eight')
    print(i)
    j = i.replace('nine' , 'nine9nine')
    print(j)
    k = j.replace('zero' , 'zero0zero')
    print(k)
    return k

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
    current_line = find_text_num(current_line)
    if not current_line:
        break
    new_num = get_left_num(current_line) * 10 + get_right_num(current_line)
    sum += new_num
print(sum)