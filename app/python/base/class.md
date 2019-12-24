# 面向对象

* 基本使用

```python
class Cat(object):

    def __init__(self, name='猫'):
        print('这是一个初始化方法')

        # self.属性名 = 属性的初始值
        self.name = name

        # 实有属性
        self.__zr = 18

    def __zr(self):
        # 在对象方法内部时可以访问私有属性的
        print('%s的主人%s' % (self.name, self.__zr))

    def eat(self):
        print('%s爱吃<。)#)))≦' % self.name)

    def __del__(self):
        print('%s去了' % self.name)

    def __str__(self):
        # 必须返回一个字符串
        # return super().__str__() + '我是小猫'
        return '我是小猫[%s]' % self.name


# 自动调用初始化方法 __init__
tom = Cat('Tom')

print(tom.name)
print(tom)
# del 关键字可以删除一个对象
del tom

lazy_cat = Cat('懒猫')
lazy_cat.eat()

cat = Cat()

cat.eat()

# 私有属性在外界不能访问
# print(cat.zr)
# 私有方法，同样不能被外界调用
# cat.__zr()
```

## 面向对象特征

* 使用继承

```python
class Animal(object):

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')

    def sleep(self):
        print('睡')


class Dog(Animal):

    # 在子类的对象方法中，不能访问父类的私有属性
    # 在子类的对象方法中，不能访问调用父类的私有方法

    def bark(self):
        # 覆盖父类方法
        print('汪汪叫')

    def eat(self):
        # 针对子类特殊的需求，编写代码啊
        print('啥都敢吃')

        # 使用super() 调用原本在父类中的方法
        super().eat()

        # 父类名.方法(self)
        # Dog.bark(self) # 不推荐使用

        # 增加其他子类的代码
        print('*&^%$$@!#$%&')


# 创建一个对象 - 狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
```

* 多继承

```python
class A:

    def test(self):
        print('test 方法')


class B:

    def demo(self):
        print('demo 方法')


class C(A, B):
    pass


# 创建子类对象
c = C()

c.demo()
c.test()

# 确定C类对象调用的顺序
print(C.__mro__)
```

* 多态

```python
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print('%s蹦蹦跳跳的玩耍...' % self.name)


class XioaTianQuan(Dog):

    def game(self):
        print('%s飞到天上玩耍...' % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print('%s和%s一起玩耍' % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 创建一个狗对象
# wangcai = Dog('旺财')
wangcai = XioaTianQuan('哮天犬')

# 创建一个小明对象
xiaoming = Person('小明')

# 让小明和狗玩的方法
xiaoming.game_with_dog(wangcai)
```

* 类属性

```python
class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 创建工具
tool1 = Tool('斧头')
tool2 = Tool('榔头')
tool3 = Tool('水桶')

# 输出工具对象的总数
print(Tool.count)
# print(tool1.count) # 不推荐
```

* 类方法

```python
class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法
    @staticmethod
    def show_help():
        print('帮助信息：让僵尸进入大门')

    # 类方法
    @classmethod
    def show_top_score(cls):
        print('历史最高分：%d' % cls.top_score)

    def start_game(self):
        print('%s开始游戏了...' % self.player_name)


# 查看游戏的帮助信息
Game.show_help()

# 查看历史最高分
Game.show_top_score()

# 创建游戏对象
game = Game('小明')

game.start_game()
```

* __new__方法

```python
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时new方法会被自动调用
        print('创建对象，分配空间')

        # 为对象分配空间
        instance = super().__new__(cls)

        # 返回对象的引用
        return instance

    def __init__(self):
        print('音乐播放器初始化')


# 创建播放器对象
player = MusicPlayer()

print(player)
```

* 单例初始化一次

```python
class MusicPlayer(object):

    # 记录第一个创建对象的引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

        # 如果没有执行过，再执行初始化动作
        print('播放器初始化')

        # 修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
```

___
> 共同学习，共同进步