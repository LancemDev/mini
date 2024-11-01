from vpython import *
import random

canva = canvas(width=2000, height=1000)

# Globe
globe = sphere(pos=vector(1, 0, 0), radius=6, texture=textures.earth, shininess=15)
rotation_speed = 0.002

# moon
moon = sphere(pos=vector(-10, 5, -5), radius=1.75, color=color.white, texture=textures.rough, shininess=100)

# Function to create stars
def create_stars(num_stars):
    stars = []
    for _ in range(num_stars):
        # Random position for each star
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-10, 10)
        # Create a small sphere for the star
        star = sphere(pos=vector(x, y, z), radius=0.025, color=color.white)
        stars.append(star)
    return stars

# Create stars in the background
num_stars = 500 
stars = create_stars(num_stars)


# Keep the canvas open and responsive
while True:
    rate(60)  # Keeps the scene interactive at 60 fps
    globe.rotate(angle = rotation_speed, axis=vector(0, 1, 0))
    moon.rotate(angle=rotation_speed, axis=vector(0, 1, 0))