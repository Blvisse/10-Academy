"""
This module aggregates various columns with functions

"""


class aggregateClass:

    def __init__(self,data):
        self.data=data

    def aggregateSum(self,col,col1,col2,col3,top,sort, **kwargs):

        #aggregate function that takes in two column and aggregates them to a specified column
        #The top parameter specifies the top number of values we need returned
        
        return self.data.groupby([col]).agg({col1:sum,col2:sum,col3:sum}).sort_values(by=sort,ascending=False)
    def aggregateSumOne(self,col,col1,col2,top,sort, **kwargs):
    
        #aggregate function that takes in two column and aggregates them to a specified column
        #The top parameter specifies the top number of values we need returned
        
        return self.data.groupby([col]).agg({col1:sum,col2:sum}).sort_values(by=sort,ascending=False)

    def aggregateSumTwo(self,col,col1,sort,top,**kwargs):
        # we take two columns and aggregate on the other and sort 

        return self.data.groupby([col]).agg({col1:sum}).sort_values(by=sort,ascending=False).head(top)

    def aggregateCategorical(self,col,col1,col2,col3,top):
        return self.data.groupby([col,col1]).agg({col2:'sum'}).sort_values(by=col3,ascending=False)
    def aggregateCategoricalTwo(self,col,col1):
        return self.data.groupby([col])[col1].value_counts().sort_values(ascending=False)

    def calculateFrequency(self,col, top,**kwargs):
        return self.data[col].value_counts().sort_values().head(top)

    def calculateAscent(self,col,top,**kwargs):
        return self.data[col].sort_values(**kwargs ).head(top)

    


    

    

