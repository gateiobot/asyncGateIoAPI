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

import yaml
from typing import Any, Dict, Type

class Config:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """加载YAML配置文件"""
        try:
            with open(self.config_path, "r",encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"配置文件 {self.config_path} 未找到")
        except yaml.YAMLError as exc:
            raise yaml.YAMLError(f"解析配置文件时出错: {exc}")

    def get(self, path: str, default: Any = None, type: Type = None) -> Any:
        """获取配置项的值，支持路径式访问，如 'database.host'，并可进行类型转换"""
        keys = path.split('.')
        value = self._config
        try:
            for key in keys:
                value = value[key]
            if type is not None:
                value = type(value)
            return value
        except (KeyError, TypeError, ValueError):
            if default is not None:
                return default
            raise KeyError(f"配置项 {path} 不存在或类型不匹配")

    def reload(self):
        """重新加载配置文件"""
        self._config = self._load_config()

    def __getitem__(self, item):
        """允许使用字典方式访问"""
        return self._config[item]

# 使用示例
config = Config()