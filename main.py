name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if "From " in line:
        clockstr = line.split(" ")[-2]
        hour = clockstr.split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1

for k in sorted(counts):
    print(k, counts[k])