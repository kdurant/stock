#-*- coding:utf-8 -*-
import tushare as ts
import time


def priceLessThanMA20(id, per=0.03, time=time.strftime("%Y-%m-%d", time.localtime())):
    """
    判断股票当天价格是否在均线之下，且价格小于3%
    :param id:
    :param time:
    :return:
    """

    info = ts.get_hist_data(id, start=time,end=time)
    ma20 = info.ma20[0]
    close = info.close[0]
    # print(ma20)
    # print(close)
    # print((ma20 - close)/close)
    if ma20 >= close:
        if (ma20 - close)/close < per:
            print(id)

if __name__ == '__main__':
    # print(priceLessThanMA20('002456'))
    print(priceLessThanMA20('002508'))