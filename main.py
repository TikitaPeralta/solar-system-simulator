import pygame, sys, math


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1900, 900
SCREEN_CENTER = SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
BLACK = (0,0,0)
WHITE = (255,255,255) 


def linelength(pos1, pos2): # planet_center, planet_surface
    x1, y1 = pos1
    x2, y2 = pos2
    x_squared = ( x2 - x1 ) * ( x2 - x1 )
    y_squared = ( y2 - y1 ) * ( y2 - y1 )
    length = math.sqrt( x_squared + y_squared )
    return length



def store_planet_info():
    planet_store = {1 : {'planet_name': 'mercury', 'radius': 5, 'orbit_radius': 100, 'color': (150,75,0)},
                    2 : {'planet_name': 'venus', 'radius': 10, 'orbit_radius': 150, 'color': (124,252,0)},
                    3 : {'planet_name': 'earth', 'radius': 10, 'orbit_radius': 200, 'color': (0,0,255)},
                    4 : {'planet_name': 'mars', 'radius': 7, 'orbit_radius': 250, 'color': (255,0,0)},
                    5 : {'planet_name': 'jupiter', 'radius': 50, 'orbit_radius': 400, 'color': (255,165,0)},
                    6 : {'planet_name': 'saturn', 'radius': 30, 'orbit_radius': 500, 'color': (255,255,0)},
                    7 : {'planet_name': 'uranus', 'radius': 20, 'orbit_radius': 600, 'color': (0,191,255)},
                    8 : {'planet_name': 'neptune', 'radius': 20, 'orbit_radius': 700, 'color': (221,160,221)}}
    return planet_store

# mass of sun: 20 x 10 e29 kg
# mercury : 6 x 10 e7 km
# venus : 10 x 10 e7
# earth : 15 x 10 e 7
# mars : 25 x 10 e 7
# jupiter: 74 x 10 e 7
# saturn : 146 x 10 e 7
# neptune : 447 x 10 e 7
# sun -> uranus : 294 x 10 e7 km


def compute_planet_center(orbit_radius):
    time_seconds = pygame.time.get_ticks()
    sun_mass = 200000000000000000000000
    grav_const = 0.00000000000000000667408
    time_period = (math.sqrt(((orbit_radius**3)*4*(math.pi**2)) / (grav_const * sun_mass)))*time_seconds
    current_time_milliseconds_as_fraction = time_period/100000.0
    PLANET_X = SCREEN_WIDTH_CENTER + (math.sin(current_time_milliseconds_as_fraction) * orbit_radius)
    PLANET_Y = SCREEN_HEIGHT_CENTER + (math.cos(current_time_milliseconds_as_fraction) * orbit_radius)
    return PLANET_X, PLANET_Y


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    running = True
    Clock = pygame.time.Clock()
    fontIntro = pygame.font.SysFont("arial", 30)

    while running:
        Clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

        screen.fill(BLACK)
        sun = pygame.draw.circle(screen, WHITE, SCREEN_CENTER, 20)


        planet_info = store_planet_info()

        for planet_id, planet in planet_info.items():
            planet_name = planet['planet_name']
            orbit_radius = planet['orbit_radius']
            planet_color = planet['color']
            planet_radius = planet['radius']
            planet_center = compute_planet_center(orbit_radius)
            posX, posY = planet_center
            planet_surface = posX - planet_radius, posY - planet_radius
            pygame.draw.circle(screen, planet_color, planet_center, planet_radius)
            click = pygame.mouse.get_pos()
            if linelength(planet_surface, planet_center) > linelength(planet_center, click):
                text = fontIntro.render(planet_name, 1, WHITE)
                screen.blit(text, (10,10,500,200))


        pygame.display.flip()


if __name__ == "__main__":
    main()