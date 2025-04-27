class Espadachin:
    def __init__(self, ataque, defensa):
        self.ataque = ataque
        self.defensa = defensa

    def entrenar(self, cantidad):
        """Mejora el ataque y defensa de espadachines."""
        self.ataque += cantidad
        self.defensa += cantidad