import pygame
import sounddevice as sd
import numpy as np
import wave
import time
import ffmpeg

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("피아노")

# 피아노 키 설정
keys = [
    pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, 
    pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k
]

# 음 높이 (주파수) 설정
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

# 녹음 설정
recording = []
is_recording = False
start_time = None

# 소리 생성 함수
def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                index = keys.index(event.key)
                frequency = frequencies[index]
                if start_time is None:
                    start_time = time.time()
                
                current_time = time.time()
                if is_recording:
                    recording.extend(np.zeros(int(44100 * (current_time - start_time))))
                
                tone = generate_tone(frequency, 1.0)
                sd.play(tone, 44100)
                start_time = current_time
                is_recording = True
                recording.extend(tone)

        if event.type == pygame.KEYUP:
            if event.key in keys:
                sd.stop()
                start_time = time.time()

    screen.fill((255, 255, 255))
    pygame.display.flip()

# 녹음 데이터 배열로 변환
recording = np.array(recording)

# 녹음 데이터 wave 파일로 저장
with wave.open("recording.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    f.writeframes(recording.astype(np.int16).tobytes())

# wave 파일을 mp3 파일로 변환
ffmpeg.input('recording.wav').output('recording.mp3').run()

# pygame 종료
pygame.quit()
