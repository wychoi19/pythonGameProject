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

weapon_to_remove = -1
ball_to_remove = -1

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
    "init_spd_y":ball_speed_y[0] #최초 속도 선택 
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

    ################################# 화면에 그리기 #########################################
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        print(weapon, weapon_x_pos, weapon_y_pos)
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    ################################## 충돌 처리 ##########################################

    # 캐릭터와 공
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running=False
            break

        #무기들과 공
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                #충돌시 무기와 공 제거.
                weapon_to_remove = weapon_idx
                ball_to_remove = idx
                break
    
    #충돌된 아이템 제거
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    
    ################################## 무기 이동 ##########################################
    #무기 이동
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 무기가 화면을 벗어나면 사라지게
    weapons = [[w[0], w[1]] for w in weapons if w[1]>0 ]

    ################################## 공 이동 ##########################################
    for ball_idx, ball_val in enumerate(balls): #키 값을 세트로 추출하는 구문
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #공의 경계값 처리 (튕겨나가야한다) -> 좌우
        if ball_pos_x < 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"]*-1
        #공의 경계값 처리 (튕겨나가야한다) -> 스테이지에 튕김
        if ball_pos_y > screen_height-stage_height-ball_width:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else :
            ball_val["to_y"] += 0.5
        # 스테이지에서 튕겨 올라오는건 최초 속도 / 그리고 중력의 영향을 받아 속도가 준다. 
        # 내려올때는 다시 속도를 증가하여 가속도를 표시한다.
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]


    #화면 새로 그리기 작업
    pygame.display.update();

#어디선가 종료된다면
pygame.quit()