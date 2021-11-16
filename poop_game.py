#캐릭터는 좌우로만 움직인다. 맨 아래에 위치
#똥은 렌덤으로 맨 위에서 떨어진다.
#똥이 화면 밖으로 사라지면 다음 똥이 떨어진다.
#충돌시 종료된다.

import pygame
import random

#초기화, 필수작업
pygame.init() 

#화면 크기 설정
screen_width = 480
screen_height = 640

#캐릭터 이동 속도
speed = 0.6

#적 이동 속도
poop_speed = 0.6

#FPS (프레임 수)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height));

#화면 title
pygame.display.set_caption("나도 게임");

#배경 이미지 설정
background = pygame.image.load("D:/python_workspace/pythonGameProject/background.png");

# 캐릭터 불러오기(스프라이트)
character = pygame.image.load("D:/python_workspace/pythonGameProject/character.png");
character_size = character.get_rect().size #이미지의 크기
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height-character_height

#적 캐릭터
enemy = pygame.image.load("D:/python_workspace/pythonGameProject/poop.png");
enemy_size = enemy.get_rect().size #이미지의 크기
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, (screen_width-enemy_width))#screen_width/2-enemy_width/2
enemy_y_pos = 0

#이동할 좌표
to_x = 0
poop_to_y = 0;

# 이벤트 루프
running = True #게임이 진행중인가? 
while running:
    dt = clock.tick(30) #30프레임으로 설정(초당)
    #사용자의 키보드나 마우스의 움직임을 체크한다.
    for event in pygame.event.get(): 
        #종료 이벤트 발생시 while 문 종료 (우측의 X버튼) => 이 부분이 없는 경우는 창이 꺼지지 않아 작업관리자에서 종료해줘야함.
        if event.type == pygame.QUIT: 
           running = False 

        if event.type == pygame.KEYDOWN: #키 눌려짐 체크
            if event.key == pygame.K_LEFT: #왼쪽
                to_x -= speed
            elif event.key == pygame.K_RIGHT: #오른쪽
                to_x += speed
        
        if event.type == pygame.KEYUP: #키를 누르는 상태가 아닌경우 움직이지 않음
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #적이 자동으로 떨어진다.
    poop_to_y = poop_speed

    character_x_pos += to_x * dt
    enemy_y_pos += poop_to_y*dt

    #경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos >= (screen_width-character_width):
        character_x_pos = screen_width-character_width

    #충돌처리
    character_rect = character.get_rect();
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect();
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        running = False

    #만약, 적이 화면 밖으로 나가는 경우 적의 위치를 다시 설정한다.
    if enemy_y_pos >= (screen_height-enemy_height):
        enemy_x_pos = random.randrange(0, (screen_width-enemy_width))#screen_width/2-enemy_width/2
        enemy_y_pos = 0

    #배경 설정 (x, y좌표)
    screen.blit(background, (0,0))
    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    #적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #화면 새로 그리기 작업
    pygame.display.update();

#어디선가 종료된다면
pygame.quit()