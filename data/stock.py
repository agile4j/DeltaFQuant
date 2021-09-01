#!/usr/bin/env python
# encoding: utf-8
"""
@author: liurenpeng
@time: 2021/8/29
"""

from jqdatasdk import *
import pandas as pd
import datetime
import time

# 账号是申请时所填写的手机号；密码为聚宽官网登录密码，新申请用户默认为手机号后6位
auth('13263258175', '@JQData123')

# 设置行列不忽略
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 1000)

# 全局变量
file_root = '/Users/liurenpeng/PycharmProjects/DeltaFQuant/data/'


def get_stock_list():
    """
    获取所有A股股票列表
    上海证券交易所.XSHG
    深圳证券交易所.XSHE
    :return: stock_list
    """
    stock_list = list(get_all_securities(['stock']).index)
    return stock_list


def get_single_price(code, time_frequency, start_date, end_date):
    """
    获取单个股票行情数据
    :param code:
    :param time_frequency:
    :param start_date:
    :param end_date:
    :return:
    """
    data = get_price(code, start_date=start_date, end_date=end_date, frequency=time_frequency)
    return data


def export_data(data, filename, type):
    """
    导出股票相关数据
    :param data:
    :param filename:
    :param type: 股票数据类型，可以是：price、finance
    :return:
    """
    file_path = file_root + type + '/' + filename + '.csv'
    data.index.names = ['time']
    data.to_csv(file_path)
    print('已成功存储至：', file_path)


def get_csv_data(filename, type):
    file_path = file_root + type + '/' + filename + '.csv'
    return pd.read_csv(file_path)


def transfer_price_frequency(data, time_frequency):
    """
    转换股票行情周期
    :param data:
    :param time_frequency:
    :return:
    """
    result = data.DataFrame()
    result['open'] = data['open'].resample(time_frequency).first()
    result['close'] = data['close'].resample(time_frequency).last()
    result['high'] = data['high'].resample(time_frequency).max()
    result['low'] = data['low'].resample(time_frequency).min()
    return result


def get_single_finance(code, date, stat_date):
    """
    获取单个股票财务指标
    :param code:
    :param date:
    :param stat_date:
    :return:
    """
    data = get_fundamentals(query(indicator).filter(indicator.code == code), date=date, statDate=stat_date)
    return data


def get_single_valuation(code, date, stat_date):
    """
    获取单个股票估值指标
    :param code:
    :param date:
    :param stat_date:
    :return:
    """
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date, statDate=stat_date)
    return data



