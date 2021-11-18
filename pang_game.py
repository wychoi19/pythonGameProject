import pygame
import os

# 변수 선언 및 초기화
####################################################
#초기화, 필수작업
pygame.init() 

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height));

#화면 title
pygame.display.set_caption("Pang 게임");

#FPS (프레임 수)
clock = pygame.time.Clock()

# 게임 설정
####################################################

current_path = os.path.dirname(__file__) #현재 경로 반환

#배경 이미지 설정
background = pygame.image.load(current_path+"/img/background1.png");

#스테이지 설정
stage = pygame.image.load(current_path+"/img/stage.png");
stage_height = stage.get_rect().size[1]; #캐릭터 위치 설정을 위해

# 캐릭터 불러오기(스프라이트)
character = pygame.image.load("D:/python_workspace/pythonGameProject/img/character1.png");
character_size = character.get_rect().size #이미지의 크기
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height-character_height-stage_height

#캐릭터 이동 속도
speed = 0.6

#이동할 좌표
to_x = 0
to_y = 0

#폰트 정의
game_font = pygame.font.Font(None, 40)

#총 시간 표시
total_time = 10
#시간 계산
start_ticks = pygame.time.get_ticks() #현재 tick

# 이벤트 루프
running = True #게임이 진행중인가? 
while running:
    dt = clock.tick(60) #30프레임으로 설정(초당)
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
            elif event.key == pygame.K_UP: #위
                to_y -= speed
            elif event.key == pygame.K_DOWN: #아래
                to_y += speed
        
        if event.type == pygame.KEYUP: #키를 누르는 상태가 아닌경우 움직이지 않음
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos >= (screen_width-character_width):
        character_x_pos = screen_width-character_width
    if character_y_pos < 0 :
        character_y_pos = 0
    if character_y_pos >= (screen_height-character_height):
        character_y_pos = screen_height-character_height

    #충돌처리
    character_rect = character.get_rect();
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    #배경 설정 (x, y좌표)
    screen.blit(background, (0,0))
    #배경 설정 (x, y좌표)
    screen.blit(stage, (0,screen_height-stage_height))
    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    #타이머 추가 (경과 시간 계산)
    elapse_time = (pygame.time.get_ticks() - start_ticks)/1000 #단위가 밀리초

    #초 기준 역순으로 숫자가 출력되게 만든다.
    timer = game_font.render(str(int(total_time-elapse_time)), True, (255,255,255))

    #시간정보 그리기
    screen.blit(timer, (10,10))

    if total_time-elapse_time < 0:
        running = False

    #화면 새로 그리기 작업
    pygame.display.update();

#어디선가 종료된다면
pygame.quit()