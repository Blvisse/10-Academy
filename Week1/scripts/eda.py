"""
This script contains funtions to fill null values and perform univariate analysis

"""


class EDA:

    def __init__(self,data):
        self.data=data

    def imputeColumns(self):
        #fill empty columns with the mean of the columns
        print ("Imputing missing rows with mean values of the feature")
        data=data.fillna(data.mean())

        print ("Done......!!!")

        return data

    def outlierdetect(self):
        #this function detects and eliminates outliers using the z-score method
        #any value that has a z-score of 3 or higher will be tretated as an outlier and hence dropped
    
      


