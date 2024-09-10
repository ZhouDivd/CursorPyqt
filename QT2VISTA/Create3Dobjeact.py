import pyvista as pv


# Create a cylinder
def create_cylinder(radius, height, resolution):
    cylinder = pv.Cylinder(radius=radius, height=height, resolution=resolution)
    return cylinder
# Create a sphere
def create_sphere(radius, resolution):
    sphere = pv.Sphere(radius=radius, center=(0, 0, 0))
    return sphere
# Create a cone
def create_cone(radius, height, resolution):
    cone = pv.Cone(radius=radius, height=height, resolution=resolution)
    return cone
# Create a Box
def create_box(length, width, height, resolution):
    box = pv.Box(bounds=[length/2, -length/2, width/2, -width/2, height/2, -height/2], level=0,quads=True)
    return box

# Create a pyramid
def create_pyramid(base_length, height, resolution):
    pyramid = pv.Pyramid(base_length=base_length, height=height, resolution=resolution)
    return pyramid
# Create a cube
def create_cube(length, resolution):
    cube = pv.Cube(length=length, resolution=resolution)
    return cube
# Create a torus knot
def create_torus_knot(p, q, radius, tube_radius, resolution):
    torus_knot = pv.TorusKnot(p=p, q=q, radius=radius, tube_radius=tube_radius, resolution=resolution)
    return torus_knot
