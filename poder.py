import numpy as np
import pandas as pd

def calcular_poder(soldados, recursos):
    """Calcula el poder total basado en soldados y recursos."""
    poder_ataque = soldados["ataque"].sum()
    poder_defensa = soldados["defensa"].sum()
    recursos_disponibles = recursos["cantidad"].sum()

    poder_total = (poder_ataque + poder_defensa) * np.log1p(recursos_disponibles)

    return {
        "poder_ataque": poder_ataque,
        "poder_defensa": poder_defensa,
        "recursos_disponibles": recursos_disponibles,
        "poder_total": poder_total
    }