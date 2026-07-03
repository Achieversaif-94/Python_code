import os

folder = "my_project"
size_limit_mb = 1

large_files = []

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        size_bytes = os.path.getsize(filepath)
        size_mb = size_bytes / (1024 * 1024)
        if size_mb > size_limit_mb:
            large_files.append((filepath, round(size_mb, 2)))

if large_files:
    print(f"Files larger than {size_limit_mb} MB:\n")
    for path, size in sorted(large_files, key=lambda x: x[1], reverse=True):
        print(f"{size} MB  ->  {path}")
else:
    print("No large files found.")