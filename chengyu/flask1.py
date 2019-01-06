
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def geocode(word)->str:
    parameters = {'word':word,'key':'40eea0dfa42690ad3b9800af162155bd'}
    base = 'http://v.juhe.cn/chengyu/query'
    response = requests.get(base, parameters)
    answer = response.json()
    return answer


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    word = request.form['word']
    title = '这是查询结果:'
    results = geocode(word)
    return render_template('results.html',
                           the_title=title,
                           the_word=word,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎使用成语词典')


if __name__ == '__main__':
    app.run(debug=True)
