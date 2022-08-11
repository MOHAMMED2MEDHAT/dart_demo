from shapes import Shapes


user=Shapes()
user.add2D("triangel",1,1,4,5)
user.add2D("rectangel",1,1,4,5)
user.add2D("circle",1,1,5,5)
user.add2D("square",1,1,5,5)
user.move2D("triangel",2,2)
user.move2D("rectangel",3,3)
user.move2D("circle",4,4)


user.add3D("cube",1,2,3,5,5,5)
user.add3D("cone",3,4,5,2,8,6)
user.move3D("cube",4,5,6)
user.move3D("cone",7,8,9)

user.scale("triangel",5)
user.scale("rectangel",4)
user.scale("cube",3)
user.scale("cone",2)

listOfShapes=["triangel","rectangel","circle","square","cube","cone"]

for shape in listOfShapes:
    user.show(shape)