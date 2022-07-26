from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def removepunc(string):
    output = ''
    for i in string:
        if i in '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''':
            pass
        else:
            output += i
    print(output)
    return output


def removespace(string):
    string=string.strip()
    output=''
    for i in range(1,len(string)):
        if string[i-1]==' ' and string[i]==' ':
            pass
        else:
            output+=string[i-1]
    return output+string[len(string)-1]


def analyze(request):
    output = ''
    method_string = ''

    # get data from homepage
    txt = request.POST.get('text', 'ERROR')
    method = request.POST.get('method', None)
    
    # analyze data accordsing to checked radio button
    if method == 'removepunc':
        output = removepunc(txt)
        method_string = 'Remove Punctuations'
    elif method == 'capitalize':
        output = txt.upper()
        method_string = 'Capitalize'
    elif method == 'minimize':
        output = txt.lower()
        method_string = 'Minimize'
    elif method == 'removespace':
        output = removespace(txt)
        method_string = 'Remove Extra Space'

    params = {
        'method_heading': method_string,
        'output': output
    }

    return render(request, 'analyze.html', params)
