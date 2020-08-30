import pygame
import random

print("*** Galaxy Song ***")

pygame.init()
screen = pygame.display.set_mode((400, 300))
done, drawn = False, False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	if not drawn:
		for _ in range(10, random.randint(20, 40)):
			coords = (random.randint(1, 400), random.randint(1, 300))
			pygame.draw.circle(screen, (255, 255, 255), coords, 1)
		drawn = True

	pygame.display.flip()
