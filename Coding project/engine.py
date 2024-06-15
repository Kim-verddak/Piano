import pygame
from pygame.locals import KEYDOWN, KEYUP


def mp(file):  # 소리 파일을 불러 오는 파일을 불러오는 함수
    pygame.mixer.music.load(file)
    return
    
image = pygame.image.load('bakground.png')
white = (255, 255, 255)
black = (0, 0, 0)  # 색깔 RGB 지정

pygame.init()  # pygame 시작

Screen = pygame.display.set_mode((1200, 670))  # Screen Size 지정
pygame.display.set_caption("작은 오케스트라")
pygame.mouse.set_visible(1)  # 마우스 이동
Screen_font = pygame.font.Font(None, 30)  # 기본폰트, Size=30
text = (u"Press your Keyboard 'a, s, d, f, g, h, j, k' ")  # 상단 안내 문구
Screen_text = Screen_font.render(text, True, black)  # 텍스트 렌더링
Screen_text_vis = Screen_text.get_rect()  # 스크린에 텍스트 띄우기
Screen_text_vis_loc = (200, 10)  # 텍스트 위치 지정

Screen.fill(white)  # Screen 하얀색으로 채우기
Screen.blit(Screen_text, Screen_text_vis)  # Screen에 텍스트 표시
Screen.blit(image, (0, 0))
running = True
while running:
    pygame.display.update()  # display를 계속 업데이트 한다.

    for event in pygame.event.get():  # 이벤트 시작

        if event.type == pygame.QUIT:  # 탈출조건 실행
            running = False

        if event.type == KEYDOWN:
            if event.key == pygame.K_a:
                mp("audio/FX_piano01.mp3")
            if event.key == pygame.K_s:
                mp("audio/FX_piano03.mp3")
            if event.key == pygame.K_d:
                mp("audio/FX_piano05.mp3")
            if event.key == pygame.K_f:
                mp("audio/FX_piano06.mp3")
            if event.key == pygame.K_g:
                mp("audio/FX_piano08.mp3")
            if event.key == pygame.K_h:
                mp("audio/FX_piano10.mp3")
            if event.key == pygame.K_j:
                mp("audio/FX_piano12.mp3")
            if event.key == pygame.K_k:
                mp("audio/FX_piano13.mp3")
            if event.key == pygame.K_k:
                mp("audio/FX_piano13.mp3")
            if event.key == pygame.K_q:
                mp("audio/HaeGeumC3.wav")
            if event.key == pygame.K_w:
                mp("audio/HaeGeumDb3.wav")
            if event.key == pygame.K_e:
                mp("audio/HaeGeumEb3.wav")
            if event.key == pygame.K_r:
                mp("audio/HaeGeumF3.wav")
            if event.key == pygame.K_t:
                mp("audio/HaeGeumG3.wav")
            if event.key == pygame.K_y:
                mp("audio/HaeGeumAb3.wav")
            if event.key == pygame.K_z:
                mp("audio/HarpC1.wav")
            if event.key == pygame.K_x:
                mp("audio/HarpD1.wav")
            if event.key == pygame.K_c:
                mp("audio/HarpE1.wav")
            if event.key == pygame.K_v:
                mp("audio/HarpF1.wav")
            if event.key == pygame.K_b:
                mp("audio/HarpG1.wav")
            if event.key == pygame.K_n:
                mp("audio/HarpA1.wav")
            if event.key == pygame.K_1:
                mp("audio/RecorderC3.wav")
            if event.key == pygame.K_4:
                mp("audio/RecorderD4.wav")
            if event.key == pygame.K_5:
                mp("audio/RecorderE4.wav")
            if event.key == pygame.K_6:
                mp("audio/RecorderF4.wav")
            if event.key == pygame.K_7:
                mp("audio/RecorderG4.wav")
            if event.key == pygame.K_2:
                mp("audio/RecorderA3.wav")
            if event.key == pygame.K_3:
                mp("audio/RecorderB3.wav")
            if event.key == pygame.K_SPACE:
                mp("audio/book.wav")
            pygame.mixer.music.play()

        if event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
