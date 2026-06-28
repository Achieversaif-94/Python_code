import os

folder = "photos"
extensions = ('.jpg', '.jpeg', '.png')
counter = 1

for filename in sorted(os.listdir(folder)):
    if filename.lower().endswith(extensions):
        ext = filename.rsplit('.', 1)[-1]
        new_name = f"photo_{counter}.{ext}"
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"{filename} -> {new_name}")
        counter += 1

print(f"\nRenamed {counter - 1} image(s).")
