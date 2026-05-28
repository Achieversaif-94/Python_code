text = "X-Mailer-Version:    3.21"
colon_pos = text.find(':')
version_str = text[colon_pos + 1:].strip()
major, minor = version_str.split('.')
print("Full version:", version_str)
print("Major:", major)
print("Minor:", minor)