from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.views.generic import UpdateView
from data.models import Sources, Quotes
from .forms import SourceForm, QuoteForm
from django.db.models import F
from django.http import HttpResponseRedirect


def edit_quote_view(request):
    sources = Sources.objects.order_by('source')
    sources_quotes = []
    for source in sources:
        sources_quotes.append({'source': {'name' :f'{source.source}', 'id': f'{source.id}'},
                               'quotes': [quote.__dict__ for quote in Quotes.objects.filter(source__exact=source.id)]})
    return render(request, 'edit/edit.html', {'sources_quotes': sources_quotes})


class AddQuoteView(FormView):
    template_name = 'edit/addquote.html'
    form_class = QuoteForm
    success_url = reverse_lazy('edit_start')

    def form_valid(self, form):
        quote = form.save(commit=False)
        quote.source = Sources.objects.get(pk=self.kwargs['pk'])
        form.save()
        Sources.objects.filter(pk=self.kwargs['pk']).update(usage=F('usage') + 1)
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, f"Ошибка: {form.errors} ")
        return super().form_invalid(form)


class EditQuoteView(UpdateView):
    model = Quotes
    fields = ['quote', 'weight']
    template_name = 'edit/editquote.html'
    success_url = reverse_lazy('edit_start')
    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, f"Ошибка: {form.errors} ")
        return super().form_invalid(form)


class AddSourceView(FormView):
    template_name = 'edit/addsource.html'
    form_class = SourceForm
    success_url = reverse_lazy('edit_start')

    def form_valid(self, form):
        source = form.save(commit=False)
        form.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, f"Ошибка: {form.errors} ")
        return super().form_invalid(form)


def delete_source(request, pk):
    Sources.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('edit_start'))


def delete_quote(request, pk):
    Quotes.objects.filter(pk=pk).delete()
    Sources.objects.filter(pk=pk).update(usage=F('usage') - 1)
    return HttpResponseRedirect(reverse('edit_start'))