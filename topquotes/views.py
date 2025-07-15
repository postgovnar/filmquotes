from django.shortcuts import render

def top_quotes_view(request):
    return render(request, 'topquotes/topquotes.html')
