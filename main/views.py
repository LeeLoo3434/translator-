from googletrans import LANGUAGES, Translator
from django.shortcuts import render

def translate(request):
    text = request.GET.get('text', '')
    if not text:
        return render(request, 'translate.html', {'languages': LANGUAGES})
    source = request.GET.get('source', 'auto')
    dest = request.GET.get('destination', 'en')
    translator = Translator()
    if source != 'auto':
        detected_language = None
    else:
        detected_language = translator.detect(text).lang
    translation = translator.translate(text, src=source, dest=dest)
    if not translation:
        translation = None
    source_language = LANGUAGES.get(source)
    destination_language = LANGUAGES.get(dest)
    return render(request, 'translate.html', {'languages': LANGUAGES, 'translation': translation, 'detected_language': detected_language, 'text': text, 'source_language': source_language, 'destination_language': destination_language})



