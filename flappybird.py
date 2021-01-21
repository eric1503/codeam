import pygame, sys, random, time

pygame.init()

def draw_floor():
	screen.blit(floor_surface, (floor_x,850))
	screen.blit(floor_surface, (floor_x + 576,850))

def create_pipe():
	random_pipe = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe))
	top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe - 300))
	return bottom_pipe, top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 1024:
			screen.blit(pipe_surface,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)

def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			death_sound.play()
			hit_sound.play()

			can_score = True
			return False

		if bird_rect.top <= -100 or bird_rect.bottom >= 850:
			death_sound.play()
			can_score = True
			return False

	return True

def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement * 3,1)
	return new_bird 

def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
	return new_bird,new_bird_rect

def score_display(self):
	score_surface = game_font.render('Score',True,(255,255,255))
	score_rect = score_surface.get_rect(center = (288,100))
	screen.blit(score_surface,score_rect)

def pipe_score_check():
	global score, can_score

	if pipe_list:
		for pipe in pipe_list:
			if 95 < pipe.centerx < 105 and can_score:
				score += 1
				score_sound.play()
				can_score = False
			if pipe.centerx < 0:
				can_score = True
	
		




screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font(r'C:\Users\erica\Desktop\pybox\demoapp\04B_19.TTF',40)

gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
can_score = True
game_over_surface = pygame.transform.scale2x(pygame.image.load(r'C:\Users\erica\assets\message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))
flap_sound = pygame.mixer.Sound(r'C:\Users\erica\sound\sfx_wing.wav')
death_sound = pygame.mixer.Sound(r'C:\Users\erica\sound\sfx_hit.wav')
hit_sound = pygame.mixer.Sound(r'C:\Users\erica\sound\sfx_die.wav')
score_sound = pygame.mixer.Sound(r'C:\Users\erica\sound\sfx_point.wav')
score_sound_countdown = 100
# background
bg_surface = pygame.image.load(r'C:\Users\erica\assets\background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# floor
floor_surface = pygame.image.load(r'C:\Users\erica\assets\base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x = 0

bird_downflap = pygame.transform.scale2x(pygame.image.load(r'C:\Users\erica\assets\yellowbird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load(r'C:\Users\erica\assets\yellowbird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load(r'C:\Users\erica\assets\yellowbird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

#bird
#bird_surface = pygame.image.load(r'C:\Users\erica\assets\bluebird-midflap.png').convert_alpha()
#bird_surface = pygame.transform.scale2x(bird_surface)
#bird_rect = bird_surface.get_rect(center = (100,512))


#pipe
pipe_surface = pygame.image.load(r'C:\Users\erica\assets\pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface) 
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1500)
pipe_height = [450,500,550]

#gameloop
while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement -= 12
				flap_sound.play()
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,512)
				bird_movement = 0


		if event.type == BIRDFLAP:
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index = 0

			bird_surface,bird_rect = bird_animation()

		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())
    
	screen.blit(bg_surface, (0,0))


	if game_active:
    
	    # bird
		bird_movement += gravity
		rotated_bird = rotate_bird(bird_surface)
		bird_rect.centery += bird_movement
		screen.blit(rotated_bird, bird_rect)
		game_active = check_collision(pipe_list)
		
		# pipes
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)
		pipe_score_check()
		score += 0.01
		score_display('main_game')
	else:
		screen.blit(game_over_surface,game_over_rect)

		
		


	#floor
	floor_x -= 1
	draw_floor()
	if floor_x <= -576:
		floor_x = 0

	pygame.display.flip()
	clock.tick(120)




pygame.quit()