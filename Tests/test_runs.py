import unittest
import pandas as pd
import sys, os

from dataClean import nulCols
from loadData import DataReading

columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']

class DataTestin(unittest.TestCase):
    

    def readData(df) -> pd.DataFrame:
        df=pd.read_csv(df)
               

    def dataCheckDuplicates(df):
        self.assertEqual(self.data.isna(), False)


    def checkPolarity(self):
        self.assertEqual(self.df['polarity'][:4], [0, 0.133333333333333, 0.3, 0.644444444444444, 5.55111512312578E-17])

    def findCreatedAt(self):
        creatAtdtypes=dtypes(data['created_at'])

        self.assertEqual(dtypes(self.data['created_at']), createdAtdtypes)

    

if __name__ == '__main__':
	unittest.main()

    