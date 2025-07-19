from django.shortcuts import render

from data.models import Quotes


def chart_view(request):
    quotes = Quotes.objects.all().order_by('-likes')[:10]
    data = {
        'quotes': quotes,
    }
    return render(request, 'chart/chart.html', data)