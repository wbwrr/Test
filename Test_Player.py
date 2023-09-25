import random

class Creature:
    def __init__(self, attack, defense, health):
        self.attack = attack
        self.defense = defense
        self.health = health
# Конструктор __init__ принимает три аргумента: attack, defense и health.
# Значения этих аргументов используются для установки соответствующих
# атрибутов объекта Creature

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.die()

    def die(self):
        print("Существо погибло.")

class Player(Creature):
    def __init__(self, attack, defense, health):
        super().__init__(attack, defense, health)
        self.max_health = health

    def heal(self):
        if self.health == 0:
            print("Нельзя использовать исцеление на погибшем игроке.")
            return
        # Реакция объектов на на некорректные аргументы методов (в данном случае проверка на то,
        # является ли max_health и health целым числом, на то больше ли они нуля, а также
        # проверка не превышает ли health значение max_health)
        if not isinstance(self.max_health, int) or self.max_health <= 0:
            raise ValueError("Неверное значение max_health.")
        if not isinstance(self.health, int) or self.health < 0 or self.health > self.max_health:
            raise ValueError("Неверное значение health.")

        if self.max_health - self.health < 0.3 * self.max_health:
            amount = self.max_health - self.health
        else:
            amount = 0.3 * self.max_health
        self.health += amount
        print(f"Игрок исцелился на {amount} здоровья. Текущее здоровье: {self.health}")

    def attack_creature(self, creature):
        if not isinstance(creature, Creature):
            raise TypeError("Неверное значение объекта существа.")
        attack_modifier = self.attack - creature.defense + 1
        success = False
        if attack_modifier > 0:
            dice_rolls = max(1, attack_modifier)
            for _ in range(dice_rolls):
                roll = random.randint(1, 6)
                if roll >= 5:
                    success = True
                    break

        if success:
            damage = random.randint(1, 6)
            creature.take_damage(damage)
            print(f"Игрок успешно атаковал на {damage} урона.")
        else:
            print("Игрок промахнулся.")

class Monster(Creature):
    def __init__(self, attack, defense, health, damage_range):
        super().__init__(attack, defense, health)
        self.damage_range = damage_range

    def attack_creature(self, creature):
        damage = random.randint(self.damage_range[0], self.damage_range[1])
        creature.take_damage(damage)
        print(f"Монстр атаковал на {damage} урона.")

# Пример использования классов
player = Player(10, 8, 100)
monster = Monster(12, 6, 50, (1, 6))

player.attack_creature(monster)
monster.attack_creature(player)

player.heal()
player.attack_creature(monster)

# РЕАЛИЗАЦИЯ ООП
# Инкапсуляция: Атрибуты attack, defense и health в классе Creature
# являются закрытыми (приватными) и доступны только внутри класса.
# Они могут быть изменены и получены только с помощью методов класса,
# таких как take_damage() и die().

# Наследование: Классы Player и Monster наследуются от класса Creature.

# Полиморфизм: Методы attack_creature() в классах Player и Monster
# имеют одно и то же имя, но выполняют различные действия в зависимости от
# типа объекта, на котором они вызываются.

# Абстракция: Класс Creature является абстрактным представлением
# существа в игре. Он определяет общие атрибуты и методы.
