
import os
import socket
import time
import random
from Animal import Animal
from Common import AnimalKind
from Map import KindToCnName


# 这个是扩展的部分 老师：

class PythonShellForAnimal:
    # 获取用户名字 和 主机名字 #
    # getcwd 这个是获取当前的工作目录 #
    username_ = os.getlogin()
    hostname_ = socket.gethostname()
    current_dir = os.getcwd()
    timestamp_ = time.time()
    local_time = time.localtime(timestamp_)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    def __init__(self,hotel_out):
        self.hotel_ = hotel_out
        self.commands_ = {
            "addrect": self.AddRectRoom,
            "addcircle": self.AddCircleRoom,
            "droom":self.DeleRoom,
            "checkin": self.CheckIn,
            "checkout": self.CheckOut,
            "exit":self.Exit,
            "help":self.ShowHelp,
            "showani":self.ShowAnimal,
            "showkind":self.ShowKind,
            "showcroom": self.ShowCRoom,
            "showrroom": self.ShowRRoom,
            "showroom":self.Showroom,
            "clear":self.Clear,
            "random": self.RandomHouse
        }
        # 动物 #
        self.animal_contain = {}
        self.hotel_.hotel_rect_room = []
        self.hotel_.hotel_circle_room = []
        self.hotel_.password_and_room = {}

    """
    这里死循环 运行
    """
    def Run(self):
        while True:
            try:
                self.PrintFormat()
                cmd_ = input("").strip()
                if not cmd_:
                    continue
                self.DealCMD(cmd_)
            except Exception as e:
                print(f"发生错误: {e}")
    """
    这里接受指令
    """
    def DealCMD(self,cmd_):
        cmd_contain = cmd_.split()
        cmd_head =cmd_contain[0].lower()
        args_ = cmd_contain[1:]
        # 在的话 返回对应的函数 #
        handler_ = self.commands_.get(cmd_head,self.Unknow)
        handler_(args_)
        # 退出 #
    """
    这里实现一个 打印数据
    end="" 是为了不换行
    """
    def PrintFormat(self,args_=None):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{current_time}]{self.username_}:f{self.current_dir}$", end="")

    """
    这里实现   
    """
    def Unknow(self,args_=None):
        print_text= """
        对不起，暂没有你这个指令
        要么你先试试这个 help
        """
        print(print_text)
        return


    def AddRectRoom(self,args_):
        if len(args_) != 4:
            print("用法错误!")
            print_text = """
            addroom x(int) y(int) z(int) id(int)
            ADDRoom x(int) y(int) z(int) id(int)
            """
            print(print_text)
            return


        # 用法正确 #
        else:
            x_ = args_[0]
            y_= args_[1]
            z_ = args_[2]
            id_ = args_[3]
            self.hotel_.AddRectRoom(x_,y_,z_,id_)
            print("插入成功")
            return

    def AddCircleRoom(self,args_):
        if len(args_) != 2 :
            print("用法错误!")
            print_text = """
            addcircleroom r(int)  id(int)
            ADDCIRCLEROOM r(int)  id(int)
            """
            print(print_text)
            return

        # 用法正确 #
        else:
            r_ = args_[0]
            id_ = args_[1]
            self.hotel_.AddCircleRoom(r_,id_)
            print("插入成功")
            return

    def DeleRoom(self,args_):
        if len(args_) != 1:
            print("用法错误!")
            print_text = """
            droom <password(int(100000-999999))>
            """

        else:
            password_ = int(args_[0])
            for room_ in self.hotel_.hotel_rect_room:
                if room_.id_ == password_:
                    self.hotel_.hotel_rect_room.remove(room_)
                    del self.hotel_.password_and_roomp[password_]
                    print(f"密码是{password_}的方形房间已经删除")
                    return
            for room_ in self.hotel_.hotel_circle_room:
                if room_.id_ == password_:
                    self.hotel_.hotel_circle_room.remove(room_)
                    del self.hotel_.password_and_roomp[password_]
                    print(f"密码是{password_}的圆形房间已经删除")
                    return

            print("对不起，对应该密码的房间不存在，要不尝试 showroom ?")

    def RandomHouse(self,args_):
        if len(args_)!=2:
            print_text = """
            1. 
            random circle <num(int)>
            random rect <num(int)>
            """
            print("用法错误!")
            print(print_text)
        else:
            for _ in range(int(args_[1])):
                if args_[0] != "circle" and args_[0] != "rect":
                    print_text = """
                                2.
                                random circle <num(int)>
                                random rect <num(int)>
                                """
                    print("用法错误!")
                    print(print_text)
                # 用法正确的位置 #
                else:
                    if args_[0] == "circle":
                        # 生成 1 - 10 的数字 #
                        r_ = random.randint(1,10)
                        id_ = -1
                        self.hotel_.AddCircleRoom(r_, id_)
                        print("插入成功")
                    else:
                        x_ = random.randint(1,10)
                        y_ = random.randint(1,10)
                        z_ = random.randint(1,10)
                        id_ = -1
                        self.hotel_.AddRectRoom(x_, y_, z_, id_)
                        print("插入成功")

    def CheckIn(self,args_):
        if len(args_)!=5:
            print("用法错误!")
            print_text = """
            checkin <animal_name(str)> <kind(class AnimalKind)> <x(int)> <y(int)> <z(int)> 
            """
            print(print_text)
            return

        else:
            name = str(args_[0])
            kind = args_[1]
            try:
                x_ = int(args_[2])
                y_ = int(args_[3])
                z_ = int(args_[4])
            except ValueError:
                print("参数类型错误。<x>, <y>, <z> 应为整数。")
                print("""
            用法:
            checkin <animal_name(str)> <kind(str)> <x(int)> <y(int)> <z(int)>
                    """)
                return

            # 找一下 kind在不在 AnimalKind里面
            if hasattr(AnimalKind, kind):
                kind_value = getattr(AnimalKind, kind)
                if name in self.animal_contain:
                    print(f"动物 '{name}' 已存在。")
                    return
                animal_ = Animal(name, kind_value, x_, y_, z_)
                if self.hotel_.CheckIn(animal_):
                    self.animal_contain[animal_.name_] = animal_
                return

            else:
                print(f"未知的动物种类: {kind}")
                print("可用种类:", ", ".join(KindToCnName.keys()))
                return


    def CheckOut(self,args_):
        if len(args_)!=1:
            print("用法错误!")
            print_text = """
            checkout animal_name(str)
            """
            print(print_text)
            return
        # 数量输入正确 #
        else:
            if isinstance(args_[0],str):
                for animal_name_in_contain,animal in self.animal_contain.items():
                    if animal_name_in_contain == args_[0]:
                        self.hotel_.CheckOut(animal)
                        del self.animal_contain[args_[0]]
                        return
                print("用法错误!")
                print_text = """
                            请检查动物名字是否正确
                            可以 输入指令 <showanimal>
                            """

                print(print_text)
                return
            else:
                print("用法错误!")
                print_text = """
                            checkout <animal_name(str)>
                            """
                print(print_text)
                return

    """
    展示创建的房间信息
    """
    def ShowCRoom(self,args_=None):
        print("圆形房间如下:")
        header_ = ["半径","房间密码","是否有动物入住"]
        print("-" * 47)
        print("{:<4}{:<6}{:<7}".format(*header_))
        print("-" * 47)
        for circle_room in self.hotel_.hotel_circle_room:
            print("{:<6}{:<10}{:<14}".format(
                circle_room.r_,circle_room.id_,circle_room.has_animal
            ))
            print("-" * 47)

    def ShowRRoom(self,args_=None):
        print("方形房间如下:")
        header_ = ["长","宽","高","房间密码","是否有动物入住"]
        print("-" * 47)
        print("{:<4}{:<4}{:<4}{:<10}{:<10}".format(*header_))
        for rect_room in self.hotel_.hotel_rect_room:
            print("{:<5}{:<5}{:<5}{:<14}{:<14}".format(
                rect_room.x_,rect_room.y_,rect_room.z_,rect_room.id_,rect_room.has_animal
            ))
            print("-" * 47)

    def Showroom(self,args_=None):
        self.ShowRRoom()
        self.ShowCRoom()

    def ShowAnimal(self,args_=None):
        # 打印一下头 #
        headers_ = ["姓名","种类","x","y","z","房间密码"]
        print("{:<10}{:<10}{:<5}{:<5}{:<5}{:<10}".format(*headers_))
        print("-" * 47)
        for animal_name_in_contain,animal_ in self.animal_contain.items():
            kind_name = KindToCnName[animal_.kind_]
            print(
                "{:<10}{:<10}{:<5}{:<5}{:<5}{:<10}".format(
                    animal_.name_ , kind_name, animal_.x_ , animal_.y_, animal_.z_, animal_.room_card
                )
            )
            # 画一条线
            print("-"*47)

    def ShowKind(self,args=None):
        print_text ="""
        
        class AnimalKind:
        Amphibious      # 两栖
        Reptile         # 爬行
        Fish            # 鱼类
        Mammal          # 哺乳
        Bird            # 鸟类
        """
        print(print_text)

    def ShowHelp(self, args=None):
        help_text = """
    可用命令:
      addrect <x(int)> <y(int)> <z(int)> <id(int)>
        添加方形房间

      addcircle <r(int)> <id(int)>
        添加圆形房间

      droom <animal_name(str)>
        删除动物房间  
        
      checkin <animal_name(str)> <kind(str)> <x(int)> <y(int)> <z(int)>
        动物入住

      checkout <animal_name(str)>
        动物退房

      showani
        显示所有动物

      showkind
        显示种类名称
        
      showcroom 
      showrroom 
      showroom
        显示圆形/方形房间类型
        
      random circle <num(int)>
      random rect <num(int)>
        随机生成若干房间
        
      help
        显示帮助信息
        
      clear
        清理屏幕

      exit
        退出Shell
            """
        print(help_text)

    """
    退出Shell
    """
    def Exit(self, args=None):
        print("退出酒店shell")
        exit()


    def Clear(self,args=None):
        try:
            # 判断操作系统并执行对应的清屏命令
            command = "cls" if os.name == "nt" else "clear"
            os.system(command)
        except Exception as e:
            print(f"清理屏幕时发生错误: {e}")


















