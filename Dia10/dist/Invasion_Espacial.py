import pygame
import random
import math
from pygame import mixer
import io



#Convertir strings en bytes para exportar las fuentes
def cargar_fuente_bytes(fuente, fuente_final):
    with open(fuente, 'rb') as f:
        ttf_bytes1 = f.read()
    with open(fuente_final, 'rb') as f2:
        ttf_bytes2 = f2.read()
    return io.BytesIO(ttf_bytes1), io.BytesIO(ttf_bytes2)


# Inicializar Pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))


#Titulo e Icono
pygame.display.set_caption("Space Invaders || Marcianitos")
icon = pygame.image.load("ovni .png")
pygame.display.set_icon(icon)
fondo = pygame.image.load("Fondo.jpg")

#Agregar música
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)




#Variables del Jugador
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#Variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for n in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

#Variables de la Bala
balas= []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False


#Puntuación
puntuacion = 0
fuente_bytes, fuente_final_bytes = cargar_fuente_bytes('f2-tecnocratica-ffp.ttf', 'Fastest.ttf')
fuente = pygame.font.Font(fuente_bytes, 30)
fuente_final = pygame.font.Font(fuente_final_bytes, 40)
texto_x = 10
texto_y = 10

#Texto final de juego
#fuente_final = pygame.font.Font('Fastest.ttf', 40)



#Mostrar Puntuacion
def mostrar_puntuacion(x, y):
    texto = fuente.render(f"Puntuación  {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

#Función Jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))


#Función Enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x,y))

#Función Bala
def disparar_bala(x,y) :
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#Funcion detectar colisiones
def hay_colision(x_1, x_2, y_1, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

#Funcion fin del juego
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (120, 200))


#Loop del juego
se_ejecuta = True
while se_ejecuta:

    #Pantalla RGB
    #pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0,0))

    #iterar eventos
    for event in pygame.event.get():
        #evento presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.2
            if event.key == pygame.K_SPACE:
                if len(balas) == 0 or balas[-1]['y'] < jugador_y - 50:  # Esto evita disparar muchas balas demasiado rápido
                    sonido_bala = mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    nueva_bala = {
                        "x": jugador_x,
                        "y": jugador_y,
                        "velocidad": -3
                    }
                    balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #evento soltar tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0


        #evento cerrar
        if event.type == pygame.QUIT:
            se_ejecuta = False

    #modificar ubicación jugador
    jugador_x += jugador_x_cambio

    #modificar ubicación enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]
        # mantener dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        # Verificacion Colision
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], bala["x"], enemigo_y[e],  bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntuacion += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break
        enemigo(enemigo_x[e], enemigo_y[e], e)

    #mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736


    #movimiento de la Bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 3))
        if bala["y"] < 0:
            balas.remove(bala)
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    #mostrar Puntuacion
    mostrar_puntuacion(texto_x, texto_y)
    #actualizar
    pygame.display.update()
