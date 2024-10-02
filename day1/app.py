from flask import Flask, render_template, request

app123 = Flask(__name__)

@app123.route('/anchit')
def test():
    return 'hello world abc'

@app123.route('/test', methods=['GET', 'POST'])
def test1():
    var1 = 'this is coming from the backend'
    data = request.form.get('name')
    print(data)
    return render_template('test.html', var2=var1)


if __name__ == '__main__':
    app123.run(debug=True)