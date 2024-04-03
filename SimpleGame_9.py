import pygame


pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Animation')
clock = pygame.time.Clock()

player_stand_L = pygame.image.load('Characters/edited/L_Stand.png').convert_alpha()
player_L1 = pygame.image.load('Characters/edited/L1.png').convert_alpha()
player_L2 = pygame.image.load('Characters/edited/L2.png').convert_alpha()
player_L3 = pygame.image.load('Characters/edited/L3.png').convert_alpha()
player_L4 = pygame.image.load('Characters/edited/L4.png').convert_alpha()

player_stand_R = pygame.image.load('Characters/edited/R_Stand.png').convert_alpha()
player_R1 = pygame.image.load('Characters/edited/R1.png').convert_alpha()
player_R2 = pygame.image.load('Characters/edited/R2.png').convert_alpha()
player_R3 = pygame.image.load('Characters/edited/R3.png').convert_alpha()
player_R4 = pygame.image.load('Characters/edited/R4.png').convert_alpha()

player_L_head_down = pygame.image.load('Characters/edited/L_head_down.png').convert_alpha()
player_R_head_down = pygame.image.load('Characters/edited/R_head_down.png').convert_alpha()

player_L = [player_L1, player_L2, player_L3, player_L4]
player_R = [player_R1, player_R2, player_R3, player_R4]


player_rect = player_L[0].get_rect(midbottom = (400,500))
player_image = player_stand_L

index = 0

	
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		elif event.type == pygame.KEYUP:

			# When Left arrow key is released
			if event.key == pygame.K_LEFT:
				player_image = player_stand_L

			# When Right arrow key is released
			if event.key == pygame.K_RIGHT:
				player_image = player_stand_R

			# When Down arrow key is released
			if event.key == pygame.K_DOWN:
				# player's direction is 'left'
				if dir == 'left':
					player_image = player_stand_L

				# player's direction is 'right'
				else:
					player_image = player_stand_R
	
	keys = pygame.key.get_pressed()


	if keys[pygame.K_LEFT]:
		dir = 'left'
		index += 0.5
		if int(index) == index:
			player_rect.x -= 40
		if player_rect.centerx < 0:					# If character moving out left of display
			player_rect.centerx = display_width		# Put the character to the right edge of display
		if index > 3:
			index = 0
		player_image = player_L[int(index)]

	if keys[pygame.K_RIGHT]:
		dir = 'right'
		index += 0.5
		if int(index) == index:
			player_rect.x += 40
		if player_rect.centerx > display_width:		# If character moving out right of display
			player_rect.centerx = 0 				# Put the character to the left edge of display
		if index > 3:
			index = 0
		player_image = player_R[int(index)]

	# Down arrow key is pressed
	if keys[pygame.K_DOWN]:
		# player's direction is 'left'
		if dir == 'left':
			player_image = player_L_head_down

		# player's direction is not 'left'
		else:
			player_image = player_R_head_down 

	screen.fill('black')
	screen.blit(player_image, player_rect) 
	
	

	pygame.display.update()
	clock.tick(30)
	