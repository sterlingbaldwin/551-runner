from subprocess import Popen, PIPE, STDOUT
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import json

cores = [2, 4, 8, 20]
runs = 5
a = 100
b = 600
output = []
if not os.path.exists('./config.json'):
    p = Popen(['./serial'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    n = p.communicate()[0]
    config = {'n' : n}
    with open('./config.json', 'w') as outfile:
        json.dump(config, outfile)
else:
    with open('./config.json', 'r') as infile:
        config = json.load(infile)
        n = config['n']



for i in cores:
    for j in range(runs):
        run_input = str(a) + ' ' + str(b) + ' ' + str(i + j)
        p = Popen(['./parallel'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        outdata = int(p.communicate(input=run_input)[0])
        output.append(outdata)


plt.plot(range(len(output)), output, 'ro')
plt.show()
