import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import linprog

class OptimizadorPoder:
    def __init__(self, soldados, recursos):
        """Inicializa la clase con los datos de soldados y recursos."""
        self.soldados = pd.DataFrame(soldados)
        self.recursos = pd.DataFrame(recursos)

    def calcular_optimizacion(self):
        """Optimiza la distribución de soldados según los recursos disponibles."""
        c = -self.soldados[["ataque", "defensa"]].sum(axis=1).values  # Maximizar ataque y defensa

        A = np.array([self.soldados["cantidad"].values])  # Límite en número de soldados
        b = np.array([self.recursos["cantidad"].sum()])  # Total de recursos disponibles

        bounds = [(0, cantidad) for cantidad in self.soldados["cantidad"].values]

        resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

        if resultado.success:
            cantidad_optima = resultado.x
        else:
            cantidad_optima = np.zeros(len(self.soldados))

        return {"Cantidad óptima de soldados": cantidad_optima, "Estado": resultado.success}

    def graficar_resultados(self):
        """Genera gráficos sobre la distribución de soldados."""
        poder_total = self.soldados["ataque"] + self.soldados["defensa"]
        plt.bar(self.soldados["tipo"], poder_total, color=['blue', 'green', 'red'])
        plt.xlabel("Tipo de Soldado")
        plt.ylabel("Poder total (Ataque + Defensa)")
        plt.title("Distribución del Poder Militar")
        plt.show()