import matplotlib.pyplot as plt
import math
g = 9.81
while True:
    try:
        x = []
        y = []
        angle = int(input('Input the angle :'))
        vo = int(input('Input the initial speed:'))
        rad = (angle/180)*math.pi
        soh = math.sin(rad)
        cah = math.cos(rad)
        t_max = 2*vo*soh/g
        t = 0
        while True:
            position_x = vo*cah*t
            position_y = (vo*soh*t) - (g*0.5*t*t)
            x.append(position_x)
            y.append(position_y)
            t +=0.001
            if t_max > t :
                continue
            else:
                break
        print(x,y)
        plt.plot(x,y)
        conti = input('Do you wish to continue(y/n)?').lower()
        if conti == 'y':
            continue
        else:
            break

    except:
        print('Please input in integer!!')

plt.show()


