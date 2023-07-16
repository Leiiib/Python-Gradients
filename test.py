from gradient import animated_gradient, Color, Animation, gradient

text = """
████████╗███████╗██╗  ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║   
   ██║   ██╔══╝   ██╔██╗    ██║   
   ██║   ███████╗██╔╝ ██╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   
"""

animation = Animation(Color(40, 221, 242), Color(112, 11, 250), text, 5, .5, True)

while True:
    animated_gradient(animation)

    print(gradient(Color(112, 11, 250), Color(40, 221, 242), text))

    animation.tick()