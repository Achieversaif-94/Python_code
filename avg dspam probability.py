fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0

for line in fh:
    if line.startswith("X-DSPAM-Probability:"):
        value = float(line.split(":")[1].strip())
        count += 1
        total += value

if count > 0:
    average = total / count
    print("Average DSPAM probability:", average)
else:
    print("No matching lines found.")