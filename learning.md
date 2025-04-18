## python 补充知识：

- 属性（Attributes）：类的状态或数据，分为实例属性和类属性。

```pycon
class Animal:
    species = "哺乳动物"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age
```

- 方法

```pycon
def speak(self):
        print(f"{self.name}说：喵喵！")  # 实例方法

    @classmethod
    def get_species(cls):
        return cls.species  # 类方法

    @staticmethod
    def is_mammal():
        return True  # 静态方法
```

- 构造方法

```pycon
__init__ 方法：用于初始化对象的属性。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- 继承和多态

```pycon
继承（Inheritance）：允许一个类继承另一个类的属性和方法，促进代码复用。

class Dog(Animal):
    def speak(self):
        print(f"{self.name}说：汪汪！")
多态（Polymorphism）：允许不同类的对象以统一的接口调用各自的方法。

animals = [Animal("动物1", 5), Dog("狗狗", 3)]

for animal in animals:
    animal.speak()  # 根据对象类型调用不同的 speak 方法
```


- 访问权限

```pycon
访问权限：通过命名约定（单下划线 _ 表示受保护，双下划线 __ 表示私有）来控制属性和方法的访问。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # 受保护属性
        self.__secret = "这是私有属性"  # 私有属性

    def get_secret(self):
        return self.__secret
```

- 魔法方法

```pycon
常用魔法方法：如 __str__、__repr__、__eq__ 等，用于定义对象的字符串表示、比较行为等。

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.name == other.name and self.age == other.age
        return False
```

- 单例模式

```pycon
class Singleton:
    _instance = None  # 类属性，用于存储类的唯一实例

    def __new__(cls, *args, **kwargs):
        # 检查类的 _instance 属性是否已经有实例
        if not cls._instance:
            # 如果没有实例，调用父类的 __new__ 方法创建一个新的实例
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance  # 返回类的唯一实例

# 创建两个 Singleton 类的实例
s1 = Singleton()
s2 = Singleton()

# 检查两个实例是否是同一个对象
print(s1 is s2)  # 输出: True
```

- 计算数组大小
```pycon
# 计算列表的大小
my_list = [1, 2, 3, 4, 5]
list_size = len(my_list)

# 计算元组的大小
my_tuple = (10, 20, 30)
tuple_size = len(my_tuple)
```

- 类方法 和 实例方法

```pycon
# 定义派生类
class MyConcreteClass(MyAbstractClass):
    def instance_method(self):
        return "这是实例方法的实现"

    @classmethod
    def class_method(cls):
        return "这是类方法的实现"

# 创建实例并调用方法
obj = MyConcreteClass()
print(obj.instance_method())  # 通过实例调用实例方法
print(MyConcreteClass.class_method())  # 通过类名调用类方法
```


