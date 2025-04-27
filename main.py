from optimizador import OptimizadorPoder

def graficar_resultados(soldados, resultado):
    tipos = [s["tipo"] for s in soldados]
    cantidades_optimas = resultado["Cantidad óptima de soldados"]

    plt.bar(tipos, cantidades_optimas, color=['blue', 'green', 'red'])
    plt.xlabel("Tipo de Soldado")
    plt.ylabel("Cantidad Optimizada")
    plt.title("Distribución Óptima de Soldados")
    plt.show()

def main():
    soldados = [
        {"tipo": "arquero", "ataque": 3, "defensa": 2, "cantidad": 20},
        {"tipo": "espadachin", "ataque": 4, "defensa": 3, "cantidad": 15},
        {"tipo": "jinete", "ataque": 5, "defensa": 4, "cantidad": 10}
    ]

    recursos = [
        {"tipo": "comida", "cantidad": 100},
        {"tipo": "madera", "cantidad": 50},
        {"tipo": "oro", "cantidad": 30}
    ]

    optimizador = OptimizadorPoder(soldados, recursos)
    resultado = optimizador.calcular_optimizacion()

    print("\n✅ **Resultados de Optimización:**")
    for tipo, cantidad in zip([s["tipo"] for s in soldados], resultado["Cantidad óptima de soldados"]):
        print(f"{tipo}: {cantidad:.2f} soldados")

    graficar_resultados(soldados, resultado)

if __name__ == "__main__":
    main()