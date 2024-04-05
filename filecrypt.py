import sys
import os
import operator

path = sys.argv[1]
tmp = os.path.basename(path)
if tmp.endswith('.encrypt'):
    new_name = tmp[:len(tmp) - 8] + '(new)'
else:
    new_name = tmp + '.encrypt'
with open(path, 'rb') as f:
    content = f.read()
key = sys.argv[2]

def crypt(raw: bytes, key: str) -> bytes:
    key = key.ljust(len(raw)).encode()
    return bytes(map(operator.xor, raw, key))
data = crypt(content, key)
with open(new_name, 'wb') as f:
    f.write(data)
