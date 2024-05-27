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