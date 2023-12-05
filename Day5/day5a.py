x = open("day5.txt", "r").read().split("\n\n")
seeds = [int(i) for i in x[0][7:].split(" ")]
mappings = [[[int(i)for i in line.split(" ")]for line in mapping.splitlines()[1:]]for mapping in x[1:]]

vals = seeds
for mapping in mappings:
    new_vals = []
    for val in vals: 
        new_val = val
        for dest, start, size in mapping:
            if start <= val < start + size:
                new_val = val - start + dest
                break
        new_vals.append(new_val)
    vals = new_vals

print(min(vals))
