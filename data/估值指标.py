#!/usr/bin/env python
# encoding: utf-8
"""
@author: liurenpeng
@time: 2021/8/5
"""

'''获取股票估值数据'''

# https://www.joinquant.com/help/api/help#name:JQData
from jqdatasdk import *
import pandas as pd
import datetime
import time

# 设置行列不忽略
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 100)

# 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
auth('13263258175', '@JQData123')

# XSHG-上海证券交易所；XSHE-深圳证券交易所

df = get_fundamentals(query(valuation), statDate = datetime.datetime.today())
print(df)