text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(':')
number_str = text[colon_pos + 1:].strip()
number = float(number_str)
print(number)