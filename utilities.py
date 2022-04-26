# Utility functions
import settings


# Function to set frame width in window
def width_prct(percentage):
    return (settings.window_width / 100) * percentage

# Function to set frame height in window
def height_prct(percentage):
    return (settings.window_height / 100) * percentage