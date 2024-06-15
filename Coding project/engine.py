import pygame
from pygame.locals import KEYDOWN, KEYUP


def mp(file):  # 소리 파일을 불러 오는 파일을 불러오는 함수
    pygame.mixer.music.load(file)


white = (255, 255, 255)
black = (0, 0, 0)  # 색깔 RGB 지정

pygame.init()  # pygame 시작

Screen = pygame.display.set_mode((1000, 300))  # Screen Size 지정
pygame.display.set_caption("Mini Piano")
pygame.mouse.set_visible(1)  # 마우스 이동
Screen_font = pygame.font.Font(None, 30)  # 기본폰트, Size=30
text = (u"Press your Keyboard 'a, s, d, f, g, h, j, k' ")  # 상단 안내 문구
Screen_text = Screen_font.render(text, True, black)  # 텍스트 렌더링
Screen_text_vis = Screen_text.get_rect()  # 스크린에 텍스트 띄우기
Screen_text_vis_loc = (200, 10)  # 텍스트 위치 지정

Screen.fill(white)  # Screen 하얀색으로 채우기
Screen.blit(Screen_text, Screen_text_vis)  # Screen에 텍스트 표시

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
            pygame.mixer.music.play()

        if event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
