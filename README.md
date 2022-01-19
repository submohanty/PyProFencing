## PyProFencing
<img src="https://img.shields.io/github/license/submohanty/PyProFencing?color=MIT"><br>  
### A 2D Multiplayer Fencing (Sword-fighting) game created with Python and Processing.

<img src="https://raw.githubusercontent.com/submohanty/PyProFencing/main/game.gif"> <br>

This is a two player game playable on one keyboard, where both players try to put their fencing sword through their opponent player model and rack up points. It is recommended to play with a keyboard that has N-Key Rollover to allow for all keyboard inputs to go through.  

### Controls
#### Player 1: WASD for movement, Q/E for movement of the sword  
#### Player 2: IJKL for movement, U/O for movement of the sword  

### Color Changing  
If you would like to change the color of your player models, find this block of code and change the rgb values where indicated by my comment:
```
    def collideCircleCircle(self,other):
        if(dist(self.x,self.y,other.x,other.y)<=self.siz/2+other.siz/2):
            other.col=color(0,255,0) # change the RGB color value
            return True
        else:
            other.col=color(0,0,255)
            return False
    def collidePointCircle(self,other):
        if(dist(self.xend,self.yend,other.x,other.y)<=other.siz/2):
            other.col=color(255,0,0) # change this RGB color value
            return True
        else:
            other.col = color(0,0,255)
            return False
```  
