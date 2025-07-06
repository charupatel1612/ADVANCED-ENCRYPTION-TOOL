from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os

def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def encrypt_file(filename, password):
    key = get_key(password)
    chunksize = 64 * 1024
    out_filename = filename + '.enc'
    iv = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = str(os.path.getsize(filename)).zfill(16)

    with open(filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(iv)

            while chunk := infile.read(chunksize):
                if len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(filename, password):
    key = get_key(password)
    chunksize = 64 * 1024
    out_filename = filename.replace('.enc', '.dec')

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16).decode('utf-8'))
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while chunk := infile.read(chunksize):
                data = decryptor.decrypt(chunk)
                outfile.write(data)
            outfile.truncate(filesize)
