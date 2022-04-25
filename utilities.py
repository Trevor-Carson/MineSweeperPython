import settings

def width_prct(percentage):
    return (settings.window_width / 100) * percentage

def height_prct(percentage):
    return (settings.window_height / 100) * percentage

# print(width_prct(25))