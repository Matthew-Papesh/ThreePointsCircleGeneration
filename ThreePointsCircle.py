import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

def main():
    # given points:
    (x_0, y_0) = (0.0,0.0)
    (x_1, y_1) = (0.5,0.2)
    (x_2, y_2) = (0.8,1.0)
    
    # compute coefficients
    A = -(pow(x_0, 2.0)*y_1 - pow(x_0, 2.0)*y_2 - pow(x_1, 2.0)*y_0 + pow(x_1, 2.0)*y_2 + pow(x_2, 2.0)*y_0 - pow(x_2, 2.0)*y_1 + pow(y_0, 2.0)*y_1 - pow(y_0, 2.0)*y_2 - y_0*pow(y_1, 2.0) + y_0*pow(y_2, 2.0) + pow(y_1, 2.0)*y_2 - y_1*pow(y_2, 2.0))/(2*(x_0*y_1 - x_1*y_0 - x_0*y_2 + x_2*y_0 + x_1*y_2 - x_2*y_1))
    B = -(- pow(x_0, 2.0)*x_1 + pow(x_0, 2.0)*x_2 + x_0*pow(x_1, 2.0) - x_0*pow(x_2, 2.0) + x_0*pow(y_1, 2.0) - x_0*pow(y_2, 2.0) - pow(x_1, 2.0)*x_2 + x_1*pow(x_2, 2.0) - x_1*pow(y_0, 2.0) + x_1*pow(y_2, 2.0) + x_2*pow(y_0, 2.0) - x_2*pow(y_1, 2.0))/(2*(x_0*y_1 - x_1*y_0 - x_0*y_2 + x_2*y_0 + x_1*y_2 - x_2*y_1))
    C = (- pow(x_0, 2.0)*x_1*y_2 + pow(x_0, 2.0)*x_2*y_1 + x_0*pow(x_1, 2.0)*y_2 - x_0*pow(x_2, 2.0)*y_1 + x_0*pow(y_1, 2.0)*y_2 - x_0*y_1*pow(y_2, 2.0) - pow(x_1, 2.0)*x_2*y_0 + x_1*pow(x_2, 2.0)*y_0 - x_1*pow(y_0, 2.0)*y_2 + x_1*y_0*pow(y_2, 2.0) + x_2*pow(y_0, 2.0)*y_1 - x_2*y_0*pow(y_1, 2.0))/(x_0*y_1 - x_1*y_0 - x_0*y_2 + x_2*y_0 + x_1*y_2 - x_2*y_1)
    
    # computed circle properties
    x_ICC = -A
    y_ICC = -B
    R = pow(pow(A, 2.0) + pow(B, 2.0) - C, 0.5)
    
    # view computed circle plot with matplotlib
    figure, axis = plt.subplots()
    circle = patches.Circle((x_ICC, y_ICC), radius=R)
    axis.add_patch(circle)
    
    plt.plot((x_0, x_1, x_2), (y_0, y_1, y_2), 'o', color='r')
    
    axis.set_aspect('equal')
    axis.set_xlim((-5.0, 5.0))
    axis.set_ylim((-5.0, 5.0))
    
    # print computed results 
    print('Radius = ' + str(format(R, '.3')) + ', ICC = ( ' + str(format(x_ICC, '.3')) + ', ' + str(format(y_ICC, '.3')) + ' )')
    
    plt.title('Plotted Circle From Three Points')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(visible=True)
    plt.show()
    
main()