import math
import random
import binascii
from Crypto.Util import number

x = "string"
num = int(binascii.hexlify(x.encode("utf-8")), 16)
print(num)
z = binascii.unhexlify(format(num, "x").encode("utf-8")).decode("utf-8")
print(z)