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
        df=self.data.dropna(thresh=self.data.shape[0]*threshold,how='all',axis=1)
       

        return df
    
    def dropDuplicates(self):
        print("Dropping Duplicates...\n")
        df=self.data.drop_duplicates()
        dupCount=len(self.data)-len(self.data.drop_duplicates())
        print("There are {}  duplicates in the dataset".format(dupCount))

        print("Done Dropping duplicates!")
        return df


    def imputeColumnsMean(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with mean values of the feature")
        data=self.data[cols].fillna(self.data[cols].mean(),inplace=True)

        print ("Done......!!!")

        return data
    def imputeColumnsMode(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with mode values of the feature")
        data=self.data[cols].fillna(self.data[cols].mode(),inplace=True)

        print ("Done......!!!")

        return data
    def imputeColumnsMedian(self,cols):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with median values of the feature")
        data=self.data[cols].fillna(self.data[cols].median(),inplace=True)

        print ("Done......!!!")

        return data    

    def outlierdetect(self):
        #this function detects and eliminates outliers using the z-score method
        #any value that has a z-score of 3 or higher will be tretated as an outlier and hence dropped
        pass
      


