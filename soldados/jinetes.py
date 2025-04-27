class Jinete:
    def __init__(self, ataque, defensa):
        self.ataque = ataque
        self.defensa = defensa

    def aumentar_velocidad(self, porcentaje):
        """Incrementa la agilidad de los jinetes."""
        self.ataque *= (1 + porcentaje / 100)
        self.defensa *= (1 + porcentaje / 100)