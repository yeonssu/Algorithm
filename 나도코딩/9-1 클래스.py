# 클래스 : 틀을 만들어 반복적인 작업을 실행한다

# 클래스를 쓰지않고 유닛을 생성하는 방법
name = "마린"   # 이름
hp = 40         # 체력
damage = 5      # 공격력
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{} : {}방향으로 적군을 공격합니다. [공격력 {}]".format(name,location,damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 클래스를 사용하고 유닛을 생성하는 방법
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
