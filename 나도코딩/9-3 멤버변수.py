# 멤버변수 : 클래스 내에서 정의된 변수(self.name, self.hp, self.damage에서 self뒤 부분)
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
        
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

# 객체에 추가로 변수를 외부에서 만들어서 설정할 수 있다
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))