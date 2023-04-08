import pygame
import random

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

tamanho = (800, 600)

tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Quer namorar comigo?")

sim_imagem = pygame.image.load("sim.png").convert()
nao_imagem = pygame.image.load("nao.png").convert()

sim_posicao = (200, 200)
nao_posicao = (400, 200)

botao_largura = 150
botao_altura = 150

movimento = 20

fonte = pygame.font.SysFont(None, 48)

feito = False
while not feito:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            feito = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if sim_rect.collidepoint(pos):
                sim_press_botao = pygame.image.load("fotonossa.png").convert() #Não disponibilizar a foto no Github
                sim_press_botao = pygame.transform.scale(sim_press_botao, tamanho)
                tela_cheia = pygame.display.set_mode(tamanho, pygame.FULLSCREEN)
                tela_cheia.blit(sim_press_botao, [0,0])
                pygame.display.flip()
                while True:
                    for evento2 in pygame.event.get():
                        if evento2.type == pygame.KEYDOWN and evento2.key == pygame.K_ESCAPE:
                            tela_cheia = pygame.display.set_mode(tamanho)
                            pygame.display.flip()
                            break
                        elif evento2.type == pygame.QUIT:
                            pygame.quit()
                            quit()
            elif nao_rect.collidepoint(pos):
                nao_posicao = (random.randint(botao_largura, tamanho[0]-botao_largura), random.randint(botao_altura, tamanho[1]-botao_altura))
                nao_rect = tela.blit(nao_imagem, nao_posicao)


    fundo_imagem = pygame.image.load("fundo6.png").convert()
    tela.blit(fundo_imagem, [0, 0])


    sim_rect = tela.blit(sim_imagem, sim_posicao)
    nao_rect = tela.blit(nao_imagem, nao_posicao)


    if nao_rect.right > tamanho[0] - botao_largura or nao_rect.left < botao_largura or nao_rect.bottom > tamanho[
        1] - botao_altura or nao_rect.top < botao_altura:
        nao_posicao = (random.randint(botao_largura, tamanho[0] - botao_largura),
                       random.randint(botao_altura, tamanho[1] - botao_altura))
        nao_rect = tela.blit(nao_imagem, nao_posicao)


    pygame.display.flip()

pygame.quit()





