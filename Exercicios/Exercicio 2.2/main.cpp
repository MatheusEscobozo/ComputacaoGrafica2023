#include <GL/glut.h>

int windowWidth = 800;    // Largura da janela
int windowHeight = 600;   // Altura da janela
int pointSize = 10;       // Tamanho do ponto
int pointX = -1;          // Coordenada X do ponto
int pointY = -1;          // Coordenada Y do ponto
bool clicked = false;

void janela() {
    glClear(GL_COLOR_BUFFER_BIT);   // Limpa a janela
    glColor3f(1.0f, 1.0f, 0.0f);    // Define a cor do ponto 
    glPointSize(pointSize);         // Define o tamanho do ponto
    glBegin(GL_POINTS);             // Começa a desenhar o ponto
    glVertex2i(pointX, pointY);     // Define as coordenadas do ponto
    glEnd();                        // Finaliza o desenho do ponto
    glutSwapBuffers();              // Troca os buffers
}

void mouse(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {  // Verifica se foi um clique esquerdo do mouse
        pointX = x;           // Salva a coordenada X do clique do mouse
        pointY = windowHeight - y; // Salva a coordenada Y do clique do mouse e inverte a origem do eixo Y	//
        clicked = true;			// É necessário subtrair a coordenada Y do mouse da altura da janela
        glutPostRedisplay();  // Redesenha a janela
    }
}


void teclado(int key, int x, int y) {  //Função onde é realizada a chamada do teclado
    if (clicked) {
        switch (key) {				
            case GLUT_KEY_LEFT:		// Setinha esquerda					
                pointX -= 10;
                break;
            case GLUT_KEY_RIGHT:	// Setinha direita
                pointX += 10;
                break;
            case GLUT_KEY_UP:		//Setinha cima
                pointY += 10;
                break;
            case GLUT_KEY_DOWN:		//Setinha baixo
                pointY -= 10;
                break;
            default:
                break;
        }
        glutPostRedisplay();		//Redesenha a janela
    }
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);                              // Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);        // Configura o modo de display
    glutInitWindowSize(windowWidth, windowHeight);     // Define o tamanho da janela
    glutCreateWindow("Ex02");                   		// Cria a janela com o título
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);                // Define a cor de fundo da janela
    gluOrtho2D(0, windowWidth, 0, windowHeight);         // Define as coordenadas do sistema de coordenadas
    glutDisplayFunc(janela);                            // Configura a função de display
    glutMouseFunc(mouse);                                // Configura a função de mouse
    glutSpecialFunc(teclado);
    glutMainLoop();                                      // Inicia o loop principal do GLUT
    return 0;
}

