from recursos.recursos import Recursos

def main():
    gestor_recursos = Recursos()
    print("🔹 Estado inicial de los recursos:")
    print(gestor_recursos.obtener_recursos())

    gestor_recursos.agregar_recurso("madera", 20)
    print("\n✅ Después de agregar 20 unidades de madera:")
    print(gestor_recursos.obtener_recursos())

    gestor_recursos.consumir_recurso("comida", 30)
    print("\n⚠️ Después de consumir 30 unidades de comida:")
    print(gestor_recursos.obtener_recursos())

if __name__ == "__main__":
    main()