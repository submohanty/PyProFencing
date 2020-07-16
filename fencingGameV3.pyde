class Player(object):
    def __init__(self,x,y,col,siz,speed,controls):
        self.x=x
        self.y=y
        self.col=col
        self.siz=siz
        self.speed=speed
        self.controls=controls
        self.swordSpeed=0.05
        self.angle=0
        self.score=0
        self.sword_length=siz+20
        self.overlap=False
        self.hit=False
        
    def show(self):
        #draw the sword
        self.xend = self.x + cos(self.angle)*self.sword_length
        self.yend= self.y+sin(self.angle)*self.sword_length
        strokeWeight(1)
        stroke(self.col)
        line(self.x,self.y,self.xend,self.yend)
        #draw the player
        noStroke()
        fill(self.col)
        ellipse(self.x,self.y,self.siz,self.siz)
        text(self.score,self.x-3,self.y+self.siz/2+10)
    
    def move(self):
        #move the player
        if(keyPressed and key==self.controls[0]):
            self.y-=self.speed
        elif(keyPressed and key==self.controls[1]):
            self.x+=self.speed
        elif(keyPressed and key==self.controls[2]):
            self.y+=self.speed
        elif(keyPressed and key==self.controls[3]):
            self.x-=self.speed
        elif(keyPressed and key==self.controls[4]):
            self.angle+=self.swordSpeed
        elif(keyPressed and key==self.controls[5]):
            self.angle-=self.swordSpeed
    def collideCircleCircle(self,other):
        if(dist(self.x,self.y,other.x,other.y)<=self.siz/2+other.siz/2):
            other.col=color(0,255,0)
            return True
        else:
            other.col=color(0,0,255)
            return False
    def collidePointCircle(self,other):
        if(dist(self.xend,self.yend,other.x,other.y)<=other.siz/2):
            other.col=color(255,0,0)
            return True
        else:
            other.col = color(0,0,255)
            return False
    def collide(self,other):
        self.overlap=self.collideCircleCircle(other)
        self.hit=self.collidePointCircle(other)
        
        if(self.overlap==False):
            if(self.hit==True):
                self.score+=1
                
    
p1Controls=['w','d','s','a','e','q']
p2Controls=['i','l','k','j','o','u']
    
player1=Player(100,100,color(0),100,1,p1Controls)
player2=Player(300,500,color(255,0,255),100,1,p2Controls)
    
def setup():
    size(800,800)
        
def draw():
        background(200)
        player1.show()
        player2.show()
        player1.move()
        player2.move()
        player1.collide(player2)
        player2.collide(player1)
    
