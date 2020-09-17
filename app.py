from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        file = request.files.get('file1', None)
        text = request.form.get('text1', None)
        radio = request.form.get('radio', None)
        check = request.form.getlist('check', None)

        filename = file.filename if file is not None else None
        text = text if text is not None else None
        radio = radio if radio is not None else None
        check = check if check is not None else None

        return render_template('index.html',
                               filename=filename,
                               text=text,
                               radio=radio,
                               check=check)


if __name__ == '__main__':
    app.run()
