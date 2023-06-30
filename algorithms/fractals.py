import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


class Fractal:
    """
    base class for creating fractals
    """

    POINTS_AMOUNT = 100_000

    def _plot_fractal(self, fern_image, colors=cm.Greens):
        plt.imshow(fern_image[::-1, :], cmap=colors)
        plt.show()


class LeafsFractal(Fractal):
    """
    creates a leaf fractal
    """

    TRANSFORMATIONS_OCCURENCE_PROBABILITIES = [0.01, 0.85, 0.07, 0.07]

    def run(self):
        self.draw_fractal()

    def transformation_1(self, x, y):     # stem
        return 0, 0.16 * y

    def transformation_2(self, x, y):     # successively smaller leaflets
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6

    def transformation_3(self, x, y):     # largest left-hand leaflet
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6

    def transformation_4(self, x, y):     # largest right-hand leaflet
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    def draw_fractal(self):
        fern_image = self._prepare_fractal_points()
        self._plot_fractal(fern_image)

    def _prepare_fractal_points(self):
        width, height = 300, 300
        x, y = 0, 0
        fern_image = np.zeros((width, height))
        transformations = [self.transformation_1, self.transformation_2, self.transformation_3, self.transformation_4]
        for i in range(self.POINTS_AMOUNT):
            function = np.random.choice(
                transformations, p=self.TRANSFORMATIONS_OCCURENCE_PROBABILITIES)  # choose function with probabilty
            x, y = function(x, y)
            ix, iy = int(width / 2 + x * width / 10), int(y * height / 12)
            fern_image[ix, iy] = 1
        return fern_image

class TrianglesFractal(Fractal):
    """
    creates a triangle fractal
    """

    TRANSFORMATIONS_OCCURENCE_PROBABILITIES = [0.3334, 0.3333, 0.3333]

    def run(self):
        self.draw_fractal()

    def transformation_1(self, x, y):
        return 0.5 * x, 0.5 * y

    def transformation_2(self, x, y):
        return 0.5 * x + 1, 0.5 * y

    def transformation_3(self, x, y):
        return 0.5 * x, 0.5 * y + 1

    def draw_fractal(self):
        fern_image = self._prepare_fractal_points()
        self._plot_fractal(fern_image, colors=cm.Reds)

    def _prepare_fractal_points(self):
        width, height = 300, 300
        x, y = 0, 0
        fern_image = np.zeros((width, height))
        transformations = [self.transformation_1, self.transformation_2, self.transformation_3]
        for i in range(self.POINTS_AMOUNT):
            function = np.random.choice(
                transformations, p=self.TRANSFORMATIONS_OCCURENCE_PROBABILITIES)  # choose function with probabilty
            x, y = function(x, y)
            ix, iy = int(width / 2 + x * width / 4), int(y * height / 4)
            fern_image[ix, iy] = 1
        return fern_image


leafs_fractal = LeafsFractal()
triangles_fractal = TrianglesFractal()
leafs_fractal.run()
triangles_fractal.run()
