class operation:
    def __init__(self):
        self.length=int(input("enter the length in cm:"))
        self.breadth=int(input("enter the breadth in cm:"))
    def areas(self):
        self.area=self.breadth*self.length
        print("the area of rectangle is:",self.area)

obj1=operation()
obj1.areas()
    