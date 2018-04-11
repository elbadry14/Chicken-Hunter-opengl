import numpy as np
from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

s = 30


def Chicken(x,y,z,rwy):    

    #Body
    glLoadIdentity()
    glColor(0.33,0.33,0.33)
    glTranslate(x,y,z)
    glScale(1.2,1.7,0.9)
    glutSolidSphere( s*0.4,20,15)
    
    glColor(1,1,1)
    glTranslate(0,s*-0.05,s*0.13)
    glScale(1,0.9,1)
    glutSolidSphere( s*0.3,20,15)

    # Tail

    glTranslate(0,s*-0.15,s*-0.5)
    glScale(1,0.1,0.6)
    glutSolidSphere( s*0.2,20,15)
    
    
    #head
    glLoadIdentity()
    glColor(0.4,0.4,0.4)
    glTranslate(x,y+s*0.8,z)
    glutSolidSphere(s*0.35,20,15)

    


    ## Mouth
    glColor(1,1,0)
    glutSolidCone( s*0.3,s*0.55,20,50)

    
    
    ## Legs

    # Right U
    
    glLoadIdentity()
    glColor(1,1,0)
    glTranslate(x-s*0.12,y-s*0.7,z+s*0.08)
    glScale(0.35,0.7,0.35)
    glutSolidSphere( s*0.2,20,15)

    # Left U

    glTranslate(s*0.73,0,0)
    glutSolidSphere( s*0.2,20,15)

    # Right D

    glLoadIdentity()
    glColor(1,1,0)
    glTranslate(x+s*0.16,y-s*0.9,z+s*0.3)
    glRotate(180,0,1,0)
    glScale(0.9,0.3,0.7)
    glBegin(GL_TRIANGLES)
    glVertex( s*0.2,0,0)
    glVertex( s*-0.2,0,0)
    glVertex(0, s*0.4,0)
    
    glVertex( s*0.2,0,0)
    glVertex(0,0, s*0.4)
    glVertex(0, s*0.4,0)

    glVertex( s*-0.2,0,0)
    glVertex(0, s*0.4,0)
    glVertex(0,0, s*0.4)
    glEnd()

    #Left D
    
    glTranslate(s*0.35,0,0)

    glBegin(GL_TRIANGLES)
    glVertex(s*0.2,0,0)
    glVertex( s*-0.2,0,0)
    glVertex(0, s*0.4,0)
    
    glVertex( s*0.2,0,0)
    glVertex(0,0, s*0.4)
    glVertex(0, s*0.4,0)

    glVertex( s*-0.2,0,0)
    glVertex(0, s*0.4,0)
    glVertex(0,0, s*0.4)
    glEnd()
    

    

    ## Eyes
    # Right W
    
    glLoadIdentity()
    glColor(1,1,1)
    glTranslate(x+s*0.15,y+s*0.95,z+s*0.25)
    glScale(1,1.2,0.6)
    glutSolidSphere( s*0.1,20,15)

    # Left W

    glTranslate(s*-0.3,0,0)
    glutSolidSphere( s*0.1,20,15)

    # Left B
    
    glColor(0,0,1)
    glTranslate(0,0,s*0.1)
    glutSolidSphere(s*0.05,20,15)

    # Right B

    glTranslate(s*0.3,0,0)
    glutSolidSphere(s*0.05,20,15)
    
    

    ## Arms

    #right
    
    glLoadIdentity()
    glColor(0.33,0.33,0.33)
    glTranslate(x+s*0.4,y+s*0.2,z)
    glRotate(33+rwy,0,0,1)
    glScale(0.25,1,0.7)
    glutSolidSphere(s*0.45,20,15)


    glColor(1,1,1)
    glTranslate(s*0.2,s*-0.3,0)
    glRotate(30,1,0,0)
    glScale(1,1,0.5)
    glutSolidSphere(s*0.2,20,15)

    glTranslate(0,0,s*-0.2)
    glutSolidSphere(s*0.2,20,15)
    
    # Left
    
    glLoadIdentity()
    glColor(0.33,0.33,0.33)
    glTranslate(x-s*0.4,y+s*0.2,z)
    glRotate(-33-rwy,0,0,1)
    glScale(0.25,1,0.7)
    glutSolidSphere(s*0.45,20,15)


    glColor(1,1,1)
    glTranslate(s*-0.2,s*-0.3,0)
    glRotate(30,1,0,0)
    glScale(1,1,0.5)
    glutSolidSphere(s*0.2,20,15)


    glTranslate(0,0,s*-0.2)
    glutSolidSphere(s*0.2,20,15)

    


    


