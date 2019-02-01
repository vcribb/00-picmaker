file = open('homework.ppm', 'w')
file.write('P3\n500 500\n255\n')
for x in range(500):
    for y in range(500):
        file.write('255 '+str(y)+' '+str(x)+' ')
    file.write('\n')
file.close()
