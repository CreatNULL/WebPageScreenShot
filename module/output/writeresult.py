# -*- coding: UTF-8 -*-
import os
import threading
import uuid


class WriteResult:
    """记录访问URL结果的类"""

    def __init__(self, output: str):
        """初始化输出文件路径"""
        self.__html_lock = threading.Lock()  # 创建互斥锁
        self.__record_success_lock = threading.Lock()  # 记录访问成功的锁
        self.__record_error_lock = threading.Lock()  # 记录访问失败的锁
        self.__result_output = os.path.join(output, 'result.html')
        self.__success_output = os.path.join(output, 'success_url.txt')
        self.__error_output = os.path.join(output, 'error_url.txt')

        if not os.path.exists(output):
            raise FileNotFoundError('The specified path does not exist')

    def write_html_head(self):
        """创建 HTML 样板的样式"""
        html_head_report = """
        <!DOCTYPE html>
        <html lang="zh">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>网页截图 - screenshort_url</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                    margin: 0;
                    padding: 20px;
                }
                .web_page_box {
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    margin-bottom: 30px;
                    padding: 20px;
                }
                h2 {
                    color: #333;
                    cursor: pointer;
                    user-select: none; /* 禁止选中文本 */
                }
                p {
                    color: #555;
                }
                img {
                    max-width: 100%;
                    height: auto;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                pre {
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow: auto;
                }
                .content {
                    display: none; /* 默认隐藏内容 */
                }
            </style>
            <script>
                function toggleContent(id) {
                    const content = document.getElementById(id);
                    content.style.display = content.style.display === 'block' ? 'none' : 'block';
                }
            </script>
        </head>
        <body>
        """
        with open(self.__result_output, 'w', encoding='utf-8') as file:
            file.write(html_head_report)

    def write_html_body(self, data: dict):
        """写入 html body 标签"""
        content_id = f"content-{uuid.uuid4()}"
        thumbnail_src = f"data:image/png;base64,{data['screenshot']}"  # 使用截图作为缩略图
        html_report = f"""
        <div class="web_page_box">
            <h2 style="display: flex; justify-content: space-between; align-items: center;" onclick="toggleContent('{content_id}')">
                <span>{data['title']}</span>
                <img src="{thumbnail_src}" alt="Thumbnail" class="thumbnail" width="80px" height="50px"
                     onmouseover="showModal('{thumbnail_src}')"
                     onmouseout="hideModal()">
            </h2>
            <div id="{content_id}" class="content">
                <p><strong>原始 URL: <a href={data.get('url','无')}>{data.get('url','无')}</a></p>
                <p><strong>访问后 URL:</strong> <a href={data.get('tab_url','无')}>{data.get('tab_url','无')}</a></p>
                <h3>请求方法</h3>
                <pre>{data.get('method', '无')}</pre>
                <h3>状态码</h3>
                <pre>{data.get('status_code', '无')}</pre>
                <h3><strong>User-Agent:</h3>
                <pre>{data.get('user_agent', '无')}</pre>
                <h3>通过参数指定的-请求参数</h3>
                <pre>{data.get('params', '无')}</pre>
                <h3>通过参数指定的-请求头</h3>
                <pre>{data.get('headers', '无')}</pre>
                <h3>通过参数指定的-请求数据</h3>
                <pre>{data.get('data', '无')}</pre>
                <h3>请求 JSON</h3>
                <pre>{data.get('json', '无')}</pre>
                <h3>请求文件</h3>
                <pre>{data.get('files', '无')}</pre>
                <h3>响应 JSON</h3>
                <pre>{data['response_json']}</pre>
                <h3>代理设置</h3>
                <pre>{data.get('proxy', '无')}</pre>
                <h3>超时设置</h3>
                <pre>{data['timeouts']}</pre>
                <h3>重试设置</h3>
                <pre>重试次数: {data['retry_times']}, 重试间隔: {data['retry_interval']}</pre>
                <h3>页面加载策略</h3>
                <pre>{data['load_mode']}</pre>
                <h3>截图</h3>
                <img src="data:image/png;base64,{data['screenshot']}" alt="Screenshot">
            </div>
        </div>
    
        <div id="modal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background-color:rgba(0,0,0,0.8); justify-content:center; align-items:center; z-index:1000;">
            <img id="modalImage" style="max-width:90%; max-height:90%; margin:auto;">
        </div>
        <script>
            function showModal(src) {{
                const modal = document.getElementById('modal');
                const modalImage = document.getElementById('modalImage');
                modalImage.src = src;
                modal.style.display = 'flex';
            }}
            function hideModal() {{
                const modal = document.getElementById('modal');
                modal.style.display = 'none';
            }}
        </script>
        """
        with self.__html_lock:
            with open(self.__result_output, 'a+', encoding='utf-8') as file:
                file.write(html_report)

    def write_html_foot(self):
        """创建 HTML 样板的尾部样式"""
        html_tail_report = """
        </body>
        </html>
        """
        with open(self.__result_output, 'a+', encoding='utf-8') as file:
            file.write(html_tail_report)

    def write_success_url(self, url: str):
        """记录访问成功的URL"""
        with self.__record_success_lock:
            with open(self.__success_output, 'a+', encoding='utf-8') as file:
                file.write(str(url) + '\n')

    def write_error_url(self, url: str):
        """记录访问失败的URL"""
        with self.__record_error_lock:
            with open(self.__error_output, 'a+', encoding='utf-8') as file:
                file.write(str(url) + '\n')
