# -*- coding: utf-8 -*-
from revChatGPT.V3 import Chatbot
import asyncio
from flask import Flask, request, render_template
app = Flask(__name__, template_folder='/Users/ligang/Desktop/git/test1')

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit-form', methods=['POST'])
def submit_form():
        input_value = request.form['input-field']
        print(input_value)
    # 处理 input_value 数据
        chatbot = Chatbot(api_key="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")
        for data in chatbot.ask(input_value):
            print(data, end="", flush=True)
            result = list(chatbot.ask(input_value))
            sentence = ''.join(result)
        return sentence

if __name__ == "__main__":
    app.run()





