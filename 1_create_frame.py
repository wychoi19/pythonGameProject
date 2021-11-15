import pygame

pygame.init() #초기화, 무조건

#화면 크기 설정
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height));

#화면 title
pygame.display.set_caption("나도 게임");

#배경 이미지 설정
background = pygame.image.load("D:/python_workspace/pythonGameProject/background.png");

#배경 설정 (x, y좌표)
screen.blit(background, (0,0))
#또는 배경이미지 대신 색으로 설정
#screen.fill((255,0,0))
#화면 새로 그리기 작업
pygame.display.update();

# 이벤트 루프
running = True #게임이 진행중인가? 
while running:
    #사용자의 키보드나 마우스의 움직임을 체크한다.
    for event in pygame.event.get(): 
        #종료 이벤트 발생시 while 문 종료 (우측의 X버튼) => 이 부분이 없는 경우는 창이 꺼지지 않아 작업관리자에서 종료해줘야함.
        if event.type == pygame.QUIT: 
           running = False 

#어디선가 종료된다면
pygame.quit()