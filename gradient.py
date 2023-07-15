
class Color():

    r = g = b = 0

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def getRed(self):
        return self.r
    def getGreen(self):
        return self.g
    def getBlue(self):
        return self.b
    

def horizontalGradient(color1: Color, color2: Color, text: str):

    output = """"""
    lines = text.splitlines()
    amount = len(lines)

    rOff = abs(color1.getRed()-color2.getRed())
    startR = color1.getRed()
    rStep = int(abs(rOff/amount))

    gOff = abs(color1.getGreen()-color2.getGreen())
    startG = color1.getGreen()
    gStep = int(abs(gOff/amount))

    bOff = abs(color1.getBlue()-color2.getBlue())
    startB = color1.getBlue()
    bStep = int(abs(bOff/amount))

    r = startR
    g = startG
    b = startB
    for line in lines:
        r = r - rStep if color1.getRed() > color2.getRed() else r + rStep
        g = g - gStep if color1.getGreen() > color2.getGreen() else g + gStep
        b = b - bStep if color1.getBlue()>color2.getBlue() else b + bStep

        output += (f"\033[38;2;{r};{g};{b};220m{line}\033[0m\n")    
        
    return output
