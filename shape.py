
class Sh:
    name,typ="","2d"
    position_X,position_Y,length,width=0,0,0,0
    
    def __init__(self,name,position_X,position_Y,length,width):
        self.name=name
        self.position_X=position_X
        self.position_Y=position_Y
        self.length=length
        self.width=width
        
    def move(self,x,y):
        self.position_X=x
        self.position_Y=y
    
    def scale(self,scalingFactor):
        self.length=self.length*scalingFactor
        self.width=self.width*scalingFactor
        
class Sh3D(Sh):
    typ="3d"
    position_Z,height=0,0
    def __init__(self, name, position_X, position_Y,position_Z,length, width,height):
        super().__init__(name, position_X, position_Y, length, width)
        self.position_Z=position_Z
        self.height=height
    
    def move(self, x, y,z):
        self.position_X=x
        self.position_Y=y
        self.position_Z=z
        
    def scale(self, scalingFactor):
        self.length=self.length*scalingFactor
        self.width=self.width*scalingFactor
        self.height=self.height*scalingFactor