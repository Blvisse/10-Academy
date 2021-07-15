"""
This is a script to read and load data into the system

"""
import pandas as pd
import sys 
class ReadData:
    

    def __init__(self,path):
        self.path=path

    def readData(self):

        print('Reading the data....')
        try :
            data=pd.read_excel(self.path)
            print("successfully read the dataset...")
            return data
        except FileNotFoundError:
            
            print("Woops! The file was not found")

            return
    def readCsv(self):
        print("Reading Data...\n")
        try: 
            data=pd.read_csv(self.path)

            print ("Successfully read the dataset ...")
            return data 
        except FileNotFoundError:
            
            print("Woops! The file was not found")

            return
        
        except Exception as e:

            print ("Woops {} error occurred".format(e.__class__))

            return 

            
    def showTop(self):
        print ("Displaying the first 5 rows of the dataset")

        try:
            
            return self.readData().head()
        except :
            print ("An error occured while we tried to load your data")

            return

    def display(self):
        # 
        data=self.showTop()
        

        return data

if (__name__ == '__main__'):

    dataFrame=ReadData('../data/Week1_challenge_data_source.xlsx')
    # dataFrame=ReadData('data.csv')
    dataFrame=dataFrame.display()
    print (dataFrame)

    