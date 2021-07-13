"""
This script conducts univariate analysis on the the features of the dataset
"""
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style()

def readCSV(path):
    data=pd.read_csv(path)

    return data


class Univariate:
    
    
    def __init__(self,data,col):
        self.data=data
        self.col=col
    
    def readData(self):
    
        data=pd.read_csv(self.data)
        return data
    def calculateMetrics(self):
        #convert the column to a numpy array to perform the metric evaluation
        print("Reading data")
        
        
        
        print("Done")
        print('Calculating the univariate metrics of the columns {}'.format(self.col))
        
        print("Converting the data into numpy arrays")
        nmArray=self.data[self.col].values
        print("Done!")
        print("Calculating mean....")        
        mean=np.mean(nmArray)
        print ("Calculating Mode...")
        mode=stats.mode(nmArray)[0]
        print("Calculating Median...")
        median=np.median(nmArray)
        print ("Calculating skeweness...")
        skew=stats.skew(nmArray)
        print ("Calculating kurtosis...")
        kurtosis=stats.kurtosis(nmArray)
        print ("Calculating standard deviation....")
        std=np.std(nmArray)
        print ("Calculating variance ...")

        var=np.var(nmArray)

        print("Done !")
        
        columns=['Mean','Mode','Median','Skew','Kurtosis','Standard deviation','Variance']

        statsdf=[{'Mean':mean,'Mode':mode,'Median':median,'Skew':skew,'Kurtosis':kurtosis,'Standard deviation':std,'Variance':var}]
        df=pd.DataFrame(data=statsdf,columns=columns)
        df=df.T
        df.columns=['Analysis Values']

        return df
    def calculateQuatile(self):
        # nmArray=self.data[self.col].to_numpy()

        pass
    def vizualiseHist(self,colour):
        # datar=self.data
        
        # colzz=self.col
        sns.histplot(x=self.data[self.col],bins=40 , color=colour ,kde=True )
        plt.title("Histogram of {}".format(self.col), fontsize=20)
        plt.ylabel('Frequency')
        plt.xlabel(self.col)
        plt.show()
        # plt.figure(figsize=(10,8))
        plt.title("Boxplot of {}".format(self.col))
        sns.boxplot(self.data[self.col])

    
        
        
    def visualiseCount(self,num):
        
        
        
        sns.countplot(self.data[self.col],order=self.data[self.col].value_counts.iloc[:num].index)







# if (__name__ == '__main__'):
    
#     data=pd.read_excel(r'C:\Users\blais\Desktop\10-Academy\Week1\10-Academy\Week1\data\Week1_challenge_data_source.xlsx')
#     dataFrame=Univariate(data,'Other UL (Bytes)')
#     # dataFrame=ReadData('data.csv')
#     dataFrame=dataFrame.calculateMetrics()
#     print (dataFrame)