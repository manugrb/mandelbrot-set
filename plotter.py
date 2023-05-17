import tkinter
import mandelbrot_set_generator.py

top = tkinter.Tk()
C = tkinter.Canvas(top, bg="black", height=400, width=400)

for columnIndex in range(len(pixels)):
    column = pixels[columnIndex]
    for pixelIndex in range(len(column)):
        pixel = column[pixelIndex]
        if(pixel):
            C.create_line(columnIndex, pixelIndex, columnIndex + 1, pixelIndex, fill="red")


C.pack()
top.mainloop()