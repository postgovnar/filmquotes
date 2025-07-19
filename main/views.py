from django.shortcuts import render
from data.models import Sources, Quotes
import random
from django.http import JsonResponse, HttpResponse


def main_quote_view(request):
    quote = random_quote()
    quote.views += 1
    quote.save()
    data = {'quote': quote}
    return render(request, template_name='main/main.html', context=data)


def random_quote():
    quotes = list(Quotes.objects.values('id', 'weight'))
    hat = []
    for quote in quotes:
        hat += [quote['id']] * quote['weight']
    return Quotes.objects.get(id=random.choice(hat))


def vote(request, qid):
    if request.method != 'POST':
        return HttpResponse("Ошибка")

    quote = Quotes.objects.get(id=qid)
    action = request.POST.get('action')
    previous_action = request.POST.get('previous_action')

    if action == 'like':
        quote.likes += 1
        if previous_action == 'dislike':
            quote.dislikes -= 1
    elif action == 'dislike':
        quote.dislikes += 1
        if previous_action == 'like':
            quote.likes -= 1
    elif action == 'cancel':
        if previous_action == 'like':
            quote.likes -= 1
        elif previous_action == 'dislike':
            quote.dislikes -= 1

    quote.save()
    return JsonResponse({
        'likes': quote.likes,
        'dislikes': quote.dislikes
    })