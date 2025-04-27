import pandas as pd

class Soldados:
    def __init__(self):
        """Inicializa el conjunto de soldados."""
        self.soldados = pd.DataFrame(columns=["tipo", "ataque", "defensa", "cantidad"])

    def reclutar_soldado(self, tipo, ataque, defensa, cantidad):
        """Añade soldados a la tropa existente."""
        if tipo in self.soldados["tipo"].values:
            self.soldados.loc[self.soldados["tipo"] == tipo, "cantidad"] += cantidad
        else:
            nuevo_soldado = pd.DataFrame([{
                "tipo": tipo, "ataque": ataque, "defensa": defensa, "cantidad": cantidad
            }])
            self.soldados = pd.concat([self.soldados, nuevo_soldado], ignore_index=True)

    def entrenar_soldado(self, tipo, ataque_extra, defensa_extra):
        """Mejora las estadísticas de un soldado si existe."""
        if tipo in self.soldados["tipo"].values:
            self.soldados.loc[self.soldados["tipo"] == tipo, "ataque"] += ataque_extra
            self.soldados.loc[self.soldados["tipo"] == tipo, "defensa"] += defensa_extra

    def obtener_soldados(self):
        """Devuelve el estado actual de los soldados."""
        return self.soldados