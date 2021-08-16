    ##
    ##  CRIANDO SAIDA DE DADOS
    ##
    n_points=50

    # Obtendo valores de x_barra
    x_points = np.arange(0, max_x+max_x/n_points, max_x/(n_points))
    x_values=[]
    for i in range(n_points):
      x_values.append(x_points[i]+(x_points[i+1]-x_points[i])/2.0)

    # Obtendo valores de y_barra para cada serie
    y_values=[]
    for serie in range(len(series)):
      y_local=[]
      for i in range(n_points):
        dentro = s_graph[serie].x_real.between(x_points[i],x_points[i+1])
        y_local.append(np.mean(s_graph[serie][dentro].y_real))
      y_values.append(y_local)

    # Criando string de saida de dados
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

    # Gravando saida de dados em um arquivo TXT
    saida = open("grafico.txt","w")
    saida.write(output)
    saida.close()


    print("End of code")
    pass