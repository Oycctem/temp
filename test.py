import hashlib

title = "tttt"
hash16 = hashlib.sha256(title.encode()).hexdigest()[:16]
print(hash16)
