"""
通过以下邀请链接注册，将享受高额的手续费返佣
1. 芝麻开门交易所（gateio）
注册芝麻开门交易所，您将获得60%以上的手续费返佣
点击此链接注册芝麻开门交易所：https://www.gateex.cc/signup/UgBHUV8M/30?ref_type?=103
备用网址（科学上网）：https://www.gate.io/signup/UgBHUV8M/30?ref_type?=103

2. 币安交易所（binance）
注册币安交易所，您将获得40%以上的手续费返佣
点击此链接币安交易所：https://accounts.suitechsui.io/register?ref=L9VRCUHB
备用网址（科学上网）：https://www.binance.com/register?ref=L9VRCUHB

3. 欧易交易所（okx）
注册欧易交易所，您将获得40%以上的手续费返佣
点击此链接欧易交易所,领取50USDT数字货币盲盒：https://www.cnouyi.info/join/4390294
备用网址（科学上网）：https://www.okx.com/join/4390294

4. bitget交易所（bitget）
注册bitget交易所，您将获得60%以上的手续费返佣
点击此链接bitget交易所：https://partner.bitget.fit/bg/Y32LHU
备用网址（科学上网）：https://partner.bitget.com/bg/Y32LHU

qq:2926888267
qq群: 649390535
微信：daniugege6
电报：https://t.me/benbenniu666
电报群：https://t.me/daniuzhandui
推特：https://twitter.com/daniugelaile
"""

import time
import datetime
def get_cur_timestamp():
    """Get current timestamp(second)."""
    ts = int(time.time())
    return ts

def ts_to_datetime_str(ts=None, fmt="%Y-%m-%d %H:%M:%S"):
    """Convert timestamp to date time string.

    Args:
        ts: Timestamp, millisecond.
        fmt: Date time format, default is `%Y-%m-%d %H:%M:%S`.

    Returns:
        Date time string.
    """
    if not ts:
        ts = get_cur_timestamp()
    dt = datetime.datetime.fromtimestamp(int(ts))
    return dt.strftime(fmt)

def datetime_str_to_ts(dt_str, fmt="%Y-%m-%d %H:%M:%S"):
    """Convert date time string to timestamp.

    Args:
        dt_str: Date time string.
        fmt: Date time format, default is `%Y-%m-%d %H:%M:%S`.

    Returns:
        ts: Timestamp, millisecond.
    """
    ts = int(time.mktime(datetime.datetime.strptime(dt_str, fmt).timetuple()))
    return ts


def format_time_difference(timestamp1, timestamp2):
    """
    计算两个时间戳之间的差值，并将其转换为天、时、分和秒的格式
    :param timestamp1: 第一个时间戳
    :param timestamp2: 第二个时间戳
    :return: 包含差值的天、时、分和秒的字符串
    """
    difference_seconds = (timestamp1 - timestamp2)

    # 计算天、时、分和秒
    days = difference_seconds // (24 * 3600)
    hours = (difference_seconds % (24 * 3600)) // 3600
    minutes = (difference_seconds % 3600) // 60
    seconds = difference_seconds % 60

    return f"{days}天{hours}小时{minutes}分钟{seconds}秒"