"""
This module aggregates various columns with functions

"""


class aggregateClass:

    def __init__(self,data):
        self.data=data

    def aggregateSum(self,col,col1,col2,col3,top, **kwargs):

        #aggregate function that takes in two column and aggregates them to a specified column
        #The top parameter specifies the top number of values we need returned
        
        return self.data.groupby([col]).agg({col1:sum,col2:sum,col3:sum}).head(top).reset_index(drop=True)

    def aggregateSumTwo(self,col,col1,top,**kwargs):
        # with function overloading we can now take in a single column

        return self.data.groupby([col]).agg({col1:sum}).head(top).reset_index(drop=True)

    def aggregateCategorical(self,col,col1,col2,col3,top):
        return self.data.groupby([col,col1]).agg({col2:'sum'}).sort_values(by=col3,ascending=False)

    

