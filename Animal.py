from Map import KindToCnName
class Animal:
    """
    1. 保证传入的名字有效
    """
    def __init__(self,name_out,kind,x,y,z):
        self.name_ = name_out                # 姓名
        self.x_ = x                           # 尺寸
        self.y_ = y                           # 尺寸
        self.z_ = z                           # 尺寸
        self.kind_ = kind                    # 种类
        self.room_card = ""                  # 持有的房间密码
        print(f"{self.name_}是一只{KindToCnName[self.kind_]}已经生成!")

    def GetSize(self):
        return self.x_ * self.y_ * self.z_



