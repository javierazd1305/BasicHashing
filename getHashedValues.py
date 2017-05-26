from hash_alg import hashAlg
from unhash_alg import unhashAlg
valor = "javierazd@hotmail.com"
hashed = hashAlg(valor)
again = unhashAlg(hashed)
print hashed, again
print type(again)
