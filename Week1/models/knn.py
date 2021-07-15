"""
simple models
"""
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class Models:

    def __init__(self,data):
        self.data=data

    def scaleData(self):
        ss=StandardScaler()
        return ss.fit_transform(self.data)

    def knnCluster(self,cluster):
        
        kmean=KMeans(n_clusters=cluster)
        return kmean.fit(self.scaleData())

    def modelMetrics(self):

        pass 
    def visualizePlot(self,cluster,color,**kwargs):
        kmean=KMeans(n_clusters=cluster)
        preds=kmean.fit_predict(self.scaleData())
        plt.figure(figsize=(15,8))
        plt.scatter(self.scaleData[:,0],self.scaleData[:,1],c=preds)

        plt.scatter(kmean.cluster_centers_[:,0],kmean.cluster_centers_[:,1],c=color)
        plt.show()

        


    