from flask import Flask
from flask import render_template, request
import config  # 配置文件
import json
from normally import chat_normally

app = Flask(__name__)
app.config.from_object(config)


def receive(ans):

    get_ans = chat_normally(ans, 1000, 0.9)
    return get_ans.talk()


@app.route("/form", methods=['GET', 'POST'])
def post():

    if request.method == 'POST':

        get_ques = request.form['questions']
        answer_back = receive(get_ques)
        return render_template('form.html', answer=answer_back)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4000', debug=True)
