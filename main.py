from flask import Flask, request, render_template
from translate import Translator

app = Flask(__name__)

def translate_text(text, input_language, output_language):
    translator = Translator(from_lang=input_language, to_lang=output_language)
    translation = translator.translate(text)
    return translation

@app.route("/", methods=["GET", "POST"])
def interpreter():
    if request.method == 'POST':
        text = request.form['text']
        input_language = request.form['input_language']
        output_language = request.form['output_language']
        translated_text = translate_text(text, input_language, output_language)
        return render_template('main.html', text=text, translated_text=translated_text, input_language=input_language, output_language=output_language)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
