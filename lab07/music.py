import pygame # type: ignore
import os

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Плеер")
music_directory = "C:\pp2\lab07\music"
os.chdir(music_directory)

music_files = [file for file in os.listdir() if file.endswith(".mp3")]

current_track = 0
paused = False

pygame.mixer.music.load(music_files[current_track])

font = pygame.font.Font(None, 24)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
    
    screen.fill((255, 255, 255))
    instructions = font.render("Spacebar: Play/Pause, Left Arrow: Previous, Right Arrow: Next", True, (0, 0, 0))
    screen.blit(instructions, (20, 10))
    font = pygame.font.Font(None, 36)
    text_lines = [
        "Songs:",
        "1. Lady Gaga feat. Bruno Mars - Die With A Smile", 
        "2. Playboi Carti - Fell In Luv (feat. Bryson Tiller)",
        "3. Jay-Z - 4:44"
    ]
    for i, line in enumerate(text_lines):
        text = font.render(line, True, (52, 52, 52))
        screen.blit(text, (20, 30 * i + 50))
    pygame.display.flip()

    pygame.display.flip()

pygame.quit()