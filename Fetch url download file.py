import urllib.request

url = "https://www.w3.org/WAI/WCAG21/Techniques/pdf/PDF3/table.pdf"
save_as = "downloaded_file.pdf"

print(f"Downloading from: {url}")
urllib.request.urlretrieve(url, save_as)
print(f"Saved as: {save_as}")

import os
size_kb = os.path.getsize(save_as) / 1024
print(f"File size: {round(size_kb, 2)} KB")