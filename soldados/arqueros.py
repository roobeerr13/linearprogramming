class Arquero:
    def __init__(self, ataque, defensa):
        self.ataque = ataque
        self.defensa = defensa

    def mejorar_ataque(self, cantidad):
        """Aumenta el ataque de los arqueros."""
        self.ataque += cantidad

    def mejorar_defensa(self, cantidad):
        """Refuerza la defensa de los arqueros."""
        self.defensa += cantidad