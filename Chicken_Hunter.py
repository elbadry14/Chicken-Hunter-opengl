from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *
import winsound
import ChickenCode
import random
import background

winsound.PlaySound("C:\\Users\\abdal\\AppData\\Local\\Programs\\Python\\Python35-32\\Rooster-crowing-in-the-morning.wav", winsound.SND_FILENAME | winsound.SND_NOSTOP)
winsound.PlaySound("C:\\Users\\abdal\\AppData\\Local\\Programs\\Python\\Python35-32\\Duck-quack-sound.wav", winsound.SND_ASYNC | winsound.SND_FILENAME | winsound.SND_NOSTOP | winsound.SND_LOOP)

def init( ):
  glClearColor (0.0, 0.0, 0.0, 0.0)
  glMatrixMode (GL_PROJECTION)
  glLoadIdentity ()
  glOrtho(0, 800, 0 , 500 , -600 , 600) 
  glMatrixMode (GL_MODELVIEW)
  glEnable(GL_DEPTH_TEST)

class cir:
        def __init__(self, x , y):
                self.x0 = x
                self.y0 = y 

class LINE:
        def __init__(self, left, right, top , bottom):
                self.left = left
                self.bottom = bottom
                self.right = right
                self.top = top
x=0
y=0
radius=10
def draw_circle(circle):
    glBegin(GL_LINE_LOOP)
    for theta in np.arange(0,360,0.1):
        x= circle.x0 + radius * cos(theta * pi / 180)
        y= circle.y0+500 + radius * sin(theta * pi / 180)
        glVertex(x,y)
    glEnd()

def DrawRectangle(rect):
    glLoadIdentity()
    glBegin(GL_LINES) 
    glVertex(rect.left,rect.bottom)
    glVertex(rect.left,rect.top)
    glVertex(rect.right,rect.bottom) 
    glVertex(rect.right,rect.top) 
    glVertex(rect.left,rect.top)
    glVertex(rect.right,rect.top)
    glVertex(rect.left,rect.buttonttom)
    glVertex(rect.right,rect.bottom)
    glEnd()

def DrawPluse(plus):
    glLoadIdentity()
    glBegin(GL_LINES) 
    glVertex(plus.right,plus.top+510)     
    glVertex(plus.right,plus.top+490) 
    glVertex(plus.right+20/2,plus.top+1000/2) 
    glVertex(plus.right-20/2,plus.top+1000/2) 
    glEnd()

mouse_x=0
mouse_y=0
def MouseMotion(x,y):
  global mouse_x
  global mouse_y 
  mouse_x=x
  mouse_y=-y

Hit = False
r = 0
g = 0
b = 0
Score = 0
Level = 1
Tries = 3
Hits = 3
def MouseAction (button, state, x, y):
    global Hit,r,g,b,k,n,Target,mouse_x,mouse_y,movement1,movement2,plus,Score,Level,Hits,Tries
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
                winsound.PlaySound("C:\\Users\\abdal\\AppData\\Local\\Programs\\Python\\Python35-32\\Gun2.wav", winsound.SND_FILENAME)
                Hits -= 1
                if  movement2.top+510 <= Target.top and movement2.top+490 >= Target.bottom and movement2.right+20/2 <= Target.right and movement2.left+20/2 >= Target.left:
                        winsound.PlaySound("C:\\Users\\abdal\\AppData\\Local\\Programs\\Python\\Python35-32\\Duck-quack-sound.wav", winsound.SND_ASYNC | winsound.SND_NOWAIT | winsound.SND_FILENAME | winsound.SND_NOSTOP | winsound.SND_LOOP)
                        Hit = True
                        Score += 1
                        if Score %5 == 0:
                          Level += 1
                        r=0
                        g=1
                        b=1
                else:
                        winsound.PlaySound("C:\\Users\\abdal\\AppData\\Local\\Programs\\Python\\Python35-32\\Duck-quack-sound.wav", winsound.SND_ASYNC | winsound.SND_NOWAIT | winsound.SND_FILENAME | winsound.SND_NOSTOP | winsound.SND_LOOP)
                        if Hits == 0:
                          Tries -= 1
                          Hits = 3
                        r=1
                        g=1
                        b=0
                        
       
time_interval=10
def Timer(v): 
  Display() 
  glutTimerFunc(time_interval,Timer,1)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

animated = 1
Valid = 0
Valid2 = 0
def keyboard (key,x,y):
  global animated,Valid,Valid2
  if key == b"q" :
    animated = 0
    Valid = 1
  if key == b"p":
    animated = 0
    Valid2 = 1
  if key == b"c":
    animated = 1
    Valid2 = 0
  if key == b"r":
    restart_program ()
  if key == b"y" and Valid == 1:
    sys.exit()
  if key == b"n" and Valid == 1:
    animated = 1
    Valid = 0

Shift = 0
def Sin(a , Shift):
    y = 200*sin(a/16) + Shift
    return y
      
def Straight(a,Shift):
    y = a +Shift 
    return y

def Cos(a , Shift):
    y = 100*cos(a/8) + Shift
    return y

def init_start () :
    initi = random.randrange(20, 600 , 2)
    return initi

def random_path (path_selection, x ) :
    if path_selection == 0 :
        y=Sin(x,Shift) 
        return y
      
    if path_selection == 1 :
        y=Straight(x,Shift) 
        return y
      
    if path_selection == 2:
        y=Cos(x,Shift) 
        return y

def drawText(string, x, y):
        glLineWidth(1)
        glColor(0.21,0.21,0.21)  # Yellow Color
        glLoadIdentity()
        glTranslate(x,y,0)
        glScale(0.13,0.13,1)
        string = string.encode() # conversion from Unicode string to byte string
        for c in string:
                glutStrokeCharacter(GLUT_STROKE_ROMAN , c )

Target = LINE (-20, 20, 35 , -29)
movement1 = cir(65,15)
movement2 = LINE(0,0,60,10)
x1 = 0
mov = 0
y1 = 0
z1 = 0
Wing = 0
path = 0
path_selection = 0
speed = 0.1
Disappear = 0
WingMov = True
def Display():
  global movement1,movement2,x1,y1,z1,Wing,Hit,Target,r,g,b,animated,path_selection,mov,path,initi,speed,Shift,Disappear,Score,Level,Tries,Hits,Valid,Valid2,WingMov
  
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  
  string = "Score: " + str(Score)
  drawText(string,425,20)
  string = "Level: " + str(Level)
  drawText(string,515,20)
  string = "Tries: " + str(Tries)
  drawText(string,605,20)
  string = "Hits: " + str(Hits)
  drawText(string,695,20)

  if Valid ==1:
    string = "Are You Sure" 
    drawText(string,350,250)
    string = "(Y)es or (N)o" 
    drawText(string,350,225)
    
  if Tries == 0:
    animated = 0
    string = "Game Over" 
    drawText(string,350,250)
    string = "press (R) to Restart or (Q) to Quit" 
    drawText(string,250,225)
    if Valid == 1:
      sys.exit()
    
  if Valid2 == 1:
    string = "press (C) to Continue" 
    drawText(string,350,250)
  
  #glLoadIdentity()
  #glColor(0.6,0.3,5.9)
  #DrawRectangle(Target)
  
  glLoadIdentity()
  glColor(1-r,1-g,1-b)
  movement1.x0 = (mouse_x+1)*animated
  movement1.y0 = (mouse_y+1)*animated
  draw_circle(movement1)

  glLoadIdentity()
  glColor(1-r,1-g,1-b)
  movement2.left = (mouse_x-1)*animated
  movement2.right = (mouse_x+1)*animated
  movement2.top = (mouse_y+1)*animated
  movement2.bottom = (mouse_y-1)*animated
  DrawPluse(movement2)

  r -= 0.1
  g -= 0.1
  b -= 0.1

  if mov == 0:
      path_selection = 0
    
  y1= random_path(path_selection,mov)
  
  if Hit == False:
      ChickenCode.Chicken(x1+mov,y1+210,z1,Wing)
      if Wing >= 50:
          WingMov = False
      if WingMov :
        Wing = Wing + 13
        
      if WingMov == False :
        if Wing != 0:
          Wing = Wing - 13
        else :
          WingMov = True
      mov = mov+(5+speed)*animated
      Shift = Shift+(2)*animated
      Target.right = x1+mov+25
      Target.left = Target.right-52
      Target.top = y1+250
      Target.bottom = Target.top-64
      
  if x1+mov >= 800 or y1 >= 500 or Hit == True :
      Tries -= 1
      if Hit == True:
          Hits = 3
          Tries += 1
          ChickenCode.Chicken(x1+mov,y1-Disappear,z1,Wing)
          Wing = 0
          Disappear += 30
          if Disappear > 500:
            Hit = False
                    
            mov = 10
            speed = speed+0.1
            x1 = init_start ()
            path_selection = random.randrange (0 , 2 ,1)
            Shift = 0
            Disappear = 0

      else:
        Hits = 3
        mov = 10
        speed = speed+0.1
        x1 = init_start ()
        path_selection = random.randrange (0 , 2 ,1)
        Shift = 0
        Hit = False

  glLoadIdentity()
  background.display1()
  
  glutSwapBuffers()
        
def main():
   glutInit(sys.argv)
   glutInitDisplayMode ( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize (800,500)
   glutInitWindowPosition (0, 0)
   glutCreateWindow (b"Chicken Hunter");
   glutDisplayFunc(Display)
   glutTimerFunc(time_interval,Timer,1)
   glutPassiveMotionFunc(MouseMotion)
   glutMouseFunc(MouseAction)
   glutSetCursor(GLUT_CURSOR_NONE)
   glutKeyboardFunc(keyboard)
   init( )   
   glutMainLoop()

main()
