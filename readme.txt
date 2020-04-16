Nothing is required except python (I believe hashlib comes with python.)

The hash function returns identical hash on identical files, and returns a different hash on missing_period.txt, which is missing a period at the end.

The hashing algorithm is blake2, called blaked2b because b is the 64bit variant.

From their website blake2.net:
BLAKE2 is a cryptographic hash function faster than MD5, SHA-1, SHA-2, and SHA-3, yet is at least as secure as the latest standard SHA-3.

I picked this algorithm because it required no extra package installs, and it's fast and seems like the future of hashing algorithms!
