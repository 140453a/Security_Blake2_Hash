from hashlib import blake2b
h = blake2b() #Setting up the blake2 algorithm. No parameters are needed.

target = input("What file to hash(Blake2)?: ")

BLOCKSIZE = 65536 # This can be any size, it's the size of each block that is encrypted at a time.
with open(target, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        h.update(buf) # Adding the encrypted block to h.
        buf = afile.read(BLOCKSIZE) # Continue to read


print(h.hexdigest()) # Printing the hash for comparison purposes.
