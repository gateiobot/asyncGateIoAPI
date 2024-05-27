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