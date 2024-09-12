from cryptography.fernet import Fernet


async def encrypt(file):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    originalFile = await file.read()
    encryptedData = fernet.encrypt(originalFile)
    filePath = f"./encrypted/encrypted{file.filename}"
    keyPath = f"./encrypted/keys/encryypted{file.filename}.key"
    encryptedFile = open(filePath, "wb")
    encryptedFile.write(encryptedData)
    encryptedFile.close
    keyFile = open(keyPath, "wb")
    keyFile.write(key)
    keyFile.close()
    return filePath, keyPath


async def decrypt(file, keyfile):
    key = await keyfile.read()
    fernet = Fernet(key)
    enc_File = await file.read()
    decryptedData = fernet.decrypt(enc_File)
    filename = file.filename
    stripFilename = filename.strip("encrypted")
    filePath = f"./decrypted/{stripFilename}"
    decryptedFile = open(filePath, "wb")
    decryptedFile.write(decryptedData)
    decryptedFile.close
    return filePath

