from math import *

tringle_sides = [int(input()) for _ in range(3)]

sq = (tringle_sides[0] + 
      tringle_sides[1] + 
      tringle_sides[2])

area = sqrt(sq * (sq - tringle_sides[0])
            * (sq - tringle_sides[1]) *
            sq - tringle_sides[2])
