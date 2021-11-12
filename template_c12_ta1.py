# Importing 'random'
import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
# Invert the pipe image and loading it into the 'images' dictionary

groundx=0
speed=0
class Bird:
    bird=pygame.Rect(100,250,30,30)
    
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    # The following line is commented as it is no longer required
    #bpipe=pygame.Rect(250,400,40,320)
    
    # Define the constructor __init__()
    
        # Assign a random value in the range of 150 and 400 to the variable 'self.height'
        
        # Create 'self.tpipe' rectangle 
        # x-coordinate is the 'x' value passed as argument
        # y-coordinate is 'self.height-400' where 400 is the length of pipe image
        
        
        # Create 'self.bpipe' rectangle 
        # x-coordinate is the 'x' value passed as argument
        # y-coordinate is 'self.height+150' where 150 is the constant gap between the pipes
        
        
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      # Display the inverted pipe image over the 'self.tpipe' rectangle
      
    
bird1=Bird()
# Create an object 'pipe1' for the 'Pipe' class by passing x-coordinate value as the argument


while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  
  pipe1.display()
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
