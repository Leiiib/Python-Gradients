
![Logo](https://cdn.discordapp.com/attachments/1128119568389382156/1129873294078771322/python-gradients.png)


# Python Gradients

An utility to create and print gradients in Python


## Features

- Compact
- Dynamic (adapts to text size)
- Supports RGB!


## Usage/Examples

To create a gradient, use the gradient and pass as argumets two rgb colors.

```python
from gradient import  Color, gradient

text = """
████████╗███████╗██╗  ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║   
   ██║   ██╔══╝   ██╔██╗    ██║   
   ██║   ███████╗██╔╝ ██╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   
"""

print(gradient(Color(112, 11, 250), Color(40, 221, 242), text))

```

![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129874862538772503/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877221163667486/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877301203570769/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877495110443068/image.png)

Doing animated gradients is a little more complicated. To use them, you will need to have a loop and create an Animation instance, which takes two colors, the text, the animation duration and a step:
```python
from gradient import animated_gradient, Color, Animation

text = """
████████╗███████╗██╗  ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║   
   ██║   ██╔══╝   ██╔██╗    ██║   
   ██║   ███████╗██╔╝ ██╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   
"""

animation = Animation(Color(40, 221, 242), Color(112, 11, 250), text, 5, .5)

while True:
    print(animated_gradient(animation))

    #Other actions

    animation.tick()
```
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1130123957098528778/Untitled_video_-_Made_with_Clipchamp.gif)



## TODO

- Add vertical and if i have the required iq diagonal.
- Support more than 2 colors.

## Authors

- [@NebulusDev](https://www.github.com/Leiiib)

