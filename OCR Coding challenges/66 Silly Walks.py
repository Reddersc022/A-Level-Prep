import pygame
import random

print("*** Silly Walks ***")

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
coords = [200, 150]

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	coords[0] += random.choice([-1, 1])
	coords[1] += random.choice([-1, 1])

	if coords[0] < 0:
		coords[0] = 0
	elif coords[0] > 400:
		coords[0] = 400

	if coords[1] < 0:
		coords[1] = 0
	elif coords[1] > 300:
		coords[1] = 300

	pygame.draw.circle(screen, (255, 255, 255), coords, 2)

	pygame.display.flip()
