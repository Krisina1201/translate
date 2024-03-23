def translate():
    from translate import Translator

    def translate_text(text, target_language):
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation

    text_to_translate = input("Введи текст который хочешь перевезти: \n")
    target_language = "ru"
    count = 0

    translated_text = translate_text(text_to_translate, target_language)


    if text_to_translate == translated_text:
        text_to_translate = input("Твой текст введен не корректно, провь его содержимое и введи его занаво: \n")
        translated_text = translate_text(text_to_translate, target_language)

    print(f"Вот твой переведенный текст: \n {translated_text}")

