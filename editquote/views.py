from django.shortcuts import render

def edit_quote_view(request):
    return render(request, 'editquote/editquote.html')
