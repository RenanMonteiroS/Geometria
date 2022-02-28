class Ponto:
    __slots__ = ['_x_coord', '_y_coord']

    def __init__(self, x_coord, y_coord):

        if not isinstance(x_coord, int) or not isinstance(y_coord, int):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        else:
            self._x_coord = x_coord
            self._y_coord = y_coord

    @property
    def x_coord(self):
        return self._x_coord

    @property
    def y_coord(self):
        return self._y_coord

    @x_coord.setter
    def x_coord(self, valor):
        self._x_coord = valor

    @y_coord.setter
    def y_coord(self, valor):
        self._y_coord = valor

    def __str__(self):
        return f'Ponto:({self.x_coord}, {self.y_coord})'

    def distancia(self, outro_ponto):
        distancia = (((outro_ponto.x_coord - self.x_coord) ** 2) + ((outro_ponto.y_coord - self.y_coord) ** 2)) ** 0.5
        return distancia

    def resetar(self):
        self.x_coord = 0
        self.y_coord = 0

class Circulo(Ponto):
    __slots__ = ['_raio']

    def __init__(self, x_coord, y_coord, raio):
        super().__init__(x_coord, y_coord)
        if not isinstance(raio, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        else:
            self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        self._raio = valor

    def __str__(self):
        return f'Centro:({self.x_coord}, {self.y_coord}. Raio: {self.raio})'

    def area(self):
        area = 3.14 * (self._raio ** 2)
        return area

class Cilindro(Circulo):
    __slots__ = ['_altura']

    def __init__(self, x_coord, y_coord, raio, altura):
        super().__init__(x_coord, y_coord, raio)
        if not isinstance(altura, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        else:
            self._altura = altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def area(self):
        area = (2 * 3.14 * self.raio * self.altura) + ((3.14 * (self.raio ** 2)) * 2)
        return area

    def volume(self):
        volume = (self.raio ** 2) * self.altura * 3.14
        return volume

    def __str__(self):
        return f'Centro:({self.x_coord}, {self.y_coord}. Raio: {self.raio}. Altura: {self._altura})'

class Ponto3D(Ponto):
    __slots__ = ['_z_coord']

    def __init__(self, x_coord, y_coord, z_coord):
        super().__init__(x_coord, y_coord)
        if not isinstance(z_coord, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        else:
            self._z_coord = z_coord

    @property
    def z_coord(self):
        return self._z_coord

    @z_coord.setter
    def z_coord(self, valor):
        self._z_coord = valor

    def distancia(self, outro_ponto):
        #distancia = (((outro_ponto.x_coord - self.x_coord) ** 2) + ((outro_ponto.y_coord - self.y_coord) ** 2) + ((outro_ponto.z_coord - self.z_coord) ** 2)) ** 0.5
        distancia = ((outro_ponto.x_coord - self.x_coord) ** 2) + ((outro_ponto.y_coord - self.y_coord) ** 2)
        distancia += ((outro_ponto.z_coord - self.z_coord)) ** 2
        distancia = distancia ** 0.5
        return distancia

    def resetar(self):
        self.x_coord = 0
        self.y_coord = 0
        self.z_coord = 0


    def __str__(self):
        return f'Ponto:({self.x_coord}, {self.y_coord}, {self._z_coord})'

def run():
    p1 = Ponto3D(1,2,10)
    p2 = Ponto3D(1,2,20)
    print(p1)
    print(p1.distancia(p2))




if __name__ == '__main__':
    run()