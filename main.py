from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()
ident(transform)
cstack=[]
cstack.append(transform)

parse_file('script', edges, polygons, cstack, screen, color )
