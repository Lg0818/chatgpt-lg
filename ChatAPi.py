# -*- coding: utf-8 -*-
from revChatGPT.V3 import Chatbot
from flask import Flask, request, render_template, jsonify
from gevent import pywsgi
import threading
# 这里的文件路径有问题
app = Flask(__name__, template_folder='/www/wwwroot/chatgpt')

# 初始化 Chatbot 对象
chatbot = Chatbot(api_key="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")

# 初始化缓存对象
cache = {}

@app.route("/")
def index():
    return render_template("index.html")

from flask import Response

# ...

@app.route('/chatbot', methods=['POST'])
def chatbot_route():
    input_value = request.form['input-field']

    # 尝试从缓存中获取结果
    if input_value in cache:
        sentence = cache[input_value]
    else:
        # 异步调用 chatbot.ask() 方法
        def ask_chatbot(input_value):
            result = []
            for data in chatbot.ask(input_value):
                result.append(data)
            return ''.join(result)

        def thread_job():
            sentence = ask_chatbot(input_value)
            cache[input_value] = sentence

        # 创建线程并启动
        t = threading.Thread(target=thread_job)
        t.start()
        t.join()

        # 从缓存中获取结果
        sentence = cache[input_value]

    # 创建 Response 对象，并设置响应头部的 Content-Type 字段为 text/plain;charset=utf-8
    response = Response(sentence, content_type='text/plain;charset=utf-8')
    return response


@app.route('/submit-form', methods=['POST'])
def submit_form():
    input_value = request.form['input-field']

    # 尝试从缓存中获取结果
    if input_value in cache:
        sentence = cache[input_value]
    else:
        # 异步调用 chatbot.ask() 方法
        def ask_chatbot(input_value):
            result = []
            for data in chatbot.ask(input_value):
                result.append(data)
            return ''.join(result)

        def thread_job():
            sentence = ask_chatbot(input_value)
            cache[input_value] = sentence

        # 创建线程并启动
        t = threading.Thread(target=thread_job)
        t.start()
        t.join()

        # 从缓存中获取结果
        sentence = cache[input_value]

    # 返回结果页面
    return render_template('result.html', sentence=sentence)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
