# __init__ : 생성자, 객체를 생성할 때 반드시 호출되고 제일 먼저 실행되는 일종의 메서드
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
        
# 객체 : marine1, marine2, tank에 대입한 class로부터 만들어지는 것
# 인스턴스 : 생성된 객체를 실체화한 것        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
