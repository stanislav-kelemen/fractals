import random
import array
from PIL import Image

class IFS:
    def __init__(self, nr_points):
        self.nr_points = nr_points

        # Початкова точка
        self.x = 0.0
        self.y = 0.0

        # Списки для збереження точок фракталу
        self.point_x = []
        self.point_y = []

        '''
        serpinski_carpet
        fern
        tree
        leaf
        dragon
        fractals
        serpinski_triangle
        custom
        '''
        # Імпорт коефіцієнтів афінних перетворень
        with open('./coeff/serpinski_carpet.txt', 'r') as f:
            matrix = [[float(num) for num in line.split(',')] for line in f]

        self.probability_factors = matrix[0]
        self.a = matrix[1]
        self.b = matrix[2]
        self.c = matrix[3]
        self.d = matrix[4]
        self.e = matrix[5]
        self.f = matrix[6]

        # Кількість афінних перетворень
        self.nr_transforms = len(self.probability_factors)

        # Кумулятивна сума вірогідностей,
        # Визначаємо інтервали, які відповідають за кожне перетворення
        self.cumulative_probabilities = [0] * (self.nr_transforms + 1)
        for i in range(1, len(self.cumulative_probabilities)):
            self.cumulative_probabilities[i] = self.cumulative_probabilities[i - 1] + \
                                               self.probability_factors[i - 1]

    def select_transform(self):
        # Випадково вибране афінне перетворення
        rnd = random.random()
        for i in range(self.nr_transforms):
            if self.cumulative_probabilities[i] <= rnd <= self.cumulative_probabilities[i + 1]:
                self.current_transform = i
                break

    def next_point(self):
        # Наступна точка фракталу
        self.select_transform()
        x_new = self.a[self.current_transform] * self.x + self.b[self.current_transform] * self.y + self.e[self.current_transform]
        y_new = self.c[self.current_transform] * self.x + self.d[self.current_transform] * self.y + self.f[self.current_transform]
        self.x = x_new
        self.y = y_new
        self.point_x.append(x_new)
        self.point_y.append(y_new)

    def generate_points(self):
        # Генерація всіх точок фракталу
        for _ in range(self.nr_points):
            self.next_point()

        # Визначення крайніх точок фракталу
        self.x_min = min(self.point_x)
        self.x_max = max(self.point_x)
        self.y_min = min(self.point_y)
        self.y_max = max(self.point_y)


# Ініціалізуємо дані для побудови фрактала
nr_points = 1000000
fern = IFS(nr_points)
fern.generate_points()

# Визначаємо розмір зображення і його масштаб
width, height = 2000, 2000
scale = min([height/(fern.y_max - fern.y_min), width/(fern.x_max - fern.x_min)]) * 0.9

# Ініціалізуємо масив, який буде зберігати пікселі зображення
image_data = array.array('B', [255, 255, 255] * width * height)

# Кожну точку фракталу переносимо на зображення і вибираємо колір
for i in range(nr_points):
    x = int((fern.point_x[i] - fern.x_min) * scale) + int((width - (fern.x_max - fern.x_min) * scale)/2)
    y = -int((fern.point_y[i] - fern.y_min) * scale) - int((height - (fern.y_max - fern.y_min) * scale)/2)

    index = 3 * (y * width + x)
    image_data[index] = random.randrange(0, 255) % 85
    image_data[index + 1] = random.randrange(0, 255) % 170
    image_data[index + 2] = random.randrange(0, 255) % 13

# Показуємо і зберігаємо зображення
img = Image.frombytes("RGB", (width, height), image_data.tobytes())
img.show("ifs")
img.save("ifs.png")
