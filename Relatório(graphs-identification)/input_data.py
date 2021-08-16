    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import pandas as pd
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import scale


    img=mpimg.imread('t2.PNG')

    eps=0.15
    pmin=25
     
    # Obtendo dados da imagem

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
    data = {'R':vec_r,'G':vec_g, 'B':vec_b,'alpha':vec_alpha,'x':vec_x,'y':vec_y}
    df = pd.DataFrame (data, columns = ['R','G','B','alpha','x','y'])