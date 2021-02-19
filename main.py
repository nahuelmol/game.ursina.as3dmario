from ursina import *
from things.buttons import*
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()


camera.orthographic = True 
camera.fov = 20

class PlayerCube(Entity):
	def __init__(self):
		super().__init__(
			texture='white_cube',
			model='cube',
			color=color.magenta,
			rotation=Vec3(-10,20,0),
			)
	
ground = Entity(model='cube',)

voxel = Voxel()

player = PlayerCube()


def update():
	player.x += held_keys['d']*1
	player.x -= held_keys['a']*1
	player.y += held_keys['w']*1
	player.y -= held_keys['s']*1

	print(player.position.y)

	if player.position.y < 0:
		player.position = Vec3(player.position.x,0,0)

app.run()