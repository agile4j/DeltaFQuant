#!/usr/bin/env python
# encoding: utf-8
"""
@author: liurenpeng
@time: 2021/8/29
@desc: 用于调用股票行情数据的脚本
"""

import data.stock as st
import pandas as pd

# 初始化变量
code = '000001.XSHE'
type = 'price'

# 调用一只股票的行情数据
data = st.get_single_price(code=code,
                           time_frequency='daily',
                           start_date='2021-01-01',
                           end_date='2021-02-01')
# 存储csv
st.export_data(data=data, filename=code, type=type)

data = st.get_csv_data(code, type)
print(data)


# 实时更新数据：假设每天更新日K数据 > 存到csv文件里面 > data.to_csv(append)
