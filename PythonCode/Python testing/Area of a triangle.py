"""
This is a very simple program which allows you to input
the Height and Base of a triangle in order to calculate its area.
"""

print('Finding the area of a triangle')
Height = input('Height of triangle = ')
Base = input('Base of triangle = ')
Base = float(Base)
Height = float(Height)
Area = (Height*Base/2)
print('The area of this triangle = {}' .format(Area))

