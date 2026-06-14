import os

folder = "my_folder"
prefix = "cleaned_"

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, prefix + filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {prefix + filename}")

print("Done.")