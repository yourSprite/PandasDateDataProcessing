import pandas as pd

# 从csv文件中读取数据
path = 'date.csv'
df = pd.read_csv(path, header=None, encoding='utf-8')
# print(df.head(2))

# 整理数据
df.columns = ['date', 'number']
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
# print(df.head(2))
# print(df.tail(2))

# print(type(df))
# print(df.index)
# print(df.shape)

# 构造Series类型数据
s = pd.Series(df['number'], index=df.index)
# print(type(s))
# print(s.head(2))

print('----------获取2013年数据----------')
print(df['2013'].head(2))
print(df['2013'].tail(2))

# 切片（slice）方式时间
print('----------获取2016至2017年数据----------')
print(df['2016':'2017'].head(2))
print(df['2016':'2017'].tail(2))

# dataframe的truncate函数实现
print('----------获取某个时期之前或之后的数据----------')
print('----------after----------')
print(df.truncate(after='2013-11'))
print('----------before----------')
print(df.truncate(before='2017-02'))

print('----------获取某月数据----------')
print(df['2013-11'])

print('----------获取具体某天的数据----------')
print(df['2013-11-06':'2013-11-06']) # 这里注意dataframe和series的使用差异
# print(s['2013-11-06'])

#to_period()方法
# 注意：df.index的数据类型是DatetimeIndex,df_period.index的数据类型是PeriodIndex

# 按月显示，不统计
df_period = df.to_period('M')
# print(type(df_period))
# print(type(df_period.index))
print(df_period.head())

# 按季度显示，不统计
print(df.to_period('Q').head())

# 按年度显示，不统计
print(df.to_period('A').head())

# asfreq()方法
# 按年度频率显示
print(df_period.index.asfreq('A'))
print(df_period.index.asfreq('A-JAN'))

# 按季度频率显示
print(df_period.index.asfreq('Q'))
print(df_period.index.asfreq('Q-SEP'))

# 按月度频率显示
print(df_period.index.asfreq('M'))

# 按工作日显示
# method1
print(df_period.index.asfreq('B', how='start'))
# method2
print(df_period.index.asfreq('B', how='end'))

# 按日期统计数据
# 按周统计数据
print(df.resample('w').sum().head())
# 按月月统计数据
print(df.resample('M').sum().head())
# 按季度统计数据
print(df.resample('Q').sum().head())
# 按年统计数据
print(df.resample('AS').sum())

# 按年统计并显示
print(df.resample('AS').sum().to_period('A'))
# 按季度统计并显示
print(df.resample('Q').sum().to_period('Q').head())
# 按月度统计并显示
print(df.resample('M').sum().to_period('M').head())