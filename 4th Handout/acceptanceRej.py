import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import pi
import scipy.stats as stats


def normalRandomVariable(n):
    fileGenerator = open("generator.dat","w+")
    fileGenerator.write("#DADOS AMOSTRA DO GERADOR\n")
    fileGenerator.write("#X     #Y\n")
    fileNormalFunction = open("normalRandomVariable.dat","w+")
    fileNormalFunction.write("#FUNCAO DE UMA VA NORMAL\n")
    fileNormalFunction.write("#X     #Y\n")
    pmfYCol = []
    Tries = 0
    for i in range(n):
        acceptance = True
        tries = 0;
        normalRandomVariable = np.random.normal(0,1)
        fileNormalFunction.write(str(normalRandomVariable)+"     "+str(2.0*np.exp(-((normalRandomVariable*1.0)**2.0)/2.0)/((2*pi)**(0.5)))+"\n")
        while acceptance:
            uniformRandomVariable1 = np.random.uniform(0,1)
            uniformRandomVariable2 = np.random.uniform(0,1)
            pmfY = np.random.exponential(1)
            g = np.exp(-(((pmfY*1.0)-1.0)**2.0)/2.0)
            gN = 2.0*np.exp(-((pmfY*1.0)**2.0)/2.0)/((2*pi)**(0.5))
            tries+=1
            if uniformRandomVariable1 <= g:
                if uniformRandomVariable2 > 0.5:
                    fileGenerator.write(str(pmfY)+"     "+str(gN)+"\n")
                    pmfYCol += [pmfY]
                else: 
                    fileGenerator.write(str(-pmfY)+"     "+str(gN)+"\n")
                    pmfYCol += [-pmfY]
                acceptance = False
        Tries+=tries
    stats.probplot(pmfYCol, dist="norm", plot=plt)
    plt.savefig('QQplot.png')
    print "Media do numero de iteracoes ate que uma amostra valida seja gerada pelo algoritmo: ", Tries*1.0/n,"\n"+"Valor teorico da media:",(2.0*np.exp(1.0)/pi)**(1.0/2.0)



