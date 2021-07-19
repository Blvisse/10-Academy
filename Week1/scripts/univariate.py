"""
This script conducts univariate analysis on the the features of the dataset
"""
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import logging

# sns.set_style()
# logging.basicConfig(filename="..tests/newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')

# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)
def readCSV(path):
    data=pd.read_csv(path)

    return data


class Univariate:
    
    
    def __init__(self,data):
        self.data=data
        
    
    def readData(self):
    
        data=pd.read_csv(self.data)
        return data
    def calculateMetrics(self,col):
        #convert the column to a numpy array to perform the metric evaluation
        print("Reading data")
        
        
        
        print("Done")
        print('Calculating the univariate metrics of the columns {}'.format(col))
        
        print("Converting the data into numpy arrays")
        nmArray=self.data[col].values
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
    def calculateDispersion(self,col):
        # nmArray=self.data[self.col].to_numpy()
        print("Calculating dispersion stats for {}".format(col))
        nmArray=self.data[col].values
        
        Q1=np.quantile(nmArray,.25)
        Q2=np.quantile(nmArray,.50)
        Q3=np.quantile(nmArray,.75)

        print("Calculating Standard Deviation")

        std=np.std(nmArray)

        print ("Calculating Inter Quartile Range")

        IQR=Q3-Q1

        print ("Caclulating Max ")
        maxVal=np.max(nmArray)
        minVal=np.min(nmArray)

        print("Done....\n ")
        
        dispdf=[{'Q1':Q1,'Q2':Q2,'Q3':Q3,'Std deviation':std,'IQR':IQR,'Max Value':maxVal,'Min Value':minVal}]
        print("Creating DataFrame")
        df=pd.DataFrame(data=dispdf)
        df=df.T
        df.columns=['Dispersion Values']



        return df 
    def vizualiseHist(self,col,colour):
        # datar=self.data
        
        # colzz=self.col
        plt.figure(figsize=(10,8))
        sns.histplot(x=self.data[col], color=colour ,kde=True )
        plt.title("Histogram of {}".format(col), fontsize=20)
        plt.ylabel('Frequency')
        plt.xlabel(col)
        plt.show()
        
        plt.figure(figsize=(10,8))
        plt.title("Boxplot of {}".format(col))
        sns.boxplot(self.data[col])

    
        
        
    def visualiseCount(self,col,num):
        
        
        
        plt.title("A countplot of the top {} most frequent {}".format(num,col))
        sns.countplot(self.data[col],order=self.data[col].value_counts().iloc[:num].index)
        plt.xticks(rotation=90)

    def pieChart(self,col,color):
        cmap=plt.get_cmap(color)
        colors=[cmap(i) for i in np.linspace(0, 1, 8)]
        plt.pie(self.data[col].value_counts(),labels=self.data[col].unique(),shadow=True,colors=colors,autopct='%1.1f%%')
        plt.show()





# if (__name__ == '__main__'):
    
#     data=pd.read_excel(r'C:\Users\blais\Desktop\10-Academy\Week1\10-Academy\Week1\data\Week1_challenge_data_source.xlsx')
#     dataFrame=Univariate(data,'Other UL (Bytes)')
#     # dataFrame=ReadData('data.csv')
#     dataFrame=dataFrame.calculateMetrics()
#     print (dataFrame)