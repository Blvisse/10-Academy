from loaddata import ReadData
from aggregarefunctions import aggregateClass
from eda import EDA
import pandas as pd
import numpy as np


class CLEANDATA:

    def __init__(self,path):
        self.path=path

    def readDataFrame(self):
        dataRead=ReadData(self.path)
        data=dataRead.readCsv()

        return data 

    def cleanOutliers(self):
        data=self.readDataFrame()
        catCols=['Handset Manufacturer','Handset Type','Last Location Name','IMSI','MSISDN/Number','IMEI']
        numerCols=['TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)','Avg RTT DL (ms)','Avg RTT UL (ms)','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)','Activity Duration DL (ms)','Activity Duration UL (ms)','Dur. (ms).1','Social Media DL (Bytes)','Social Media DL (Bytes)',
    'Social Media UL (Bytes)','Google DL (Bytes)','Google UL (Bytes)','Email DL (Bytes)','Email UL (Bytes)','Youtube DL (Bytes)','Youtube UL (Bytes)','Netflix DL (Bytes)','Netflix UL (Bytes)','Gaming DL (Bytes)','Gaming UL (Bytes)','Other DL (Bytes)','Other UL (Bytes)','Total UL (Bytes)','Total DL (Bytes)']
        for column in numerCols:
            print ("Imputing missing rows of {} column with mean values of the feature".format(column))
            data[column].fillna(data[column].mean(),inplace=True)
            print ("Done......!!!")
        for column in catCols:
            print ("Imputing missing rows of {} column with mode values of the feature".format(column))
            data[column].fillna(data[column].value_counts().index[0],inplace=True)
            print ("Done......!!!")

       
        print("Detecting Outliers...")
        print(data.shape)
        edaInstance=EDA(data)
        cleanData=edaInstance.outlierdetect()
        print (cleanData.shape)
        return cleanData 
    def checkforNulls(self):
        
            
        cleanData=self.cleanOutliers()
        dataFrame=EDA(cleanData)
        
        cleanReport=dataFrame.calculateMissingValues()

        return cleanReport

    def aggregation(self):
        data=self.cleanOutliers()
        aggInstance=aggregateClass(data)
        avgRTT=aggInstance.aggregateSumOne('MSISDN/Number','Avg RTT DL (ms)','Avg RTT UL (ms)',10,'Avg RTT DL (ms)')
        avgRTTUp=aggInstance.aggregateSumTwo('MSISDN/Number','Avg RTT UL (ms)','Avg RTT UL (ms)',10)
        handsetType=aggInstance.aggregateCategoricalTwo('MSISDN/Number','Handset Type')
        avgTCP=aggInstance.aggregateSumOne('MSISDN/Number','TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)',10,'TCP DL Retrans. Vol (Bytes)')
        avgTTP=aggInstance.aggregateSumOne('MSISDN/Number','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)',10,'Avg Bearer TP DL (kbps)')
        
        return avgRTT,handsetType,avgRTTUp,avgTCP,avgTTP
    def calculateValueCounts(self):
        data=self.cleanOutliers()
        freqInstance=aggregateClass(data)
        tcpTop=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10,ascending=False)
        tcpBottom=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10)

        tcpULTop=freqInstance.calculateAscent('TCP UL Retrans. Vol (Bytes)',10,ascending=False)
        tcpULBot=freqInstance.calculateAscent('TCP UL Retrans. Vol (Bytes)',10)
        
        rttULTop=freqInstance.calculateAscent('Avg RTT UL (ms)',10,ascending=False)
        rttULBot=freqInstance.calculateAscent('Avg RTT UL (ms)',10)

        rttDLTop=freqInstance.calculateAscent('Avg RTT DL (ms)',10,ascending=False)
        rttDLBot=freqInstance.calculateAscent('Avg RTT DL (ms)',10)


        tpDLTop=freqInstance.calculateAscent('Avg Bearer TP DL (kbps)',10,ascending=False)
        tpDLBot=freqInstance.calculateAscent('Avg Bearer TP DL (kbps)',10)

        tpULTop=freqInstance.calculateAscent('Avg Bearer TP UL (kbps)',10,ascending=False)
        tpULBot=freqInstance.calculateAscent('Avg Bearer TP UL (kbps)',10)

        # tcpFreq=freqInstance.calculateFrequency()
        # rttFreq=freqInstance.calculateFrequency()


        valueReport=[{'TCP Top DL Values':tcpTop,'TCP Bottom DL Value':tcpBottom,'TCp Top UL Values ':tcpULTop,'TCP Bottom UL Values':tcpULBot,'Avg Top RTT DL Values':rttDLTop,'Avg Bottom RTT DL Values':rttDLBot,'Avg Top RTT UL':rttULTop,'Avg Bott RTT UL':rttULBot,'Avg Throughput DL Top':tpDLTop}]
        dataFrame=zip(tcpTop,tcpBottom,tcpULTop,tcpULBot,rttDLTop,rttDLBot,rttULTop,rttULBot,tpDLTop,tpDLBot,tpULTop,tpULBot)
        cols=['TCP Top DL Values','TCP Bottom DL Values','TCP Top UL Values','TCP Bottom UL Values','Avg Top RTT DL Values','Avg Bot RTT DL Values','Avg Top RTT UL Values','Avg Bottom RTT UL Values','Avg Top Bearer TP DL (kbps)','Avg Bottom TP DL (kbps)','Avg Top Bearer TP UL (kbps)','Avg Bot Bearer TP UL (kbps)']
        data=pd.DataFrame(dataFrame,columns=cols)

        return data

 



        

    def reportsAgg(self):
        data=self.cleanOutliers()
        reportInstance=aggregateClass(data)

        self.data.groupby(['Handset Type']).agg({'Avg Bearer TP UL (kbps)':np.mean,'Avg Bearer TP DL (kbps)':np.mean})
        self.data.groupby(['Handset Type']).agg({'TCP DL Retrans. Vol (Bytes)':np.mean,'TCP UL Retrans. Vol (Bytes)':np.mean})

    def kmeansModel(self):
        from sklearn.preprocessing import StandardScaler
        from sklearn.cluster import KMeans
        from sklearn.decomposition import PCA
        import matplotlib.pyplot as plt
        data=self.cleanOutliers()
        aggInstance=aggregateClass(data)
        avgRTT=aggInstance.aggregateSumOne('MSISDN/Number','Avg RTT DL (ms)','Avg RTT UL (ms)',10,'Avg RTT DL (ms)')
        avgRTTUp=aggInstance.aggregateSumTwo('MSISDN/Number','Avg RTT UL (ms)','Avg RTT UL (ms)',10)
        handsetType=aggInstance.aggregateCategoricalTwo('MSISDN/Number','Handset Type')
        # avgTCP=aggInstance.aggregateCategorical('MSISDN/Number','TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)',10,'TCP DL Retrans. Vol (Bytes)')
        # avgTTP=aggInstance.aggregateSumOne('MSISDN/Number','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)',10,'Avg Bearer TP DL (kbps)')
        #avgRTT=aggInstance.aggregateSumOne('MSISDN/Number','Avg RTT DL (ms)','Avg RTT UL (ms)',10,'Avg RTT DL (ms)')

        data=data[['Handset Type','TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)','Avg RTT DL (ms)','Avg RTT UL (ms)','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)']]
        data=pd.get_dummies(data,columns=['Handset Type'])

        ss=StandardScaler()
        pca=PCA(n_components=2)
        
        transformedData=ss.fit_transform(data)
        pcaData=pca.fit_transform(transformedData)
        kmeans=KMeans(n_clusters=3)
        predictions=kmeans.fit_predict(pcaData)
        plt.figure(figsize=(15,8))
        plt.scatter(pcaData[:,0],pcaData[:,1],c=predictions)
        plt.show()

        return predictions







        

        



        




if (__name__ == '__main__'):
    
    dataFrame=CLEANDATA('../data/clustered3.csv')
   
    # dataFrame=dataFrame.cleanOutliers(['Avg RTT DL (ms)','Avg RTT UL (ms)','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)','DL TP < 50 Kbps (%)','50 Kbps < DL TP < 250 Kbps (%)','250 Kbps < DL TP < 1 Mbps (%)','DL TP > 1 Mbps (%)','UL TP < 10 Kbps (%)','10 Kbps < UL TP < 50 Kbps (%)','50 Kbps < UL TP < 300 Kbps (%)','UL TP > 300 Kbps (%)','Activity Duration DL (ms)','Activity Duration UL (ms)','Dur. (ms).1','Nb of sec with Vol DL < 6250B','Nb of sec with Vol UL < 1250B','Social Media DL (Bytes)','Social Media DL (Bytes)',
    # 'Social Media UL (Bytes)','Google DL (Bytes)','Google UL (Bytes)','Email DL (Bytes)','Email UL (Bytes)','Youtube DL (Bytes)','Youtube UL (Bytes)','Netflix DL (Bytes)','Netflix UL (Bytes)','Gaming DL (Bytes)','Gaming UL (Bytes)','Other DL (Bytes)','Other UL (Bytes)','Total UL (Bytes)','Total DL (Bytes)','Social Media Total (Bytes)','Google Total (Bytes)','Email Total (Bytes)','Youtube Total (Bytes)','Netflix Total (Bytes)','Gaming Total (Bytes)','Other Total (Bytes)'],['Handset Manufacturer','Handset Type','Last Location Name','IMSI','MSISDN/Number','IMEI'])
    
    modelCluster=dataFrame.kmeansModel()
    print (modelCluster)
    dataReport=dataFrame.calculateValueCounts()
    
    print(dataReport)
    aggReport=dataFrame.aggregation()
    print(aggReport)

