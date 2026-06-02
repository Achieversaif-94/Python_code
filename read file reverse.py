fname = input("Enter file name: ")
fhand = open(fname)
lines = fhand.readlines()
fhand.close()

for line in reversed(lines):
    print(line.rstrip())
    