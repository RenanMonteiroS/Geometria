class Garrafa:
    __slots__ = ['_capacidade', '_volume']

    def __init__(self, capacidade=500, volume=0):

        if not isinstance(capacidade, (int, float)) or not isinstance(volume, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        elif capacidade < 0 or volume < 0:
            raise ValueError("O valor é negativo. Tente novamente com um número positivo. Ex.: 100")
        else:
            self._capacidade = capacidade
            self._volume = volume

    def __str__(self):
        return f'Capacidade:{self._capacidade}ml, Volume:{self._volume}ml'

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def volume(self):
        return self._volume



    @capacidade.setter
    def capacidade(self, valor):
        self._capacidade = valor

    @volume.setter
    def volume(self, valor):
        self._volume = valor


    def encher(self, quantidade):
        if not isinstance(quantidade, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        elif quantidade < 0:
            raise ValueError("O valor é negativo. Tente novamente com um número positivo. Ex.: 100")
        elif quantidade + self.volume > self._capacidade:
            raise Exception("O valor adicionado irá exceder a capacidade máxima. Tente novamente.")
        else:
            self._volume -= quantidade
            return self._volume

    def despejar(self, quantidade):
        if not isinstance(quantidade, (int, float)):
            raise TypeError("O valor é inválido! Tente novamente com um número válido. Ex.: 100")
        elif quantidade < 0:
            raise ValueError("O valor é negativo. Tente novamente com um número positivo. Ex.: 100")
        elif self._volume - quantidade < 0:
            raise Exception("O valor adicionado será menor que zero. Tente novamente.")
        else:
            self._volume -= quantidade
            return self._volume




def run():
    try:
        #dando erro quando é colocado algo sem ser um número
        obj1 = Garrafa(100, 'a')

        #dando erro quando a  é negativa
        obj1 = Garrafa(-1, 10)

        #garrafa vazia com 500 ml de capacidade
        obj1 = Garrafa(500, 0)

        #adicionando 20 ml de água
        print('A quantidade da volume adicionando 20 ml é: ' f'{obj1.encher(20)}')
        # funcionando normalmente
        print('A quantidade da volume despejando 5 ml é: ' f'{obj1.despejar(5)}')
        #despejando mais que o possível
        print('A quantidade da volume despejando 21 ml é: ' f'{obj1.despejar(21)}')
        #usando número negativo
        print('A quantidade da volume despejando -1 ml é: ' f'{obj1.despejar(-1)}')
        #usando uma letra
        print('A quantidade da volume despejando a ml é: ' f'{obj1.despejar("a")}')
        #caso fosse transbordar
        print('A quantidade da volume despejando 5000 ml é: ' f'{obj1.despejar(5000)}')

    except Exception as e:
        print(f'Erro: {e}')
    except TypeError as e:
        print(f'Erro: {e}')
    except ValueError as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    run()
