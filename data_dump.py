import pandas as pd
from sqlalchemy import create_engine
from django.conf import settings
import pymysql
import os


def weather_data_dump(path):
    # path = r"C:\Naveen\KinnuBannu\Project\weather\weather_analysis\wx_data\USC00110072.txt"
    # file_path = os.path.join('..',"wx_data",file_name)
    file_data = []
    columns=['date','min_temp','max_temp','precipitation']
    # files=os.listdir(path)
    # for file in files:
        # absl_path = os.path.join(path, file)
    data = open(path).readlines()
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    return file_data


def yield_data_dump():
    path = r"C:\Naveen\KinnuBannu\Project\weather\weather_analysis\yield_data\US_corn_grain_yield.txt"
    columns=['date','corn_gain']
    data = open(path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    user = "root"
    password = "Innotas-1991"
    database_name = "weather"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weatheryield", con=engine)


def weather_stats(path):
    # path = r"C:\Naveen\KinnuBannu\Project\weather\weather_analysis\wx_data\USC00110072.txt"
    columns=['date','min_temp','max_temp','precipitation']
    # file_path = os.path.join('..',"wx_data",file_name)
    data = open(path).readlines()
    file_data = []
    for row in data:
        file_data.append(dict(zip(columns,[i.strip('\n') for i in row.split('\t')])))
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    return dataframe[(dataframe['precipitation']!='-9999') & 
                     (dataframe['max_temp']!='-9999') & 
                     (dataframe['min_temp']!="-9999")]


def calculate_stats(path):
    result = []
    import
    # for wf in os.listdir(os.path.join('..','wx_data')):
    columns=['date','min_temp','max_temp','precipitation']
    df = weather_stats(path)
    breakpoint()
    df['date'] = map(lambda x:datetime.datetime.fromtimestamp(float(x)),df['date'])
    df['year'] = map(lambda x:df['date'].ix[x].year,df.index)
    df['max_temp']=map(float,df['min_temp'].values)
    df['min_temp']=map(float,df['max_temp'].values)
    df['precipitation']=map(float,df['precipitation'].values)
    mean = df.groupby('year').mean()
    total = df.groupby('year').sum()
    maximutemp_mean  = mean['max_temp']
    minimutemp_mean = mean['min_temp']
    total_precipitation = total['precipitation']

    result.append("{0}\t{1}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(wf,
                                                                total_precipitation.index[0],
                                                                maximutemp_mean.values[0],
                                                                minimutemp_mean.values[0],
                                                                total_precipitation.values[0]))
    dataframe = pd.DataFrame(result)
    dataframe.index.names = ['id']
    user = "root"
    password = "Innotas-1991"
    database_name = "weather_status"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weather_status", con=engine)


def read_data(path):
    # breakpoint()
    file_data=weather_data_dump(path)
    dataframe = pd.DataFrame(file_data)
    dataframe.index.names = ['id']
    user = "root"
    password = "Innotas-1991"
    database_name = "weather"
    host = "localhost"
    tp = 'mysql+pymysql://{}:{}@{}/{}'.format(user, password, host, database_name)
    engine = create_engine(tp, echo=False)
    dataframe.to_sql("weather", con=engine)


if __name__ == "__main__":
    #change this path your path
    path = r"C:\Naveen\KinnuBannu\Project\weather\weather_analysis\wx_data\USC00110072.txt"
    read_data(path)
    yield_data_dump()

    # calculate_stats(path)


