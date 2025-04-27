from poder import OptimizadorPoder

def main():
    print("🚀 Simulación de Optimización Militar")

    # Datos de soldados
    soldados = [
        {"tipo": "arquero", "ataque": 3, "defensa": 2, "cantidad": 20},
        {"tipo": "espadachin", "ataque": 4, "defensa": 3, "cantidad": 15},
        {"tipo": "jinete", "ataque": 5, "defensa": 4, "cantidad": 10}
    ]

    # Datos de recursos
    recursos = [
        {"tipo": "comida", "cantidad": 100},
        {"tipo": "madera", "cantidad": 50},
        {"tipo": "oro", "cantidad": 30}
    ]

    # Crear optimizador y ejecutar cálculo
    optimizador = OptimizadorPoder(soldados, recursos)
    resultado = optimizador.calcular_optimizacion()

    print("\n✅ **Resultados de Optimización:**")
    for tipo, cantidad in zip([s["tipo"] for s in soldados], resultado["Cantidad óptima de soldados"]):
        print(f"{tipo}: {cantidad:.2f} soldados")

    # Generar gráficos
    optimizador.graficar_resultados()

if __name__ == "__main__":
    main()