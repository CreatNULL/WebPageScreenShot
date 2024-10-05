# coding=utf-8
"""
创建浏览器插件模块
"""
import os
import zipfile
import string
import logging


def unzip_file(src: str, dest: str, ):
    """ 解压缩文件"""
    if not os.path.exists(str(src)):
        logging.error(f"解压的 zip 文件 {src} 不存在")
        raise FileNotFoundError("Zip file {src} not found!")

    try:
        # 打开ZIP文件
        with zipfile.ZipFile(src, 'r') as zip_ref:
            # 解压缩文件到指定目录
            zip_ref.extractall(dest)
            # 将权限应用到解压缩后的文件
            for info in zip_ref.infolist():
                extracted_file_path = zip_ref.extract(info, dest)
                permissions = info.external_attr >> 16
                os.chmod(extracted_file_path, permissions)
    except Exception as e:
        logging.error("解压缩文件失败!" + str(e))
        raise


# 添加代理插件
def create_proxy_extension(proxy_host: str = '127.0.0.1', proxy_port: str = '8080',
                           proxy_username: str = '', proxy_password: str = '',
                           scheme: str = 'http', bypass: list = [], plugin_path: str = None) -> str:
    """代理插件, 实现不代理某些URL

    Args:
        proxy_host: 代理的IP/域名
        proxy_port: 代理主机的端口
        proxy_username: 代理验证的用户名, 默认 ''
        proxy_password: 代理验证的密码，默认 ""
        scheme: 代理的协议
        bypass: 不代理的URL
        plugin_file: 插件生成后输出的路径

    Returns:
        str: 代理插件的输出路径
    """

    # 创建代理插件默认路径
    plugin_file = f'{scheme}_proxy_plug.zip'

    if plugin_path is not None and not plugin_path.endswith(".zip"):  # 给的是目录
        plugin_file = os.path.join(plugin_path, plugin_file)
    else:
        plugin_file = plugin_path

    if type(proxy_host) != str:
        raise TypeError("指定的 proxy_host 参数类型错误")
    if type(proxy_port) != str:
        raise TypeError("指定的 proxy_port 参数类型错误")
    if type(proxy_username) != str:
        raise TypeError("指定的 proxy_username 参数类型错误")
    if type(proxy_password) != str:
        raise TypeError("指定的 proxy_password 参数类型错误")
    if type(bypass) != list:
        raise TypeError("指定的 bypass 参数类型错误")
    if type(plugin_file) != str:
        raise TypeError("指定的 plugin_file 参数类型错误")

    if bypass:
        for _ in bypass:
            if type(_) != str:
                raise TypeError("bypass 中的内容应当是字符串类型")
    else:
        bypass = []

    manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "incognito": "split",
    "name": "Abuyun Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
        """

    background_js = string.Template(
        """
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ${bypass}
            }
        };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );

        chrome.windows.onRemoved.addListener(function(windowId) {
            chrome.proxy.settings.clear({scope: "regular"}, function() {});
        });
        """
    ).substitute(
        host=proxy_host.strip(),
        port=proxy_port.strip(),
        username=proxy_username.strip(),
        password=proxy_password.strip(),
        scheme=scheme.strip(),
        bypass=bypass
    )

    try:
        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
    except Exception as e:
        raise Exception("浏览器代理插件创建失败")
    return plugin_file


# 添加自定义头部 v3
def create_add_headers_extension(headers: dict, bypass: list = [], plugin_path: str = None) -> str:
    """ 添加自定义头部

    Args:
        headers: 添加头部 格式 {"user-agent": "xxxx", "host": "192.168.0.1"}
        bypass: 不添加头部的域名
        plugin_file (str): 插件的输出路径。
    """
    if type(plugin_path) != str and type(plugin_path) is not None:
        raise TypeError("指定的 plugin_path 参数类型错误")

    plugin_file = 'headers_plug.zip'

    if plugin_path is not None and not plugin_path.endswith(".zip"):  # 给的是目录
        plugin_file = os.path.join(plugin_path, plugin_file)
    else:
        plugin_file = plugin_path

    if type(headers) != dict:
        raise TypeError("指定的 headers 参数类型错误")

    if type(bypass) != list:
        raise TypeError("指定的 bypass 参数类型错误")

    for _ in bypass:
        if '*' in _:
            raise ValueError("过滤的域名不需要添加 *")

    headers_list = []

    for header_key, headers_value in headers.items():
        _ = dict()
        if not header_key:
            continue
        _["header"]  = str(header_key)
        _["value"] = str(headers_value)
        headers_list.append(_)

    manifest_json = """
{
 
    "background": {
       "service_worker": "background.js"
    },
    "description": "Add or modify http headers ",
    "host_permissions": [ "\u003Call_urls>" ],
    "manifest_version": 3,
    "name": "T",
    "permissions": [ "declarativeNetRequest", "declarativeNetRequestWithHostAccess","declarativeNetRequestFeedback", "storage", "tabs", "notifications"],
    "version": "1.0"
}
"""

    background_js = """
var info = {
  filter: "*",  // 匹配的url
  list_headers: %s  // 添加的头部列表
}


chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url) {
    /// info.filter = changeInfo.url.split('.').slice(-2).join('.').replace(/\//g, "");  // 这个需要先请求一边，然后第二次请求才会正确加上头部
    add_rules();
  }
});


function add_rules(){   
  // let requestHeaders = [];

  let filter = info.filter;
  let obj = {addRules: []};  // 规则集
  let list_headers = info.list_headers // 头部列表

  if (list_headers !== undefined && list_headers.length > 0)
  {
      let requestHeaders = [];
      
      for (let i = 0; i < list_headers.length; i++)
      {
          let row = list_headers[i];
          if (row.header == "")
              continue;

          requestHeaders.push({
              operation: "set",
              header: row.header,
              value: row.value
          });
          
      }

    if (requestHeaders.length > 0)
    {   
        obj.addRules = [{
            id: 1,
            priority: 1,
            condition: {
                "urlFilter": filter,
                "excludedRequestDomains": %s,
                "resourceTypes": ["csp_report", "font", "image", "main_frame", "media", "object", "other", "ping", "script", "stylesheet", "sub_frame", "webbundle", "websocket", "webtransport", "xmlhttprequest"]
            },
            action: {
                type: "modifyHeaders",
                requestHeaders: requestHeaders
            }
        }];


        chrome.declarativeNetRequest.getDynamicRules(function (res) {
          let rules = res.map((e) => e.id);
          chrome.declarativeNetRequest.updateDynamicRules(
            {
              addRules: obj.addRules, //Rule[] optional
              removeRuleIds: rules, //number[] optional
            },
            function (callback) {}
          );
        });
      

        chrome.notifications.create({
            type: "basic",
            title: "您修改的头部",
            iconUrl: "https://img-blog.csdn.net/20180302212146140?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2hlbnF1ZXlpbmc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70",
            message: JSON.stringify(requestHeaders),
          });
      };
  };
}
""" %(headers_list, bypass)

    try:
        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
    except Exception as e:
        raise Exception("浏览器添加自定义头部理插件创建失败")

    return plugin_file


# 禁止访问指定的 URL
def create_no_access_url_extension(black_list: list = [], plugin_path: str = None) -> str:
    """ 禁止访问指定的URL， 不支持正则

    Args:
        black_list: 禁止访问的URL ['.com', '.cc']
        plugin_file (str): 插件的输出路径。
    """
    plugin_file = 'black_url_plug.zip'

    if plugin_path is not None and not plugin_path.endswith(".zip"):  # 给的是目录
        plugin_file = os.path.join(plugin_path, plugin_file)
    else:
        plugin_file = plugin_path


    if type(plugin_file) != str:
        raise TypeError("指定的 plugin_file 参数类型错误")

    if not black_list:
        raise ValueError("未指定需要禁止访问的URL")

    # 最终的策略代码
    policy = ''

    for url in black_list:
        policy += """
    if (details.url.includes("%s")) {
      return {cancel: true}; // 取消请求
    }
        """ % (url)

    manifest_json = """
{
    "manifest_version": 2,
    "name": "禁止请求插件",
    "version": "1.0",
    "description": "禁止请求某些URL的插件",
    "permissions": [
      "webRequest",
      "webRequestBlocking",
      "<all_urls>"
    ],
    "background": {
      "scripts": ["background.js"],
      "persistent": true
    }
}

"""

    background_js = """
chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    // 在此处添加你的URL过滤逻辑
    %s
  },
  {urls: ["<all_urls>"]},
  ["blocking"]
);
""" %(policy)

    try:
        with zipfile.ZipFile(plugin_file, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
    except Exception as e:
        raise Exception("浏览器禁止访问指定URL插件创建失败")

    return plugin_file


if __name__ == "__main__":
    # create_add_headers_extension(headers={"A": "B"})
    # create_proxy_extension()
    # create_black_url_extension()
    pass