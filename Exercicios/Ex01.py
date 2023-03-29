#Bibliotecas necessárias para o funcionamento do código
#Caso seja necessário instalar, utilize o terminal e em seguida digite: pip install glfw, pip install PyOpenGL e PyOpenGL_accelerate
import glfw
from OpenGL.GL import *


#Função do desenho
def desenhoTriangulo():
    #É necessário utilizar o glClear() para limpar o buffer e não ocorrer nenhum problema na hora de desenhar alguma coisa na tela.
    glClear(GL_COLOR_BUFFER_BIT)

    #Aqui foi definido o triângulo, passando como parâmetro a constante "GL_TRIANGLES" para informar ao OpenGL que estamos desenhando um triângulo.
    glBegin(GL_TRIANGLES)

    #Nessa parte é definida os pontos do triângulo, onde é utilizado o glVertex2f(),  o 2f representa que estamos fornecendos coordenadas em duas dimensões (x,y)
    #Define o primeiro ponto do triângulo, localizado em (-0.5, -0.5)
    glVertex2f(-0.5, -0.5)

    # Define o segundo ponto do triângulo, localizado em (0.5, -0.5)
    glVertex2f(0.5, -0.5)

    # Define o terceiro ponto do triângulo, localizado em (-0.5, 0.5)
    glVertex2f(-0.5, 0.5)

    #Finaliza o processo de desenho do triângulo
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
        desenhoTriangulo()

        #Esta linha troca os buffers de cor da janela. Essa operação mostra a imagem renderizada na janela, tornando-a visível para o usuário. Ou seja, sem essa função, a janela abre, porém não irá aparecer nada além de uma tela branca com o título e sua resolução.
        glfw.swap_buffers(window)

    glfw.terminate()

#Essa linha é uma verificação condicional que verifica se o nome do módulo em que o código está sendo executado é igual a "__main__". Quando um módulo é importado em outro programa Python, o nome do módulo não é "__main__". No entanto, quando um script é executado diretamente (por exemplo, com o comando python nome_do_script.py), o nome do módulo é definido como "__main__".
if __name__ == "__main__":
    main()
