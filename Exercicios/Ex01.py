#Bibliotecas necessárias para o funcionamento do código
#Caso seja necessário instalar, utilize o terminal e em seguida digite: pip install glfw, pip install PyOpenGL e PyOpenGL_accelerate
import glfw
from OpenGL.GL import *


#Função do desenho
def desenhoOculos():
    #É necessário utilizar o glClear() para limpar o buffer e não ocorrer nenhum problema na hora de desenhar alguma coisa na tela.
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(255, 255, 255, 0)
    glPointSize(15.0)

    glBegin(GL_POINTS)
    glColor3f(0, 0, 0) #Alterar para preto
    glVertex2f(-0.00, 0.05)
    glVertex2f(-0.05, 0.05)
    glVertex2f(-0.1, 0.05)
    glVertex2f(-0.15, 0.05)
    glVertex2f(-0.2, 0.05)
    glVertex2f(-0.25, 0.05)
    glVertex2f(-0.3, 0.05)
    glVertex2f(-0.35, 0.05)
    glVertex2f(-0.4, 0.05)
    glVertex2f(-0.45, 0.05)
    glVertex2f(0.00, 0.05)
    glVertex2f(0.05, 0.05)
    glVertex2f(0.1, 0.05)
    glVertex2f(0.15, 0.05)
    glVertex2f(0.2, 0.05)
    glVertex2f(0.25, 0.05)
    glVertex2f(0.3, 0.05)
    glVertex2f(0.35, 0.05)
    glVertex2f(0.4, 0.05)
    glVertex2f(0.45, 0.05)
    glVertex2f(0.5, 0.05)
    glVertex2f(0.55, 0.05)
    glVertex2f(0.6, 0.05)
    glVertex2f(0.65, 0.05)
    glEnd()


    glBegin(GL_POINTS) #Primeira linha de pixels
    glVertex2f(0.70, -0.00)
    glVertex2f(0.75, -0.00)
    glVertex2f(0.80, -0.00)
    
    glVertex2f(0.40, -0.00)
    glVertex2f(0.35, -0.00)
    glVertex2f(0.30, -0.00)
    glVertex2f(0.25, -0.00)
    glVertex2f(0.20, -0.00)
    glVertex2f(0.15, -0.00)
    glVertex2f(0.10, -0.00)
    glVertex2f(0.05, -0.00)

    glVertex2f(-0.10, -0.00)
    glVertex2f(-0.15, -0.00)
    glVertex2f(-0.20, -0.00)
    glVertex2f(-0.25, -0.00)
    glVertex2f(-0.30, -0.00)
    glVertex2f(-0.35, -0.00)
    glVertex2f(-0.40, -0.00)
    glVertex2f(-0.45, -0.00)
    glEnd()

    glBegin(GL_POINTS) #Segunda linha de pixels
    glVertex2f(0.35, -0.05)
    glVertex2f(0.30, -0.05)
    glVertex2f(0.25, -0.05)
    glVertex2f(0.20, -0.05)
    glVertex2f(0.15, -0.05)
    glVertex2f(0.10, -0.05)
    glVertex2f(0.05, -0.05)
 
    glVertex2f(-0.10, -0.05)
    glVertex2f(-0.15, -0.05)
    glVertex2f(-0.20, -0.05)
    glVertex2f(-0.25, -0.05)
    glVertex2f(-0.30, -0.05)
    glVertex2f(-0.35, -0.05)
    glVertex2f(-0.40, -0.05)
    glEnd()

    glBegin(GL_POINTS) #Terceira linha de pixels
    glVertex2f(0.30, -0.10)
    glVertex2f(0.25, -0.10)
    glVertex2f(0.20, -0.10)
    glVertex2f(0.15, -0.10)
    glVertex2f(0.10, -0.10)

    glVertex2f(-0.15, -0.10)
    glVertex2f(-0.20, -0.10)
    glVertex2f(-0.25, -0.10)
    glVertex2f(-0.30, -0.10)
    glVertex2f(-0.35, -0.10)

    glEnd()

#Função para abrir a janela
def main():
    #glfw.init() inicializa o GLFW, biblioteca que gerencia janelas, entradas e contextos OpenGL
    #Se, por acaso, a inicialização do GLFW falhar, o programa será encerrado imediatamente, sem criar a janela e executar as outras funções.
    if not glfw.init():
        return False

    #Aqui é onde foi criada a resolução da janela do desenho, possuindo como parâmetros a largura, altura, o nome da janela, e os outros 2 parâmetros que estão classificados como "None" funcionariam para alterar entre telas fullscreen ou não e compartilhamento de objetos, vértices, etc.
    window = glfw.create_window(700, 700, "Ex1 - Computação Gráfica", None, None)
    #Verificação se a janela foi criada efetivamente, caso contrário o programa encerra imediatamente
    if not window:
        glfw.terminate()
        return

    #Essa linha vai definir a janela criada como a janela atual do contexto OpenGL, caso não exista essa função, é impossível da janela ser aberta
    glfw.make_context_current(window)

    #Aqui é o loop principal do programa, onde o loop será executado enquanto a janela não estiver fechada pelo usuário.
    while not glfw.window_should_close(window):

        # Esta linha processa eventos de entrada, como movimentos do mouse e teclas pressionadas. Ou seja, caso essa função não esteja no programa, a janela irá abrir, porém não sera possível fechar, irá acontecer um erro e começará a não responder
        glfw.poll_events()

        #A chamada da função para renderizar a imagem na janela, a imagem é desenhada na memória GPU e ainda não aparece na janela.
        desenhoOculos()

        #Esta linha troca os buffers de cor da janela. Essa operação mostra a imagem renderizada na janela, tornando-a visível para o usuário. Ou seja, sem essa função, a janela abre, porém não irá aparecer nada além de uma tela branca com o título e sua resolução.
        glfw.swap_buffers(window)

    glfw.terminate()

#Essa linha é uma verificação condicional que verifica se o nome do módulo em que o código está sendo executado é igual a "__main__". Quando um módulo é importado em outro programa Python, o nome do módulo não é "__main__". No entanto, quando um script é executado diretamente (por exemplo, com o comando python nome_do_script.py), o nome do módulo é definido como "__main__".
if __name__ == "__main__":
    main()
