# Machine-learning project

This project applies the DBScan clustering technique to identify graph values from an image (format PNG).

The user must find the best parameters eps and min_samples for the clusterization to identify each series independently from the axis lines. 
With that, the user will see the clusters formed in an image on screen. Then, the user must inform which cluster numbers represent the axis and 
which ones represent desired series. The user must also inform the maximum values of the axis x and y. 
Considering that information, the script will write a txt file (graph.txt) containing x and y values of each one of the series assessed as desired by the user.

Examples of applications can be found on the XLSX file and PNG figures inside the project. The examples tested are: t2, t3 and t4. 

Limitations (future improvements): 
- Legend cannot be in the image (must be left outside of the graph)
- Series with black lines cannot intercept the axis lines (the DBScan algorithm won't be able to separate this line from the axis lines) 
