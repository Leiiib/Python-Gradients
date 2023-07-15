
![Logo](https://cdn.discordapp.com/attachments/1128119568389382156/1129873294078771322/python-gradients.png)


# Python Gradients

An utility to create and print gradients in Python


## Features

- Compact
- Dynamic (adapts to text size)
- Supports RGB!


## Usage/Examples

To create a gradient, use the horizontalGradient and pass as argumets two rgb colors.

```python
from gradient import Color, horizontalGradient

text = """
████████╗███████╗██╗  ██╗████████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝
   ██║   █████╗   ╚███╔╝    ██║   
   ██║   ██╔══╝   ██╔██╗    ██║   
   ██║   ███████╗██╔╝ ██╗   ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝   
"""

print(horizontalGradient(Color(24, 153, 231), Color(171, 24, 231), text))
```



![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129874862538772503/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877221163667486/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877301203570769/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877426407747624/image.png)
![App Screenshot](https://cdn.discordapp.com/attachments/1128119568389382156/1129877495110443068/image.png)
## TODO

- Add horizontal and if i have the required iq diagonal.
- Support more than 2 colors.

## Authors

- [@NebulusDev](https://www.github.com/Leiiib)

