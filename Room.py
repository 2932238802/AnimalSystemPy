
import math

class RectRoom:
    def __init__(self,x,y,z,id_out):
        self.x_ = int(x)
        self.y_ = int(y)
        self.z_ = int(z)
        self.has_animal = False
        # 唯一标识符 #
        self.id_ = id_out

    def IsOkToIn(self,animal_out):
        return animal_out.x_ <= self.x_ and animal_out.y_ <= self.y_ and animal_out.z_ <= self.z_


class CircleRoom:
    def __init__(self,r,id_out):
        self.r_ = int(r)
        self.id_= id_out
        self.has_animal = False


    def IsOkToIn(self,animal_out):
        return math.pi * self.r_**2 >= animal_out.GetSize()

