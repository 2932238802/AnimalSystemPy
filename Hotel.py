
from Room import RectRoom
from Room import CircleRoom
from Common import AnimalKind
from Password import PassWord
from Map import  KindToHappyWord

class Hotel:
    _instance = None
    __max_rect_num = 100               # 最多只能有十个 方形
    __max_circle_num = 100             # 最多只能有10个 圆形
    hotel_rect_room = []               # 存放方形房间
    hotel_circle_room = []             # 存放圆形房间
    password_and_room = {}             # 密码和房间   左边是一个房卡 对应一个房间唯一标识符

    def __new__(cls, *args, **kwargs):                                  # 这里设置一个单例模式
        if not cls._instance:
            cls._instance = super(Hotel,cls).__new__(cls,*args,**kwargs)
        return cls._instance

    """
    1. 登记入住
    2. 只要体积合适 房间没人 就可以入住
    """
    def CheckIn(self,animal_out):
        if animal_out.kind_ ==  AnimalKind.Bird:        # 如果是鸟类
                for room in self.hotel_circle_room:
                    if room.IsOkToIn(animal_out) and room.has_animal == False :
                        # 房间状态 #
                        # 有人了 #
                        room.has_animal = True


                        # 动物状态 #
                        # 密钥生成 #
                        password_ = PassWord.GetPassWord()
                        while password_ in self.password_and_room.values():
                            password_ = PassWord.GetPassWord()
                        # 房卡拿到手 #
                        animal_out.room_card = password_
                        room.id_ = password_
                        # 旅馆状态 #
                        self.password_and_room[password_]= room.id_

                        # 打印信息 #
                        print(f"{animal_out.name_}已经入住了 入住房间密码是 {room.id_} 它发出了{KindToHappyWord[animal_out.kind_]}")
                        return True

                print(f"没有圆形房间适合{animal_out.name_}入住，所以无法入住！")
                return False
        else:
                for room in self.hotel_rect_room:
                    if room.IsOkToIn(animal_out) and room.has_animal == False :
                        # 房间状态 #
                        # 有人了 #
                        room.has_animal = True

                        # 动物状态 #
                        # 密钥生成 #
                        password_ = PassWord.GetPassWord()
                        while password_ in self.password_and_room.values():
                            password_ = PassWord.GetPassWord()
                        # 房卡拿到手 #
                        animal_out.room_card = password_
                        room.id_ = password_
                        # 旅馆状态 #
                        self.password_and_room[password_]= room.id_

                        # 打印信息 #
                        print(f"{animal_out.name_}已经入住了 入住房间密码是 {room.id_} 它发出了{KindToHappyWord[animal_out.kind_]}")
                        return True
                print(f"没有方形房间适合{animal_out.name_}入住 所以无法入住！")
                return False


    """
    1. 登记退房
    """
    def CheckOut(self,animal_out):
        for password_,room_id in list(self.password_and_room.items()):
            if animal_out.room_card == password_:
                # 删除对用房间记录 #
                # 如果这个密码是正确的 那么这个房间的id 也一定是对应的 #
                del self.password_and_room[password_]
                # 如果是鸟类 退房是退圆形房子 #
                if animal_out.kind_ == AnimalKind.Bird:
                    for room in self.hotel_circle_room:
                        if room.id_ == room_id:
                            room.has_animal = False
                            print(f"{animal_out.name_}退房成功!")
                            return
                # 如果不是鸟类 #
                else:
                    for room in self.hotel_rect_room:
                        if room.id_ == room_id:
                            room.has_animal = False
                            print(f"{animal_out.name_}退房成功!")
                            return
                animal_out.room_card = ""

    """
    加入方形房间
    """
    def AddRectRoom(self,x,y,z,id_out):
        if len(self.hotel_rect_room) == 10:
            print("hotel没有方形房间的剩余空间了！")
            return
        new_room = RectRoom(x,y,z,id_out)
        self.hotel_rect_room.append(new_room)
        print(f"长是{new_room.x_},宽是{new_room.y_},高是{new_room.z_}，密码是{new_room.id_}：方形房间已经建立")

    """
    加入圆形房间
    """
    def AddCircleRoom(self,r_out,id_out):
        if len(self.hotel_circle_room) == 10:
            print("hotel没有圆形房间的剩余空间了！")
            return
        new_room = CircleRoom(r_out , id_out)
        self.hotel_circle_room.append(new_room)
        print(f"半径是{new_room.r_},房间密码是{new_room.id_}：圆形房间已经建立")

