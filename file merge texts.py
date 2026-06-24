import os

folder      = "chapters"
output_file = "full_book.txt"

with open(output_file, 'w') as outfile:
    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.txt'):
            filepath = os.path.join(folder, filename)
            with open(filepath) as infile:
                outfile.write(f"--- {filename} ---\n")
                outfile.write(infile.read())
                outfile.write("\n\n")
            print(f"Added: {filename}")

print(f"\nAll files merged into {output_file}")