import numpy as np
from PIL import Image

iterations = 255
X, Y = 1280, 680
reMin, reMax, imMin, imMax = 0.5, 2.0, 0.5, 1.0
r = 2

c1 = -0.7382
c2 = 0.0827
counter = -1
image = Image.new('RGB', (X, Y))
img = image.load()
for i in range(X):
    for j in range(Y):
        x = reMax * (i - X / 2) / (reMin * X)
        y = imMax * (j - Y / 2) / (imMin * Y)
        itr = iterations
        while abs(np.sqrt(x ** 2 + y ** 2)) <= r and itr > 1:
            itr -= 1
            temp = x ** 2 - y ** 2 + c1
            y, x = 2 * x * y + c2, temp
        counter += 1
        print(counter, itr)
        img[i, j] = (itr % 16 * 16, itr % 32 * 8, itr % 64 * 4)

image.save('julia.png')
