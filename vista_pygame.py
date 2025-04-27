import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("🏰 Estrategia de Recursos y Soldados")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Clase de soldados (representados con cuadrados)
class Soldado:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 5
        self.tamaño = 40

    def mover(self, direccion):
        if direccion == "izquierda" and self.x > 0:
            self.x -= self.velocidad
        elif direccion == "derecha" and self.x < ANCHO - self.tamaño:
            self.x += self.velocidad
        elif direccion == "arriba" and self.y > 0:
            self.y -= self.velocidad
        elif direccion == "abajo" and self.y < ALTO - self.tamaño:
            self.y += self.velocidad

    def dibujar(self):
        pygame.draw.rect(VENTANA, AZUL, (self.x, self.y, self.tamaño, self.tamaño))

# Instancia de soldados
soldados = [Soldado(random.randint(100, 700), random.randint(100, 500)) for _ in range(5)]

# Loop del juego
ejecutando = True
while ejecutando:
    VENTANA.fill(NEGRO)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                for soldado in soldados:
                    soldado.mover("izquierda")
            elif evento.key == pygame.K_RIGHT:
                for soldado in soldados:
                    soldado.mover("derecha")
            elif evento.key == pygame.K_UP:
                for soldado in soldados:
                    soldado.mover("arriba")
            elif evento.key == pygame.K_DOWN:
                for soldado in soldados:
                    soldado.mover("abajo")

    # Dibujar soldados en pantalla
    for soldado in soldados:
        soldado.dibujar()

    pygame.display.flip()

pygame.quit()