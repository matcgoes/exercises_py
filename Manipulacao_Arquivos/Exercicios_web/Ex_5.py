# Cada linha do arquivo lab.dat contém um par x,y de coordenadas. 
# Escreva uma função chamada plot_regressao que le os dados desse arquivo para 
# desenhar pontos e a reta que melhor aproxima os dados

import matplotlib.pyplot as plt

with open('lab.dat','r') as coordfile:
    coord_list = [s.split() for s in coordfile.readlines()]
    x = [int(el[0]) for el in coord_list]
    y = [int(el[1]) for el in coord_list]
    print(x)
    print(y)    
    plt.yscale('linear')
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.show()

