import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

digest = hashes.Hash(hashes.MD5(), default_backend())
with open('File_001.exe', 'rb') as f:
    contents = f.read()

digest.update(contents)
result_1 = digest.finalize().hex()
print('File_001.exe hash is: {}'.format(result_1))

digest_2 = hashes.Hash(hashes.MD5(), default_backend())
with open('File_002.exe', 'rb') as f:
    contents = f.read()

digest_2.update(contents)
result_2 = digest_2.finalize().hex()
print('File_002.exe is: {}'.format(result_2))

if (result_1 == result_2):
    print('The files has the same hash')
else:
    print('The files has different hash')