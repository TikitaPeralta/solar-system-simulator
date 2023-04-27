import pygame, sys, math


SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1900, 900
SCREEN_CENTER = SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
BLACK = (0,0,0)
WHITE = (255,255,255) 

def linelength(pos1, pos2):
    pass


def store_planet_info():
    planet_store = {1 : {'planet_name': 'mercury', 'radius': 5, 'orbit_radius': 100, 'color': (150,75,0)},
                    2 : {'planet_name': 'venus', 'radius': 10, 'orbit_radius': 150, 'color': (124,252,0)},
                    3 : {'planet_name': 'earth', 'radius': 10, 'orbit_radius': 200, 'color': (0,0,255)},
                    4 : {'planet_name': 'mars', 'radius': 7, 'orbit_radius': 250, 'color': (255,0,0)},
                    5 : {'planet_name': 'jupiter', 'radius': 50, 'orbit_radius': 400, 'color': (255,165,0)},
                    6 : {'planet_name': 'saturn', 'radius': 30, 'orbit_radius': 500, 'color': (255,255,0)},
                    7 : {'planet_name': 'uranus', 'radius': 20, 'orbit_radius': 600, 'color': (0,191.255)},
                    8 : {'planet_name': 'neptune', 'radius': 20, 'orbit_radius': 700, 'color': (221,160,221)}}
    return planet_store

    

def compute_planet_center(current_time, orbit_radius):
    current_time_milliseconds_as_fraction = current_time/1000.0
    PLANET_X = SCREEN_WIDTH_CENTER + (math.sin(current_time_milliseconds_as_fraction) * orbit_radius)
    PLANET_Y = SCREEN_HEIGHT_CENTER + (math.cos(current_time_milliseconds_as_fraction) * orbit_radius)
    return PLANET_X, PLANET_Y


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    running = True
    Clock = pygame.time.Clock()

    while running:
        Clock.tick(60)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()

        screen.fill(BLACK)
        sun = pygame.draw.circle(screen, WHITE, SCREEN_CENTER, 120)


        planet_info = store_planet_info()
        i = 0
        while i < 9:
            for planet_id, planet in planet_info.items():
                planet_name = planet['planet_name']
                orbit_radius = planet['orbit_radius']
                planet_color = planet['color']
                planet_radius = planet['radius']
                planet_center = compute_planet_center(current_time, orbit_radius)
                partX, partY = planet_center
                linelength(partX, partY)
                pygame.draw.circle(screen, WHITE, planet_center, planet_radius)
                i += 1


        pygame.display.flip()


if __name__ == "__main__":
    main()