#!/usr/bin/env python
# encoding: utf-8
"""
@author: liurenpeng
@time: 2021/8/4
"""

'''获取财务指标数据'''

# https://www.joinquant.com/help/api/help#name:JQData
from jqdatasdk import *
import pandas as pd
import time

# 设置行列不忽略
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 100)

# 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
auth('13263258175', '@JQData123')

# XSHG-上海证券交易所；XSHE-深圳证券交易所

df = get_fundamentals(query(indicator), statDate="2020")
# print(df)
# df.to_csv('/Users/liurenpeng/PycharmProjects/DeltaFQuant/data/finance/finance2020.csv')

# 基于盈利指标选股：eps,operating_profit,roe,inc_net_profit_year_on_year
df = df[(df['eps'] > 0)
        & (df['operating_profit'] > 123456)
        & (df['roe'] > 100)
        & (df['inc_net_profit_year_on_year'] > 100)]
print(df)



