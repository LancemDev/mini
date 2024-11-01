from vpython import *

from globe import rotation_speed

canva = canvas(title="3D Objects", width=1200, height=800)

# Adjusted positions to balance objects around the x-axis

# mecury
mercury = sphere(pos=vector(-30, 0, 0), radius=0.75, color=color.white, texture=textures.rough)

# venus
venus = sphere(pos=vector(-27, 0, 0), radius=1.0, texture=textures.rock)

# earth
earth = sphere(pos=vector(-24, 0, 0), radius=1.25, texture=textures.earth)

# mars
mars = sphere(pos=vector(-20, 0, 0), radius=1.5, color=color.gray(0.5), texture=textures.stucco)

# jupiter
jupiter = sphere(pos=vector(-7, 0, 0), radius=10, texture=textures.wood)

# saturn
saturn = sphere(pos=vector(12, 0, 0), radius=6, color=color.gray(0.5), texture=textures.wood_old)

# uranus
uranus = sphere(pos=vector(20, 0, 0), radius=1.25, texture=textures.gravel)

# pluto
pluto = sphere(pos=vector(24, 0, 0), radius=0.5, color=color.gray(0.5), texture=textures.granite)

# Keep the canvas open and responsive
while True:
    rate(60)  # Keeps the scene interactive at 60 fps
