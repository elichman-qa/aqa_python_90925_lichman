# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
#
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.


class Rhombus:

    def __init__(self, name, side_a, angle_ab):
        self.name = name
        self.side_a = side_a
        self.side_b = self.side_a
        self.side_c = self.side_a
        self.side_d = self.side_a
        self.angle_ab = angle_ab
        self.angle_bc = 180 - self.angle_ab
        self.angle_cd = self.angle_ab
        self.angle_da = self.angle_bc

    def __setattr__(self, key, value):
        if key == 'side_a':
            if not isinstance(value, (int, float)):
                raise TypeError(f'Значення повинно бути числом, а ви вносите тип {type(value).__name__}')
            if value <= 0:
                raise ValueError(f'Значення повинно бути числом більше 0, а ви вносите значення ={value}')
            super().__setattr__(key, value)
            super().__setattr__("side_b", value)
            super().__setattr__("side_c", value)
            super().__setattr__("side_d", value)
            return

        if key == 'angle_ab':
            if not isinstance(value, (int, float)):
                raise TypeError(f'Значення повинно бути числом, а ви вносите тип {type(value).__name__}')
            if not 1 <= value < 180:
                raise ValueError(
                    f'Значення повинно бути числом більше 0, і не більше 180 а ви вносите значення ={value}')
            super().__setattr__(key, value)
            super().__setattr__('angle_bc', 180 - value)
            super().__setattr__('angle_cd', value)
            super().__setattr__('angle_da', 180 - value)
            return
        super().__setattr__(key, value)


figure = Rhombus("figure", (int(input("Для зазначення параметрів фігури Ромб, введіть довжину однієї зі сторін: "))), (int(input("Тепер, введіть значення для одного з кутів:  "))))
print(f' Side A = {figure.side_a}, Side B = {figure.side_b}, Side C = {figure.side_c}, Side D = {figure.side_d}')
print(f' <AB = {figure.angle_ab}°, <BC = {figure.angle_bc}°, <CD = {figure.angle_cd}°, <DA = {figure.angle_da}°')
