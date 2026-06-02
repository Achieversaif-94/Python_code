fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    print(line.rstrip().upper())
fhand.close()