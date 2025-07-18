from django.shortcuts import render

def main_quote_view(request):
    return render(request, 'main/main.html')

