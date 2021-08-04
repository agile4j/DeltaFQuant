#!/usr/bin/env python
# encoding: utf-8
"""
@author: liurenpeng
@time: 2021/8/3
"""

# https://www.joinquant.com/help/api/help#name:JQData
from jqdatasdk import *
import time

# 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
auth('13263258175', '@JQData123')

# XSHG-上海证券交易所；XSHE-深圳证券交易所

# 将所有股票列表转换成数组
stocks = list(get_all_securities(['stock']).index)

for stock_code in stocks:
    print("正在获取股票行情数据，股票代码：", stock_code)
    df = get_price(security=stock_code, end_date='2021-08-02',count=10, frequency='1d', panel=False)
    print(df)
    time.sleep(3)

# resample函数的使用

# 转换周期：日K转换为周K
# 获取日K
# 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）

# 汇总统计：统计月成交量、成交额（sum）

