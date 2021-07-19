"""
This script contains funtions to fill null values and perform univariate analysis

"""
import pandas as pd

class EDA:

    def __init__(self,data):
        self.data=data

        

        

    
    def calculateMissingValues(self):
        #we calculate the number of missing values in each row 
        # data=pd.read_excel(self.data)
        sumMissing=self.data.isna().sum()
        percentageMissing=sumMissing/len(self.data)*100

        missValues=pd.DataFrame(data=[sumMissing,percentageMissing])
        missValues=missValues.T 
        missValues.columns=['Total Missing','Percentage Missing']




        return missValues

    def aboveThresholdMissing(self,threshold):
        self.data.dropna(thresh=len(self.data) * threshold,inplace=True,axis=1)

       

        
    
    def dropDuplicates(self):
        print("Dropping Duplicates...\n")
        df=self.data.drop_duplicates()
        dupCount=len(self.data)-len(self.data.drop_duplicates())
        print("There are {}  duplicates in the dataset".format(dupCount))

        print("Done Dropping duplicates!")
        return df


    def imputeColumnsMean(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows of {} column with mean values of the feature".format(cols))
        data=self.data[cols].fillna(self.data[cols].mean(),inplace=True)

        print ("Done......!!!")

        return data
    def imputeColumnsMode(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with mode values of the feature")
        data=self.data[cols].fillna(self.data[cols].value_counts().index[0],inplace=True)

        print ("Done......!!!")

        return data
    def imputeColumnsMedian(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with median values of the feature")
        data=self.data[cols].fillna(self.data[cols].median(),inplace=True)

        print ("Done......!!!")

        return data   
     
    def forwardFill(self,cols):
        print ("Imputing using forward fill...")
        data=self.data[cols].fillna(method='ffill',inplace=True)
        print("Done")
        return data

    def backwardFill(self,cols):
        print ("Imputing using backward fill...")
        data=self.data[cols].fillna(method='bfill',inplace=True)
        print("Done")
        return data

    def outlierdetect(self):
        print("Getting numerical features..\n")

        numCols=self.data.select_dtypes(exclude=['object'])
        numCols.drop(labels=['IMSI','MSISDN/Number','IMEI'],inplace=True,axis=1)
        #'Decile Class','Month','Day','Year','Hour'
        print ("Detecting outliers..\n")
        for cols in numCols:
            print("Calculating limits \n")
            upperLimit=self.data[cols].mean()+3*self.data[cols].std()
            lowerLimit=self.data[cols].mean()-3*self.data[cols].std()

            self.data=self.data[(self.data[cols]<upperLimit)&(self.data[cols]>lowerLimit)]

        print ("Sorted outliers...\n")
        return self.data 



        
    def convertToDT(self,cols):
        print("Converting {} column to date time format".format(cols))
        self.data[cols]=pd.to_datetime(self.data[cols])
        print("Done..Here's the new datset")

        return self.data
    def dateColsFE(self,cols):

        pass
      


