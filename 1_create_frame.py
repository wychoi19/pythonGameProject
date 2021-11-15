import pygame

#초기화, 필수작업
pygame.init() 

#화면 크기 설정
screen_width = 480
screen_height = 640

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

#이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True #게임이 진행중인가? 
while running:
    #사용자의 키보드나 마우스의 움직임을 체크한다.
    for event in pygame.event.get(): 
        #종료 이벤트 발생시 while 문 종료 (우측의 X버튼) => 이 부분이 없는 경우는 창이 꺼지지 않아 작업관리자에서 종료해줘야함.
        if event.type == pygame.QUIT: 
           running = False 

        if event.type == pygame.KEYDOWN: #키 눌려짐 체크
            if event.key == pygame.K_LEFT: #왼쪽
                to_x -= 0.5
            elif event.key == pygame.K_RIGHT: #오른쪽
                to_x += 0.5
            elif event.key == pygame.K_UP: #위
                to_y -= 0.5
            elif event.key == pygame.K_DOWN: #아래
                to_y += 0.5
        
        if event.type == pygame.KEYUP: #키를 누르는 상태가 아닌경우 움직이지 않음
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    #경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    if character_x_pos >= (screen_width-character_width):
        character_x_pos = screen_width-character_width
    if character_y_pos < 0 :
        character_y_pos = 0
    if character_y_pos >= (screen_height-character_height):
        character_y_pos = screen_height-character_height


    #배경 설정 (x, y좌표)
    screen.blit(background, (0,0))
    #캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    #화면 새로 그리기 작업
    pygame.display.update();

#어디선가 종료된다면
pygame.quit()