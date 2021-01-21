import hashlib

def getMd5(strr):
    m = hashlib.md5()
    m.update(str(strr).encode("utf-8"))
    return m.hexdigest()