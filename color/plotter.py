import tkinter
import numpy
import mandelbrot_set_generator

maxIterations = 100

def getHexColor(iterations, maxIterations):

    maxValue = 255
    relativeValue = iterations / maxIterations

    absoluteValue = round(relativeValue * maxValue)

    redValue = round(abs(255 - relativeValue * 510))

    greenValue = 255 - absoluteValue

    hexString = f'#{redValue:02x}{greenValue:02x}{absoluteValue:02x}'
    return hexString


top = tkinter.Tk()
C = tkinter.Canvas(top, bg="black", height=400, width=400)

pixels = [[]]

for a in numpy.arange(-2, 0, 0.005):
    column = []
    for b in numpy.arange(-1, 1, 0.005):
        column.append(mandelbrot_set_generator.devergesToInfinity(a, b, maxIterations=maxIterations))

    print(a)
    pixels.append(column)

for columnIndex in range(len(pixels)):
    column = pixels[columnIndex]
    for pixelIndex in range(len(column)):
        pixel = column[pixelIndex]
        color = getHexColor(pixel, maxIterations=maxIterations)
        C.create_line(columnIndex, pixelIndex, columnIndex + 1, pixelIndex, fill=color)




C.pack()
top.mainloop()