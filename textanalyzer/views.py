from django.shortcuts import render
from django.http import HttpResponse
from Functions import Functions 
from django.views.decorators.csrf import csrf_exempt


def message_filter(message):
    message_list = message.split()
    trash = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
             '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/',
             '?']
    filtered_words = []
    for word in message_list:
        filtered_word = ''.join(char for char in word if char not in trash)
        if filtered_word:
            filtered_words.append(filtered_word)

    joined = ' '.join(filtered_words)
    return joined



def index(request):
    params = {"name": "Text-Analyzer", 'desc': Functions.Words_Capitalzer('A Place to do anything with your text')}
    return render(request, 'index.html', params)


@csrf_exempt
def analyze(request):
    text = request.POST.get('text', 'default')
    cap = request.POST.get('cap', 'off')
    filtering = request.POST.get('filter', 'off')
    length = request.POST.get('length', 'off')
    main = {"cap": cap, "filter": filtering, "length": length}
    funcs = {"cap": f"Your Text UpperCase: {Functions.Words_Upper(text)}", "filter": f'Your Text After Filter: {message_filter(text)}', "length": f"Your Text Length: {len(text)}"}
    execute = []
    values = []

    for i in main:
        if main[i] == 'on':
            execute.append(i)

    for i in execute:
        val = funcs[i]
        values.append(val)

    params = {"output": ' '.join(values), "name": "Text-Analyzer"}

    return render(request, 'analyze.html', params)

