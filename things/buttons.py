from ursina import* 

class Voxel(Button):
	def __init__(self):
		super().__init__(
			parent = scene,
			position= (0,0,0),
			model='cube',
			origin_y=0.5,
			texture='white_cube',
			color=color.white,
			scale_z=20,
			scale_x=20,
			rotation=Vec3(-10,20,0),
			collider='box',
			)