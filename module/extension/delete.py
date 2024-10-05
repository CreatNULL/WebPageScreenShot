import json
import logging
import os.path


def remove_matching_extension(secure_preferences_file: str, target_plugn_path: str):
    logging.info("Starting to remove extension matching in 'Secure Preferences' file")
    try:
        # 读取 JSON 文件
        with open(secure_preferences_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        logging.error(f"The specified file about the plugins info file 'Secure Preferences' not found")
        return None

    # 转为绝对路径
    target_plugn_path = os.path.abspath(target_plugn_path)
    keys_to_delete = []

    try:
        # 检查是否存在 extensions 和 settings
        if 'extensions' in data and 'settings' in data['extensions']:
            extensions = data['extensions']['settings']


            # 遍历查找匹配的子项
            for key, value in extensions.items():
                if isinstance(value, dict) and 'path' in value:
                    if value['path'] == target_plugn_path:
                        keys_to_delete.append(key)
    except KeyError:
        logging.info("没有匹配到键值对, 请联系作者")
        return

    if not keys_to_delete:
        logging.info("Nothing to delete, Because not found.")
        return '', ''

    # 删除匹配的子项
    for key in keys_to_delete:
        deleted_value = extensions.pop(key)
        try:
            with open(secure_preferences_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            # 返回被删除的键和对应的路径值
            return key, deleted_value['path']
        except Exception as e:
            logging.error(f"重新写入插件信息失败: {str(e)}")
