def fractal(x, y, size):
    canvas.create_oval(x, y, x + size, y + size)
    if size < 5:
        pass
    else:
        fractal(x, y, size/2)
        fractal(x + size/2, y+size/2, size/2)

fractal(5, 5, 590)
