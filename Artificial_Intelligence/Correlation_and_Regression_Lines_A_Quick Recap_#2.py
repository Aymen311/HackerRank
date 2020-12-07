import math
x = [15,12,8,8,7,7,7,6,5,3]
y = [10,25,17,11,13,17,20,13,9,15]

slope_xy = sum([ai*bj for ai,bj in zip(x,y)])
slope_x_slope_y = sum(x)*sum(y)
slope_xx = sum([ai**2 for ai in x])
slope_x_slope_q = sum(x)*sum(x)

print(round((10*slope_xy - slope_x_slope_y)/float(10*slope_xx - slope_x_slope_q),3))
