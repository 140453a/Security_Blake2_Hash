from hashlib import blake2b
h = blake2b()

target = input("What file to hash(Blake2)?: ")

BLOCKSIZE = 65536
with open(target, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(BLOCKSIZE)


print(h.hexdigest())
