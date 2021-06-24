class  dataCleaning:
    
    """
    This module is focused on data cleaning steps
    
    Functions in the module transform the raw data to 
    
    """
    #create a constructor with the data
    def __init__(self,data):

      self.data=data 

    #drop null columns

    def dropNullCols(df)->pd.DataFrame:
        
        df=df.dropna(inplace=True)
        
        return df
    
    def nulCols(df)->pd.DataFrame:
        

        return df.isnull().sum()
        
    #incse we need to drop specific columns
    def dropSpecificCols(self,cols):
        df.dropna(labels=[cols],inpalce=True,axis=1)
        
        return df
    
    #strip tweets from the dictionary 
    def stripTweets(self):
        df[cols]=df[cols].apply(lambda x: x.strip(":")[1])
        
    #convert the created_at column to date time
    def fixDateTime(df,cols):
        df[cols]=pd.to_datetime(df[cols])