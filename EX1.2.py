class pyramid:
    def __init__(self,l = None,w = None,h = None):
        self.length = l
        self.width = w
        self.hight = h

    def calculetor(self):
        result = (self.length*self.width*self.hight)/3
        print(result)

main = pyramid(10,7,17)
main.calculetor()
