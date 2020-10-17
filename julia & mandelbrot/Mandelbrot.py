import numpy as np
from PIL import Image

pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
X, Y = 500, 500
iterations = 255

image = Image.new('RGB', (X, Y))
img = image.load()

for ip, p in enumerate(np.linspace(pmin, pmax, X)):
    for iq, q in enumerate(np.linspace(qmin, qmax, Y)):
        c = p + 1j * q
        z = 0
        for k in range(iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                img[ip, iq] = (k % 64 * 4, k % 32 * 8, k % 16 * 16)
                break
image.save('mandelbrot.png')
image.show()
