from loaddata import ReadData
from aggregarefunctions import aggregateClass
from eda import EDA


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
        numerCols=['Avg RTT DL (ms)','Avg RTT UL (ms)','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)','DL TP < 50 Kbps (%)','50 Kbps < DL TP < 250 Kbps (%)','250 Kbps < DL TP < 1 Mbps (%)','DL TP > 1 Mbps (%)','UL TP < 10 Kbps (%)','10 Kbps < UL TP < 50 Kbps (%)','50 Kbps < UL TP < 300 Kbps (%)','UL TP > 300 Kbps (%)','Activity Duration DL (ms)','Activity Duration UL (ms)','Dur. (ms).1','Nb of sec with Vol DL < 6250B','Nb of sec with Vol UL < 1250B','Social Media DL (Bytes)','Social Media DL (Bytes)',
    'Social Media UL (Bytes)','Google DL (Bytes)','Google UL (Bytes)','Email DL (Bytes)','Email UL (Bytes)','Youtube DL (Bytes)','Youtube UL (Bytes)','Netflix DL (Bytes)','Netflix UL (Bytes)','Gaming DL (Bytes)','Gaming UL (Bytes)','Other DL (Bytes)','Other UL (Bytes)','Total UL (Bytes)','Total DL (Bytes)','Social Media Total (Bytes)','Google Total (Bytes)','Email Total (Bytes)','Youtube Total (Bytes)','Netflix Total (Bytes)','Gaming Total (Bytes)','Other Total (Bytes)']
        for column in numerCols:
            print ("Imputing missing rows of {} column with mean values of the feature".format(column))
            data[column].fillna(data[column].mean(),inplace=True)
            print ("Done......!!!")
        for column in catCols:
            print ("Imputing missing rows of {} column with mode values of the feature".format(column))
            data[column].fillna(data[column].value_counts().index[0],inplace=True)
            print ("Done......!!!")

       
        

        return data 
    def checkforNulls(self):
        
            
        cleanData=self.cleanOutliers()
        dataFrame=EDA(cleanData)
        
        cleanReport=dataFrame.calculateMissingValues()

        return cleanReport

    def aggregation(self):
        data=self.cleanOutliers()
        aggInstance=aggregateClass(data)
        avgRTT=aggInstance.aggregateSumOne('MSISDN/Number','Avg RTT DL (ms)','Avg RTT UL (ms)',10,'Avg RTT DL (ms)')
        #avgRTTUp=aggInstance.aggregateSumTwo('MSISDN/Number','Avg RTT UL (ms)','Avg RTT UL (ms)',10)
        handsetType=aggInstance.aggregateCategoricalTwo('MSISDN/Number','Handset Type')
        #avgTCP=aggInstance.aggregateCategoricalSumOne('MSISDN/Number','TCP DL Retrans. Vol (Bytes)','TCP UL Retrans. Vol (Bytes)',10,'TCP DL Retrans. Vol (Bytes)')
        #avgTTP=aggInstance.aggregateSumOne('MSISDN/Number','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)',10,'Avg Bearer TP DL (kbps)')
        return avgRTT,handsetType
    def calculateValueCounts(self):
        data=self.cleanOutliers()
        freqInstance=aggregateClass(data)
        tcpTop=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10,ascending=False)
        tcpBottom=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10)

        tcpULTop=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10,ascending=False)
        tcpULBot=freqInstance.calculateAscent('TCP DL Retrans. Vol (Bytes)',10)
        
        rttULTop=freqInstance.calculateAscent('Avg RTT UL (ms)',10,ascending=False)
        rttULBot=freqInstance.calculateAscent('Avg RTT UL (ms)',10)

        rttDLTop=freqInstance.calculateAscent('Avg RTT DL (ms)',10,ascending=False)
        rttDLBot=freqInstance.calculateAscent('Avg RTT DL (ms)',10)


        tpDLTop=freqInstance.calculateAscent('Avg Bearer TP DL (kbps)',10,ascending=False)
        tpDLBot=freqInstance.calculateAscent('Avg Bearer TP DL (kbps)',10)

        tpULTop=freqInstance.calculateAscent('Avg Bearer TP UL (kbps)',10,ascending=False)
        tpULBot=freqInstance.calculateAscent('Avg Bearer TP UL (kbps)',10)

        tcpFreq=freqInstance.calculateFrequency()
        rttFreq=freqInstance.calculateFrequency()






        

        pass



        




if (__name__ == '__main__'):
    
    dataFrame=CLEANDATA('../data/Processed_data.csv')
   
    # dataFrame=dataFrame.cleanOutliers(['Avg RTT DL (ms)','Avg RTT UL (ms)','Avg Bearer TP DL (kbps)','Avg Bearer TP UL (kbps)','DL TP < 50 Kbps (%)','50 Kbps < DL TP < 250 Kbps (%)','250 Kbps < DL TP < 1 Mbps (%)','DL TP > 1 Mbps (%)','UL TP < 10 Kbps (%)','10 Kbps < UL TP < 50 Kbps (%)','50 Kbps < UL TP < 300 Kbps (%)','UL TP > 300 Kbps (%)','Activity Duration DL (ms)','Activity Duration UL (ms)','Dur. (ms).1','Nb of sec with Vol DL < 6250B','Nb of sec with Vol UL < 1250B','Social Media DL (Bytes)','Social Media DL (Bytes)',
    # 'Social Media UL (Bytes)','Google DL (Bytes)','Google UL (Bytes)','Email DL (Bytes)','Email UL (Bytes)','Youtube DL (Bytes)','Youtube UL (Bytes)','Netflix DL (Bytes)','Netflix UL (Bytes)','Gaming DL (Bytes)','Gaming UL (Bytes)','Other DL (Bytes)','Other UL (Bytes)','Total UL (Bytes)','Total DL (Bytes)','Social Media Total (Bytes)','Google Total (Bytes)','Email Total (Bytes)','Youtube Total (Bytes)','Netflix Total (Bytes)','Gaming Total (Bytes)','Other Total (Bytes)'],['Handset Manufacturer','Handset Type','Last Location Name','IMSI','MSISDN/Number','IMEI'])
    dataFrame=dataFrame.aggregation()
    print (dataFrame)

