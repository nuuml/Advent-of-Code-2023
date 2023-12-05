x = open("day5.txt", "r").read().split("\n\n")
seeds = [int(i) for i in x[0][7:].split(" ")]
mappings = [[[int(i)for i in line.split(" ")]for line in mapping.splitlines()[1:]]for mapping in x[1:]]

vals = seeds


ranges = [(seeds[i],seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
mappings = [[[dest-start, start, start+size-1] for dest, start, size in mapping] for mapping in mappings]

def carve(span_start, span_end, map_start, map_end): 
    a,b = span_start, span_end 
    c,d = map_start, map_end  
    if a<c and d<b:
        return [(c,d)], [(a,c-1), (d+1,b)]
    elif a<c<=b:
        return [(c,b)], [(a,c-1)]
    elif a<=d<b:
        return [(a,d)], [(d+1,b)]
    elif c<=a and b<=d:
        return [(a,b)], []
    else:
        return []     , [(a,b)]

for mapping in mappings:
    new_ranges = []
    for seed_span in ranges:
        unprocessed = [seed_span]
        for offset, map_start, map_end in mapping:
            new_unprocessed = []
            for span_start, span_end in unprocessed:
                toMap, extra = carve(span_start, span_end, map_start, map_end)
                new_unprocessed += extra
                new_ranges += [(a+offset,b+offset) for a,b in toMap]
            unprocessed = new_unprocessed
        new_ranges += unprocessed
    ranges = new_ranges

print(min(start for start,_ in ranges))