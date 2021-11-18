import pygame
import os

##############################변수 선언 및 초기화#############################
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


################################게임 설정########################################
current_path = os.path.dirname(__file__) #현재 경로 반환

#배경 이미지 설정
background = pygame.image.load(current_path+"/img/background1.png");

#스테이지 설정
stage = pygame.image.load(current_path+"/img/stage.png");
stage_height = stage.get_rect().size[1]; #캐릭터 위치 설정을 위해


#############################캐릭터 불러오기(스프라이트)#############################
character = pygame.image.load(current_path+"/img/character1.png");
character_size = character.get_rect().size #이미지의 크기
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height-character_height-stage_height
#캐릭터 이동 속도
speed = 5

#이동할 좌표
to_x = 0


#################################무기 만들기#########################################
weapon = pygame.image.load(current_path+"/img/weapon.png");
weapon_size = weapon.get_rect().size #이미지의 크기
weapon_width = weapon_size[0] 
#무기는 연속 발사 가능
weapons = []
#무기 속도
weapon_speed = 10

#################################공 만들기(4개)###########################################
ball_images = [
    pygame.image.load(current_path+"/img/balloon1.png"),
    pygame.image.load(current_path+"/img/balloon2.png"),
    pygame.image.load(current_path+"/img/balloon3.png"),
    pygame.image.load(current_path+"/img/balloon4.png")
]
#공의 크기에 따른 속도차이가 있음
ball_speed_y = [-18, -15, -12, -9]
#공 정보
balls = []
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0, #어떤 공을 사용할지?
    "to_x":3,
    "to_y":-6,
    "init_spd_y":0 #최초 속도 선택 
})
#################################이벤트 루프#########################################

running = True 
while running:
    dt = clock.tick(30)
    ################################# 키보드 이벤트 #########################################
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #윈도우 기준 우측 상단 X 버튼을 눌렀을 경우
           running = False 

        if event.type == pygame.KEYDOWN: #키 눌려짐 체크
            if event.key == pygame.K_LEFT: #왼쪽
                to_x -= speed
            elif event.key == pygame.K_RIGHT: #오른쪽
                to_x += speed
            elif event.key == pygame.K_SPACE: #무기 발사
                weapon_x_pos = character_x_pos+(character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos]) #리스트에 저장함.
        if event.type == pygame.KEYUP: #키를 누르는 상태가 아닌경우 움직이지 않음
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    ################################## 위치 적용 ##########################################
    #캐릭터 위치 설정
    character_x_pos += to_x

    #경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos >= (screen_width-character_width):
        character_x_pos = screen_width-character_width

    ################################## 충돌 처리 ##########################################

    ################################# 화면에 그리기 #########################################
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        print(weapon, weapon_x_pos, weapon_y_pos)
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    ################################## 무기 이동 ##########################################
    #무기 이동
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 무기가 화면을 벗어나면 사라지게
    weapons = [[w[0], w[1]] for w in weapons if w[1]>0 ]

    #화면 새로 그리기 작업
    pygame.display.update();

#어디선가 종료된다면
pygame.quit()