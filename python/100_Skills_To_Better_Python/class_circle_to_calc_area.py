class circle:
    def __init__(self,r):
        self.radius = r 
    def area(self):
        print("Area of circle is",(self.radius**2)*3.14,"cm^2")
print(circle(4).area())

