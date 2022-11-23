import random
import string

def randomizer(panjnang:int) -> str:
    res_str = ''.join(random.choice(string.ascii_letters)for i in range(panjnang))
    return res_str