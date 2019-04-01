import tushare as ts
import time
# 设置token
ts.set_token('b925e01c251167328cc748123b8632a8ae9c70b49089002ea679d385')

# 初始化pro接口
pro = ts.pro_api()
sse_stock = pro.stock_basic(exchange='SSE', list_status='L', fields='ts_code')
szse_stock = pro.stock_basic(exchange='SZSE', list_status='L', fields='ts_code')

id = sse_stock.append(szse_stock)

"""
单针探底
. 昨天必须是阴线
. 今天最低价必须小于昨天最低价
. 今天的下影线大于实体长度两倍
. 今天的上影线小于实体长度
"""
def singleNeedleBottom(id, stock_info):
    if stock_info.shape[0] < 2:
        return False
    yesterday_info = stock_info.iloc[1]
    today_info = stock_info.iloc[0]

    if yesterday_info.change >= 0:
        return False
    if today_info.low > yesterday_info.low:
        return False

    if today_info.close >= today_info.open:
        return False

    if today_info.open >= today_info.close:
        upper_shadow_line = today_info.high - today_info.close
        lower_shadow_line = today_info.open - today_info.low
    else:
        upper_shadow_line = today_info.high - today_info.open
        lower_shadow_line = today_info.close - today_info.low
    entity = abs(today_info.open - today_info.close)

    if lower_shadow_line > entity*2 and entity >= upper_shadow_line:
        print('----------------- 单针探底, 股票代码: {0}'.format(id))
        return True
    else:
        return False

def searchStock():
    fail_num = 0
    success_num = 0
    today = time.strftime("%Y%m%d", time.localtime())
    for stock_id in id['ts_code']:
        print('当前读取股票代码 {0}, 已经检索 {1:4d}, 剩下 {2:4d}'.format(stock_id, success_num , len(id['ts_code'])-success_num))
        info = pro.daily(ts_code=stock_id, start_date='20190321', end_date=today)

        if info is None:
            fail_num += 1
            continue
        else:
            success_num += 1
            singleNeedleBottom(stock_id, info)

    print(fail_num)


if __name__ == '__main__':
    searchStock()

