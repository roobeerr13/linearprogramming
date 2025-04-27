import pandas as pd

class Recursos:
    def __init__(self):
        """Inicializa los recursos disponibles."""
        self.recursos = pd.DataFrame([
            {"tipo": "comida", "cantidad": 100},
            {"tipo": "madera", "cantidad": 50},
            {"tipo": "oro", "cantidad": 30}
        ])

    def agregar_recurso(self, tipo, cantidad):
        """Añade un recurso o actualiza su cantidad."""
        if tipo in self.recursos["tipo"].values:
            self.recursos.loc[self.recursos["tipo"] == tipo, "cantidad"] += cantidad
        else:
            nuevo_recurso = pd.DataFrame([{"tipo": tipo, "cantidad": cantidad}])
            self.recursos = pd.concat([self.recursos, nuevo_recurso], ignore_index=True)

    def consumir_recurso(self, tipo, cantidad):
        """Reduce la cantidad de un recurso si hay suficiente stock."""
        if tipo in self.recursos["tipo"].values:
            disponible = self.recursos.loc[self.recursos["tipo"] == tipo, "cantidad"].values[0]
            self.recursos.loc[self.recursos["tipo"] == tipo, "cantidad"] = max(0, disponible - cantidad)
    
    def obtener_recursos(self):
        """Devuelve el estado actual de los recursos."""
        return self.recursos