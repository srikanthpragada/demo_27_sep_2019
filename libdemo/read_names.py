# Read lines from names.txt and display them separated by ,

f =  open("names.txt", "rt")
st = f.read().replace("\n",',')
print(st.strip(","))
f.close()

