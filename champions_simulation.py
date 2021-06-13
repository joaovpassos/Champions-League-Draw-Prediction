#------------------------------------------------------------------------------------------
#THIS IS A CODE THAT PREDICT THE CHANCES OF THE MATCHS IN UEFA CHAMPIONS LEAGUE ROUND OF 16
#------------------------------------------------------------------------------------------
from random import shuffle
from itertools import count, groupby
import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from seaborn import palettes
from seaborn import colors
from seaborn.palettes import color_palette

#TIMES THAT THE SIMULATION IS EXECUTED
simulacoes = 10000000

#DATA FROM THE TEAMS
#------------------------------------------
#THIS IS THE LIST OF THE FIRST PLACES WITH THE INFORMATION OF THE COUNTRY, GROUP AND PLACING IN THE GROUP
info_1 = [
    ['Bayern M.','Alemanha','A',1],
    ['R. Madrid','Espanha','B',1],
    ['M. City','Inglaterra','C',1],
    ['Liverpool','Inglaterra','D',1],
    ['Chelsea','Inglaterra','E',1],
    ['B. Dortmund','Alemanha','F',1],
    ['Juventus','Italia','G',1],
    ['PSG','França','H',1]
]

#THIS IS THE LIST OF THE SECOND PLACES WITH THE INFORMATION OF THE COUNTRY, GROUP AND PLACING IN THE GROUP
info_2 = [
    ['A. Madrid','Espanha','A',2],
    ['Borussia M.','Alemanha','B',2],
    ['Porto','Portugal','C',2],
    ['Atalanta','Italia','D',2],
    ['Sevilla','Espanha','E',2],
    ['Lazio','Italia','F',2],
    ['Barcelona','Espanha','G',2],
    ['RB Leipzig','Alemanha','H',2]
]

Primeiros = [i[0] for i in info_1] #IT TAKES ONLY THE NAME OF THE TEAMS IN FIRST PLACE OF EACH GROUP
Segundos = [i[0] for i in info_2] #IT TAKES ONLY THE NAME OF THE TEAMS IN SECOND PLACE OF EACH GROUP
#------------------------------------------

#GENERATING THE SIMULATION OF THE MATCHES
#------------------------------------------
partidas = []

contador = 0
vezes = 0
while vezes < simulacoes:
    correto = False
    while not correto:
        shuffle(info_1) #SHUFFLE THE TEAMS IN INFO_1
        shuffle(info_2) #SHUFFLE THE TEAMS IN INFO_2
        i = 0
        jogos_possiveis = 0
        while i < 8:
            if info_1[i][1] == info_2[i][1] or info_1[i][2] == info_2[i][2]: #DISTINGUISHING TEAMS FROM THE SAME GROUP AND SAME COUNTRY
                correto = False #IN THIS DRAW, THEY CAN'T FACE A TEAM FROM THE SAME COUNTRY OR FROM THE SAME GROUP IN GROUP STAGE
            else:
                jogos_possiveis += 1
            i += 1
        if jogos_possiveis == 8: #POSSIBLE SIMULATION
            correto = True
        contador += 1

    i = 0
    if correto == True:
        while i < 8:
            partida = [info_1[i][0],info_2[i][0]] #ORGANIZING THE MATCHES
            partidas.append(partida)            
            i += 1
    vezes += 1
#------------------------------------------

#COUNTING THE MATCHES
#------------------------------------------
jogos = []
i = 0
while i < 8:
    j = 0
    while j < 8:
        partidas_igual = partidas.count([Primeiros[i], Segundos[j]]) #COUNTING THE FREQUENCY OF EACH MATCH
        jogos.append(partidas_igual)
        j += 1
    i += 1
#------------------------------------------

#CREATING THE HEATMAP
#------------------------------------------
df = DataFrame(index=Segundos, columns=Primeiros) #CREATING THE TABLE WITH THE NUMBERS OF THE FREQUENCY OF EACH MATCH
i = 0
while i < 8: #INSERTING DATA IN THE TABLE
    df.iloc[:,i] = 100*(np.array(jogos[i+7*i:i+7*i+8])/simulacoes) #RELATIVE FREQUENCY OF THE MATCHES
    i += 1
print(df) #SHOW A DEMONSTRATION OF THE TABLE IN TERMINAL
fig = plt.figure(figsize = (10,10)) #DEFINE THE SIZE OF THE TABLE
plt.xticks(rotation=0) #SET TO SHOW THE TEXT IN THE HORIZONTAL
plt.figtext(0.125,0.925,'Simulation of the matches in Champions League', fontsize=20, ha='left') #TITLE
plt.figtext(0.125,.8975,f'This percentage was generated from a total of {simulacoes} simulations.', fontsize=10, ha='left', c='grey') #SUBTITLE
x = sns.heatmap(df, annot=True, cmap = 'YlGn', cbar=False) #CREATING THE HEATMAP
x.set_yticklabels(labels=Segundos, rotation=0) #SET THE Y AXIS TO SHOW IN THE HORIZONTAL 
plt.show() #GENERATES THE HEATMAP
#------------------------------------------