import os

folder = "my_folder"
seen = {}
duplicates = []

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        size = os.path.getsize(filepath)
        key = (filename, size)
        if key in seen:
            duplicates.append(filename)
        else:
            seen[key] = filepath

if duplicates:
    print(f"Found {len(duplicates)} duplicate(s):")
    for d in duplicates:
        print(" ", d)
else:
    print("No duplicates found.")
