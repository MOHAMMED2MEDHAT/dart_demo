
from shape import Sh, Sh3D

class Shapes:
    shapesDict={}
    
    def add2D(self,name,x,y,length,width):
        self.shapesDict[name]=Sh(name,x,y,length,width)
        
    def add3D(self,name,x,y,z,length,width,height):
        self.shapesDict[name]=Sh3D(name,x,y,z,length,width,height)
    
    def move2D(self,name,x,y):
        self.shapesDict[name].position_X=x
        self.shapesDict[name].position_Y=y
            
    def move3D(self,name,x,y,z):
        self.shapesDict[name].position_X=x 
        self.shapesDict[name].position_Y=y 
        self.shapesDict[name].position_Z=z 
            
    def scale(self,name,scalingFactor):
        if self.shapesDict[name].typ=="2d":
            self.shapesDict[name].length=self.shapesDict[name].length*scalingFactor
            self.shapesDict[name].width=self.shapesDict[name].width*scalingFactor
        else:
            self.shapesDict[name].length=self.shapesDict[name].length*scalingFactor
            self.shapesDict[name].width=self.shapesDict[name].width*scalingFactor
            self.shapesDict[name].height=self.shapesDict[name].height*scalingFactor
                
    def delete(self,name):
        del self.shapesDict[name]
    
    def show(self,name):
        if self.shapesDict[name].typ=="2d":
            print(self.shapesDict[name].name+","+self.shapesDict[name].typ +","+str(self.shapesDict[name].position_X)+","+str(self.shapesDict[name].position_Y)+","+str(self.shapesDict[name].length)+","+str(self.shapesDict[name].width))
        else:
            print(self.shapesDict[name].name+","+self.shapesDict[name].typ +","+str(self.shapesDict[name].position_X)+","+str(self.shapesDict[name].position_Y)+","+str(self.shapesDict[name].position_Z)+","+str(self.shapesDict[name].length)+","+str(self.shapesDict[name].width)+","+str(self.shapesDict[name].height))
        