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