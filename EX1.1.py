class cylinder:
    def __init__(self,R = None,H = None):
        self.radius = R
        self.height = H

    def calculator(self):
        result = 3.14*(self.radius*self.radius)*self.height
        print(result)
    
#V1    
main = cylinder(5,10)
main.calculator()

#V2
cylinder(7,13).calculator()
