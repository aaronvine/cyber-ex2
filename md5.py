import hashlib

def md5(string):
    return hashlib.md5(string).hexdigest()

#   v2:
#   def hashfile(afile, hasher, blocksize=65536):
    #    buf = afile.read(blocksize)
    #    while len(buf) > 0:
    #        hasher.update(buf)
    #        buf = afile.read(blocksize)
    #    return hasher.digest()

#   [(fname, hashfile(open(fname, 'rb'), hashlib.md5())) for fname in fnamelst]