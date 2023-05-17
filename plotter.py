import tkinter
import numpy
import mandelbrot_set_generator

top = tkinter.Tk()
C = tkinter.Canvas(top, bg="black", height=400, width=400)

pixels = [[]]

for a in numpy.arange(-1.4, -1.35, 0.000125):
    column = []
    for b in numpy.arange(-0.025, 0.025, 0.000125):
        column.append(mandelbrot_set_generator.devergesToInfinity(a, b))

    print(a)
    pixels.append(column)

for columnIndex in range(len(pixels)):
    column = pixels[columnIndex]
    for pixelIndex in range(len(column)):
        pixel = column[pixelIndex]
        if(pixel):
            C.create_line(columnIndex, pixelIndex, columnIndex + 1, pixelIndex, fill="red")


C.pack()
top.mainloop()