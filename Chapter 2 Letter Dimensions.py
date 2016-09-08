# This program displays the dimensions of a letter size paper in millimeters
# 8.5 x 11 inch
MILLIMETERS_PER_INCH = 24.3


# Width and height of a regular paper in inches
WIDTH_OF_PAPER = 8.5
HEIGHT_OF_PAPER = 11

widthInMillimeters = MILLIMETERS_PER_INCH * WIDTH_OF_PAPER
heightInMillimeters = MILLIMETERS_PER_INCH * HEIGHT_OF_PAPER

print("A 8.5x11 inch paper is the same as",str(widthInMillimeters) + "x" + str(heightInMillimeters), "millimeters.")
