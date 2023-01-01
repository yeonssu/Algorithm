# 상속 : 겹치는 부분이 있을 때 하나의 클래스를 다른 하나에 포함시킬 수 있다

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit:
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print("{} : {}방향으로 적군을 공격합니다. [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {}데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))



