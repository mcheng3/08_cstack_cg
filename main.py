from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []

cstack=[]
cstack.append(ident(new_matrix()))

parse_file('script', edges, polygons, cstack, screen, color )
