#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Antonio
#
# Created:     29/06/2021
# Copyright:   (c) Antonio 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import pandas as pd
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import scale


    img=mpimg.imread('t2.PNG')

    eps=0.15
##    eps=0.2  ## OBS: Usar no t3
    pmin=25

    # Pegando dados da imagem

    vec_x=[]
    vec_y=[]
    vec_r=[]
    vec_g=[]
    vec_b=[]
    vec_alpha=[]

    for i in range(len(img)):
        for j in range(len(img[i])):
            a=img[i,j]
            grava=True
            if (a[0]==1.0 and a[1]==1.0 and a[2]==1.0):
                grava=False
            if (grava):
                vec_x.append(float(j))
                vec_y.append(float(i))
                vec_r.append(a[0])
                vec_g.append(a[1])
                vec_b.append(a[2])
                vec_alpha.append(a[3])

    ## Invertendo valores de y
    y_max=float(len(img))
    print(vec_y[5],vec_y[500],vec_y[1000])

    for i in range(len(vec_y)):
      vec_y[i] = y_max - vec_y[i]

    # Colocando dados em data_frame
    data = {'R':vec_r,'G':vec_g, 'B':vec_b, 'alpha':vec_alpha,'x':vec_x,'y':vec_y}
    df = pd.DataFrame (data, columns = ['R','G','B','alpha','x','y'])
    print(df.head())
    print(df.tail())

##    ## Aplicando dbscan
##    X = np.column_stack((data['R'],data['G'],data['B'],data['alpha']))

    ## Aplicando dbscan com x,y e cores
    data1 = scale(df)
    X = np.column_stack((data1[:,0],data1[:,1],data1[:,2],data1[:,3],data1[:,4],data1[:,5]))

    clustering = DBSCAN(eps=eps, min_samples=pmin).fit(X)
    labels = clustering.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print("Number of obtained clusters:",n_clusters_)

    ## Fazendo dataframe com os labels
    data1 = {'R':vec_r,'G':vec_g, 'B':vec_b, 'alpha':vec_alpha, 'labels':labels ,'x':vec_x,'y':vec_y}
    df_cluster = pd.DataFrame (data1, columns = ['R','G','B','alpha','labels','x','y'])
    df_cluster1 = df_cluster[df_cluster['labels']!=-1]
    print(df_cluster1.head())
    print(df_cluster1.tail())

    ## Plotando grupos da clusterizacao
    groups = df_cluster1.groupby('labels')
    for name, group in groups:
        plt.plot(group['x'], group['y'], marker="o", linestyle="", label=name)
    plt.legend()
    plt.show()

    ## Getting the axis from user
    x,y = input("Digite qual o grupo contem os eixos x e y:").split()
    x = int(x)
    y = int(y)

    ## Getting series data from user
    ler = True
    series=[]
    while (ler):
      a=input("Digite qual grupo corresponde uma serie do grafico: (-1 para parar)")
      a=int(a)
      if (a==-1):
        ler = False
      else:
        series.append(a)

    ## Getting axis limits
    max_x,max_y = input("Digite valor maximo dos eixos x e y:").split()
    max_x=float(max_x)
    max_y=float(max_y)

    # Pegando eixos
    axis = df_cluster1[(df_cluster1['labels']==x) | (df_cluster1['labels']==y)]
    orig_x=min(axis.x)
    orig_y=min(axis.y)

    max_x_pixel=max(axis.x)
    max_y_pixel=max(axis.y)

    # Pegando Series
    s_graph=[]
    for i in range(len(series)):
      s_graph.append(df_cluster1[df_cluster1['labels']==series[i]])

    ## Calculando x_real e y_real
    for i in range(len(series)):
      s_graph[i]['x_real'] = (max_x/(max_x_pixel-orig_x))*(s_graph[i]['x']-orig_x)
      s_graph[i]['y_real'] = (max_y/(max_y_pixel-orig_y))*(s_graph[i]['y']-orig_y)

    ##  CRIANDO SAIDA DE DADOS
    ##
    n_points=50

    x_points = np.arange(0, max_x+max_x/n_points, max_x/(n_points))
    x_values=[]
    for i in range(n_points):
      x_values.append(x_points[i]+(x_points[i+1]-x_points[i])/2.0)

    y_values=[]
    for serie in range(len(series)):
      y_local=[]
      for i in range(n_points):
        dentro = s_graph[serie].x_real.between(x_points[i],x_points[i+1])
        y_local.append(np.mean(s_graph[serie][dentro].y_real))
      y_values.append(y_local)

    output=""
    output+='x     '
    for i in range(len(series)):
      output+='    Serie_{}    '.format(series[i])
    output+='\n'

    for i in range(n_points):
      output+='{:.6f}   '.format(x_values[i])
      for j in range(len(series)):
        if (not np.isnan(y_values[j][i])):
          output+='{:12f}  '.format(y_values[j][i])
        else:
          output+='     -        '
      output+='\n'

    saida = open("grafico.txt","w")
    saida.write(output)
    saida.close()


    print("End of code")
    pass

if __name__ == '__main__':
    main()
