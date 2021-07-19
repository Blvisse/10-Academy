import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host='localhost', user='root', password='root',
                         database=dbName, buffered=True, auth_plugin='mysql_native_password')
    cur = conn.cursor()
    return conn, cur

def emojiDB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()

def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    sqlFile = 'analysis.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return

def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    """

    Parameters
    ----------
    df :
        pd.DataFrame:
    df :
        pd.DataFrame:
    df:pd.DataFrame :


    Returns
    -------

    """
    # cols_2_drop = ['timestamp']
    # try:
    #     df = df.drop(columns=cols_2_drop, axis=1)
    #     df = df.fillna(0)
    # except KeyError as e:
    #     print("Error:", e)
    
    df['MSISDNNumber']=df['MSISDNNumber'].apply(lambda x:str(x))
    df['Experience_Score']=df['Experience_Score'].apply(lambda x: str(x))
    df['Engagement_Score']=df['Engagement_Score'].apply(lambda x: str(x))
    df['Satisfaction_score']=df['Satisfaction_score'].apply(lambda x: str(x))

    return df


def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    df = preprocess_df(df)

    # df['MSISDN/Number']=df['MSISDN/Number'].apply(lambda x:int(x/1000))
    # df['Experience Score']=df['Experience Score'].apply(lambda x: int(x/1000))
    # df['Engagement Score']=df['Engagement Score'].apply(lambda x: int(x/1000))
    # df['Satisfaction score']=df['Satisfaction score'].apply(lambda x: int (x/1000))

    for _, row in df.iterrows():
<<<<<<< HEAD
        sqlQuery = f"""INSERT INTO {table_name} ( MSISDNNumber,Experience_Score,Engagement_Score,Satisfaction_score )
             VALUES(%s, %s, %s,%s);"""
        data = (row[0], row[1], row[2], row[3])
        print(data) 
        print(sqlQuery)
=======
        sqlQuery = f"""INSERT INTO {table_name} ('MSISDN/Number','Experience Score','Engagement Score','Satisfaction score')
             VALUES(int(%s), int(%s), int(%s),int(%s));"""
        data = (row[0], row[1], row[2], row[3])
>>>>>>> parent of b420627... tweaked the database

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    """

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :


    Returns
    -------

    """
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createDB(dbName='tweets')
    
    createTables(dbName='tweets')

    df = pd.read_csv(r'C:\Users\blais\Desktop\10-Academy\Week1\10-Academy\Week1\data\finalData2.csv')

    insert_to_table(dbName='tweets', df=df, table_name='Tweetinformation')
