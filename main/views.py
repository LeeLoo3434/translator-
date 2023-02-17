from django.shortcuts import render
from googletrans import LANGUAGES, Translator

def translate(request):
    text = request.GET.get('text', '')
    if not text:
        return render(request, 'translate.html', {'languages': LANGUAGES})
    source = request.GET.get('source', 'auto')
    dest = request.GET.get('destination', 'en')
    translator = Translator()
    detected_language = translator.detect(text)
    translation = translator.translate(text, src=source, dest=dest)
    return render(request, 'translate.html', {'languages': LANGUAGES, 'translation': translation})
