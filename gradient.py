from enum import Enum
import time


"""
Currently only Horizontal supported
"""
class Type(Enum):
    HORIZONTAL= 1
    VERTICAL= 2
    DIAGONAL= 3

"""
Simple color class
"""
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
    
"""
Static gradient
"""
def gradient(color1: Color, color2: Color, text: str, type:Type = Type.HORIZONTAL):

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

"""
Simple Animation class used to contain all rewuired data
"""
class Animation:

    r = g = b = 0
    color1 = color2 = 0
    text: str = ""
    duration: int = 0
    step: float = 0.0
    amount = 0
    rOff = gOff = bOff = startR = startG = startB = rStep = gStep = bStep = 0
    running = False

    def __init__(self, color1: Color, color2: Color, text: str, duration: int = 5, step: float = 0.5) -> None:
        self.color1 = color1
        self.color2 = color2
        self.text = text
        self.duration = duration
        self.step = step
        self.r = color1.getRed()
        self.g = color1.getGreen()
        self.b = color1.getBlue()

        self.amount = self.duration/self.step

        self.rOff = abs(color1.getRed() - color2.getRed())
        self.startR = color1.getRed()
        self.rStep = int(abs(self.rOff / self.amount))
        
        self.gOff = abs(color1.getGreen() - color2.getGreen())
        self.startG = color1.getGreen()
        self.gStep = int(abs(self.gOff / self.amount))

        self.bOff = abs(color1.getBlue() - color2.getBlue())
        self.startB = color1.getBlue()
        self.bStep = int(abs(self.bOff / self.amount))
    

    def tick(self):
        time.sleep(self.step)
        print("\033c")
"""
Animated gradient
"""
def animated_gradient(animation: Animation):
    text = animation.text   
    color1 = animation.color1
    color2 = animation.color2
    output = """"""

    rStep = animation.rStep
    gStep = animation.gStep
    bStep = animation.bStep

    r = animation.r
    g = animation.g
    b = animation.b    
    
    if(color1.getRed()>color2.getRed()):
        r -= rStep  
        if(r<color2.getRed()): 
            r = color2.getRed()
            c1r = color1.getRed()
            color1.r = color2.getRed()
            color2.r = c1r
    else:
        r += rStep
        if(r>color2.getRed()): 
            r = color2.getRed()
            c1r = color1.getRed()
            color1.r = color2.getRed()
            color2.r = c1r

    if(color1.getGreen()>color2.getGreen()): 
        g -= gStep
        if(g<color2.getGreen()):
            g = color2.getGreen()
            c1g = color1.getGreen()
            color1.g = color2.getGreen()
            color2.g = c1g
    else:
        g += gStep
        if(g>color2.getGreen()):
            g=color2.getGreen()
            c1g = color1.getGreen()
            color1.g = color2.getGreen()
            color2.g = c1g
    
    if(color1.getBlue()>color2.getBlue()):
        b -= bStep
        if(b<color2.getBlue()):
            b=color2.getBlue()
            c1b = color1.getBlue()
            color1.b = color2.getBlue()
            color2.b = c1b
    else:
        b += bStep
        if(b>color2.getBlue()):
            b=color2.getBlue()
            c1b = color1.getBlue()
            color1.b = color2.getBlue()
            color2.b = c1b
            
    animation.r = r
    animation.g = g
    animation.b = b

    output = (f"\033[38;2;{r};{g};{b};220m{text}\033[0m\n")
    return output
    



