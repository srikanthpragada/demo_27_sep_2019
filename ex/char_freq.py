# Chars frequency
st = "This is to test"

chars = {}

for ch in st:
    if ch in chars:
        chars[ch] = chars[ch] + 1   # increment count by 1
    else:
        chars[ch] = 1   # set count to 1

for ch, count in sorted(chars.items()):
    print(ch,count)



