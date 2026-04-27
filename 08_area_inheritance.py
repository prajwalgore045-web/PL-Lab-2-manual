class Shape:
 def area(self):pass
class Rect(Shape):
 def __init__(self,l,b):self.l=l;self.b=b
 def area(self):print(self.l*self.b)
Rect(2,3).area()