import hashlib

h = hashlib.sha3_256()

data = b"teknik informatika ITS"
print("Input : ", data)
h.update(data)
st = ""
for i in h.digest():
    st += str(hex(i)) + "/"
print(st)

#h.update(b"tambah string lagi")
#for i in h.digest():
#    st += str(hex(i)) + "/"
#print(st)
