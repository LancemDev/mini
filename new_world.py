#import libraries
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random
import math

noise = PerlinNoise(octaves=3, seed=random.randint(1, 1000))

#create an instance of the ursina app
app = Ursina()

#define game variables
selected_block = "grass"
in_rocket = False

#create player
player = FirstPersonController(
    mouse_sensitivity=Vec2(100, 100),
    position=(0, 5, 0)
)

block_textures = {
    "grass": load_texture("assets/textures/groundEarth.png"),
    "dirt": load_texture("assets/textures/groundMud.png"),
    "stone": load_texture("assets/textures/wallStone.png"),
    "bedrock": load_texture("assets/textures/stone07.png")
}

class Block(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position=position,
            model="assets/models/block_model",
            scale=1,
            origin_y=-0.5,
            texture=block_textures.get(block_type),
            collider="box"
        )
        self.block_type = block_type

mini_block = Entity(
    parent=camera,
    model="assets/models/block_model",
    scale=0.2,
    texture=block_textures.get(selected_block),
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)

#create the ground
min_height = -5
for x in range(-10, 10):
    for z in range(-10, 10):
        height = noise([x * 0.02, z * 0.02])
        height = math.floor(height * 7.5)
        for y in range(height, min_height - 1, -1):
            if y == min_height:
                block = Block((x, y + min_height, z), "bedrock")
            elif y == height:
                block = Block((x, y + min_height, z), "grass")
            elif height - y > 2:
                block = Block((x, y + min_height, z), "stone")
            else:
                block = Block((x, y + min_height, z), "dirt")

# Create Earth and Moon
earth = Entity(
    model='sphere',
    texture='assets/textures/earth_texture.png',  # Use your own texture
    scale=2,
    position=(0, 10, -30)  # Positioned high in the sky
)

moon = Entity(
    model='sphere',
    texture='assets/textures/moon_texture.png',  # Use your own texture
    scale=1,
    position=(5, 12, -35)  # Positioned to the side of the Earth
)

# Create Rocket
rocket = Entity(
    model='assets/models/rocket_model',  # Use your own rocket model
    position=(0, 5, 0),
    scale=0.5,
    collider='box'
)

def enter_rocket():
    global in_rocket
    in_rocket = not in_rocket
    player.position = rocket.position + Vec3(0, 2, 0) if in_rocket else (0, 5, 0)
    if in_rocket:
        print("Entered the rocket! Press 1 to go to Earth, 2 for Moon.")

def travel_to(destination):
    if destination == 'earth':
        player.position = earth.position + Vec3(0, 2, 0)
    elif destination == 'moon':
        player.position = moon.position + Vec3(0, 2, 0)

def input(key):
    global selected_block
    #place block
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            block = Block(hit_info.entity.position + hit_info.normal, selected_block)
    #delete block
    if key == "right mouse down" and mouse.hovered_entity:
        if not mouse.hovered_entity.block_type == "bedrock":
            destroy(mouse.hovered_entity)
    #change block type
    if key == "1":
        selected_block = "grass"
    if key == '2':
        selected_block = "dirt"
    if key == '3':
        selected_block = "stone"
    # Enter rocket
    if key == 'e':
        enter_rocket()
    # Travel
    if in_rocket:
        if key == '1':
            travel_to('earth')
        if key == '2':
            travel_to('moon')

def update():
    mini_block.texture = block_textures.get(selected_block)

#run the app
app.run()
