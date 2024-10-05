# coding: utf-8
"""
读取配置文件，将 配置文件 与命令行参数合并，赋值给命令行参数 args 对象
"""
import json
import argparse
import configparser
import logging
from typing import Union


def __turn_to_python_types(config, config_title: str = 'DEFAULT', config_key: str = None, key_type: str = str) -> Union[list, str, tuple, dict, None]:
    """ 将配置文件中的列表转为 Python 的列表，支持 1,2,3 格式 和 ["", "", ''] ("", "", "")格式,
    转换后，内部的值统一为字符串格式，如果是需要其他的，还得转换，且不支持复杂的嵌套。

    :param config: 实例化后已经读取的配置
    :param config_title: 配置文件中这样的标题
    :param config_key: 对应的子项的标题
    :param key_type: 需要转换的类型，考虑到字符串类型中存在任何可能，所以需要该参数指定

    :return: 返回转换后的列表
    :raises ValueError: 如果 config_key 无效或 config_key 对应的值格式不正确
    """
    if not config:
        raise ValueError("参数 'config' 未传递配置文件对象")

    # 参数验证
    if config_key is None:
        raise ValueError("config_key 不能为空")

    if config_title not in config:
        raise ValueError(f"配置标题 '{config_title}' 不存在")

    if config_key not in config[config_title]:
        raise ValueError(f"配置项 '{config_key}' 不存在于标题 '{config_title}' 中")

    # 读取配置值并转换为列表
    config_value = config[config_title][config_key]

    if isinstance(config_value, str):
        if config_value:
            if config_value.strip().lower().capitalize() == 'None':
                logging.debug("-- None --")
                return None
        if key_type == list:
            logging.debug("-- list with [] --")
            # 处理类似 ["value1", "value2"] 的格式
            # 拆除 []
            if config_value.startswith("[") and config_value.endswith("]"):
                remove_square_brackets = config_value[1:-1]
            else:
                remove_square_brackets = config_value
            # 转为列表
            square_brackets_to_list = remove_square_brackets.split(',')
            # 去除多余的空
            remove_blank_list = [_.strip() for _ in square_brackets_to_list if _.strip()]
            # 存储处理后的列表
            new_value = []
            for _ in remove_blank_list:
                # 开始和结束都是 ' 意味着用 ' 包裹
                if _.startswith("'") and _.endswith("'"):
                    new_value.append(_.strip("'"))
                elif _.startswith('"') and _.endswith('"'):
                    new_value.append(_.strip('"'))
                elif not _:
                    continue
                else:
                    if  _.startswith("{") or _.startswith("(") or _.startswith("["):
                        raise ValueError("不支持嵌套的列表转换")
                    else:
                        # 纯数字形式？ [1, 2, 3] 或已经是合法的
                        new_value.append(_)

            config_value = new_value
            # 处理值为 None
            # ----- 判断是否为 None 字符串替换，否则保持原来的 <------------------------------- 1. 遍历 ------------
            config_value = [None if _.strip().lower().capitalize() == 'None' else _ for _ in config_value]
        elif key_type == tuple:
            logging.debug("-- tuple with () --")
            # 拆除 ()
            if config_value.startswith("(") and config_value.endswith(")"):
                remove_round_brackets = config_value[1:-1]
            else:
                remove_round_brackets = config_value
            # 转为列表
            square_brackets_to_list = remove_round_brackets.split(',')
            # 去除多余的空
            remove_blank_list = [_.strip() for _ in square_brackets_to_list if _.strip()]
            # 存储处理后的列表
            new_value = []
            for _ in remove_blank_list:
                # 开始和结束都是 ' 意味着用 ' 包裹
                if _.startswith("'") and _.endswith("'"):
                    new_value.append(_.strip("'"))
                elif _.startswith('"') and _.endswith('"'):
                    new_value.append(_.strip('"'))
                elif not _:
                    continue
                else:
                    if _.startswith("{") or _.startswith("(") or _.startswith("["):
                        raise ValueError("不支持嵌套的列表转换")
                    else:
                        # 纯数字形式？ [1, 2, 3]
                        new_value.append(_)
            # 处理值为 None, 以及转为 tuple
            config_value = tuple([None if _.strip().lower().capitalize() == 'None' else _ for _ in new_value])
        elif key_type == bool and config_value.strip() in ['True', 'False', 'true', 'false']:
            logging.debug(" --bool --")
            if config_value:  # 有值的情况下
                config_value = config_value.strip().capitalize() == 'True'
            else:  # 无值
                config_value = False
        elif key_type == dict and '{' in config_value and '}' in config_value:
            logging.debug("-- dict --")
            config_value = json.loads(config_value)
        elif key_type == int:
            logging.debug("-- int --")
            config_value = int(config_value)
        elif key_type == float:
            logging.debug("-- float --")
            config_value = float(config_value)
        elif key_type == str:
            logging.debug("-- str --")
            config_value = str(config_value)
        else:
            logging.debug("-- 哦啥也不做 --")
            pass
    else:
        logging.debug("从配置文件接收的不是字符串类型")
        ...
    # 如果没有值
    if key_type == list and len(config_value) == 1 and not config_value[0]:
        return []
    elif key_type == tuple and len(config_value) == 1  and not config_value[0]:
        return tuple()
    else:
        pass
    return config_value


def load_config(args, config):
    """ 读取配置文件并更新命令行参数

    :param args: argparse 实例化后的对象，包含命令行参数
    :param config: configparser.ConfigParser 的实例，已准备好读取配置文件
    :raises ValueError: 如果配置文件或参数不符合预期
    :return: 更新后的 args 对象
    """
    # 参数验证
    if not isinstance(args, argparse.Namespace):
        raise ValueError("args 必须是 argparse.Namespace 的实例")

    if not isinstance(config, configparser.ConfigParser):
        raise ValueError("config 必须是 configparser.ConfigParser 的实例")

    # 读取配置文件
    config.read(args.config)

    # 以命令为优先级最高，判断是否设置了配置文件，如果设置，则以配置文件为准

    for key in vars(args):
        # 获取命令行参数
        cmd_line = getattr(args, key)

        # 读取配置文件的值
        if key == 'config':
            # 跳过 config 参数
            continue
        elif key in ['url', 'proxy-bypass', 'ssl-cert', 'extensions', 'set-arguments', 'remove-arguments', 'headers-bypass', 'headers'] or type(cmd_line) is list:
            # 读取配置项并转换为列表
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=list)
        elif key in ['timeout'] and type(cmd_line) is tuple:
            config_value = tuple([float(_) for _ in __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=tuple)])
        elif type(cmd_line) is dict:
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=dict)
        elif type(cmd_line) is int:
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=int)
        elif type(cmd_line) is float:
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=float)
        elif type(cmd_line) is bool:
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key, key_type=bool)
        else:
            config_value = __turn_to_python_types(config=config, config_title='DEFAULT', config_key=key)

        # 如果命令行参数未设置

        # 终端和配置文件不相同，以配置文件为准
        if args.config:
            if cmd_line != config_value:
                logging.debug(f"两个值不相等: {cmd_line}, {config_value}")
                value = config_value
                setattr(args, key, value)
            else:
                logging.debug(f"两个值相等: {cmd_line}, {config_value}")

        # 终端和配置文件不相同，以终端为准
        else:
            if cmd_line != config_value:
                logging.debug(f"两个值不相等: {cmd_line}, {config_value}")
                value = cmd_line
                setattr(args, key, value)
            else:
                logging.debug(f"两个值相等: {cmd_line}, {config_value}")
    return args

