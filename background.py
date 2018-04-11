import numpy as np
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(1,1,1,1)
    glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable (GL_DEPTH_TEST)

    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glOrtho(0,800, 0 , 500, 0 , 1) # l,r,b,t,n,f


    glMatrixMode (GL_MODELVIEW)

def sky():
    #glColor3f(0,0,0)
    glBegin (GL_QUADS)
    glVertex(0,500,0)
    glVertex (800,500,0)
    glVertex (800,210,0)
    glVertex (0,210,0)
    glEnd()
        
def greenground():
    #glColor3f(0,0,0)
    glBegin (GL_QUADS)
    glVertex (0,210,0)
    glVertex (800,210,0)
    glVertex (800,100,0)
    glVertex (0,100,0)
    glEnd()
        
def ground2():
    #glColor3f(0,0,0)
    glBegin (GL_QUADS)
    glVertex  (0,100,0)
    glVertex  (800,100,0)
    glVertex  (800,0,0)
    glVertex  (0,0,0)
    glEnd()
        
def treetwnig():
    glBegin(GL_POLYGON)
    glVertex (100,150,0)
    glVertex (120,150,0)
    glVertex (120,320,0)
    glVertex (100,320,0)
    
    glEnd()

def tree (r=1,x0=0,y0=0):
   glBegin (GL_POLYGON)
   for theta in np.arange (0,2 *pi,0.01):
      x=x0+r*cos (theta)
      y=y0+r*sin(theta)
      glVertex2d(x,y)
   glEnd()

def cloud1 (r=1,x0=0,y0=0):
   glBegin (GL_POLYGON)
   for theta in np.arange (0,pi,0.1):
      x=x0+r*cos (theta)
      y=y0+r*sin(theta)
      glVertex2d(x,y)
   glEnd()
   
def cloud_sky (r=1,x0=0,y0=0):
   glBegin (GL_POLYGON)
   for theta in np.arange (0,pi,0.001):
      x=x0+r*cos (theta)
      y=y0+r*0.65*sin(theta)
      glVertex2d(x,y)
   glEnd()
   

def scoresquare():      #score
    #glColor3f(0,0,0)
    glBegin (GL_LINE_LOOP)
    glVertex2d (770,40)
    glVertex2d (690,40)
    glVertex2d (690,10)
    glVertex2d (770,10)
    glEnd()

def shootsquare():      #shoot
    #glColor3f(0,0,0)
    glBegin (GL_LINE_LOOP)
    glVertex2d (500,40)
    glVertex2d (420,40)
    glVertex2d (420,10)
    glVertex2d (500,10)
    glEnd()


def livessquare():     #hits
    #glColor3f(0,0,0)
    glBegin (GL_LINE_LOOP)
    glVertex2d (680,40)
    glVertex2d (600,40)
    glVertex2d (600,10)
    glVertex2d (680,10)
    glEnd()

def triessquare():      #tries
    #glColor3f(0,0,0)
    glBegin (GL_LINE_LOOP)
    glVertex2d (590,40)
    glVertex2d (510,40)
    glVertex2d (510,10)
    glVertex2d (590,10)
    glEnd()



def display1():

   


    glColor3f(0,0.8,0)
    tree (36,100,280)
    tree (36,155,300)         
    tree (36,60,330)         #tree
    tree (36,95,380)
    tree (36,110,335)
    tree (36,155,360)


#.............................................
    glColor3f(1,1,1)
    cloud1 (41,647,365)
    cloud_sky(41,610,356)
    cloud_sky(41,680,356)   #left cloud
    cloud_sky(41,640,357)

    
    glColor3f(0.95,0.95,0.95)
    cloud1 (41,654,365)
    cloud_sky(41,617,356)
    cloud_sky(41,687,356)   #left cloud shadow
    cloud_sky(41,647,356)
#............................................
    glColor3f(1,1,1)
    cloud1 (41,343,435)
    cloud_sky(41,310,426)
    cloud_sky(41,380,426)  #right cloud
    cloud_sky(41,340,426)

    
    glColor3f(0.95,0.95,0.95)
    cloud1 (41,350,435)
    cloud_sky(41,317,426)
    cloud_sky(41,387,426)  #right cloud shadow
    cloud_sky(41,347,426)
#............................................
    glLineWidth(2)
    glColor3f(0,0,0.56)
    scoresquare()  #score
    shootsquare ()  #shuts
    livessquare()  #lives
    triessquare()
     

    #glColor(1,0,0)
    glColor(0.5,0.25,0) #treetwnig
    treetwnig()

    glColor3f(0,0.9,1)  #blue sky 
    sky()
    
    glColor3f(0,0.91,0) #greenground
    greenground()

    glColor3f(0.75,0.75,0.75) #grayground
    ground2()






