# mandelbrot-set
Program to visualize the Mandelbrot set on a Tkinter canvas using python

## About the Mandelbrot set
To learn more about the Mandelbrot set, check out this wikipedia article: https://en.wikipedia.org/wiki/Mandelbrot_set

## Color version


## Single color version

Right now, there are 2 versions of the program. The black and white version only colors all the pixels corresponding to the coordinates, that did not deverge to infinity in the tested interval of runs. The color version colors every pixel depending on how many iterations it took to prove, that it deverges to infinity. If it could not prove, that it diverges to infinity, it colors it in full color.

## How it works
Both versions use the escape time algorithm.

By default, the program opens a window with 400 x 400 pixels. This value can however be easily changed.
Every pixel in the window represents a complex number on the complex plane. This complex number is then used as the constant c in the function f(z) = z² + c. In the first step the program calculates the result for f(0). Then it runs f(z) again, but uses the result of the previous iteration as z. It repeats this process for a finite amount of iterations.
It checks, result of the calculation diverges to infinity. If it does, c does not belong to the Mandelbrot set and it's corresponding pixel therefore doesn't get painted. If it does not, the program interprets it as c belonging to the Mandelbrot set and colors the corresponding pixel.
It does this for every pixel on the screen.

The color version does essentially the same thing with the small difference, that it keeps track of how many iterations it takes for a given c to diverge to infinity (if it does). The amount of iterations then gets converted into a color to show what values of c are more and less "stable".
 