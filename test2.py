# import random as r
# from random import choice,randint
# print(randint(1,6))
# print(choice([2,3,4,5,6,7,99,88,77,55]))
# print(r.)
# import random 
# color = random.randrange(0,255)
# hex_color = hex(color)
# total_color = '#' + hex_color[2:] 
# print(total_color)
from random import choice
rgb_color = ""
for i in range (6):
     rgb_color += choice('0123456789ABCDEF')
rgb_color = '#' + rgb_color
print(rgb_color)












