from random import random
import  random

class PassWord:

    @classmethod
    def GetPassWord(cls):
        return ''.join([str(random.randint(0,9)) for _ in range(6)])
