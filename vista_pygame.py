import pygame
import random
from recursos.recursos import Recursos
from soldados.recursos import Soldados

# Configuración inicial
pygame.init()
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🏰 Gestión de Recursos y Soldados")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Instancia de gestión
gestor_recursos = Recursos()
gestor_soldados = Soldados()

# Carga de fuentes
fuente = pygame.font.Font(None, 36)

# Loop principal
ejecutando = True
while ejecutando:
    VENTANA.fill(NEGRO)

    # Mostrar recursos
    recursos_actuales = gestor_recursos.obtener_recursos()
    y_offset = 50
    for index, recurso in recursos_actuales.iterrows():
        texto = fuente.render(f"{recurso['tipo']}: {recurso['cantidad']}", True, VERDE)
        VENTANA.blit(texto, (50, y_offset))
        y_offset += 40

    # Mostrar soldados
    soldados_actuales = gestor_soldados.obtener_soldados()
    y_offset = 50
    for index, soldado in soldados_actuales.iterrows():
        texto = fuente.render(f"{soldado['tipo']} | Atq: {soldado['ataque']} | Def: {soldado['defensa']} | Cantidad: {soldado['cantidad']}", True, ROJO)
        VENTANA.blit(texto, (400, y_offset))
        y_offset += 40

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                gestor_recursos.agregar_recurso("comida", random.randint(5, 20))
                gestor_recursos.agregar_recurso("madera", random.randint(3, 15))
                gestor_recursos.agregar_recurso("oro", random.randint(1, 10))
            elif evento.key == pygame.K_s:
                gestor_soldados.reclutar_soldado("arquero", 3, 2, random.randint(1, 5))
                gestor_soldados.reclutar_soldado("espadachin", 4, 3, random.randint(1, 5))
                gestor_soldados.reclutar_soldado("jinete", 5, 4, random.randint(1, 5))

    pygame.display.flip()
pygame.quit()