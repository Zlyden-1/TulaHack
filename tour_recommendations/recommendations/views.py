from django.shortcuts import render
from .models import Events
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'recommendations/index.html')


class EventsListView(ListView):
    template_name = ""

    def get_queryset(self):
        self.events = get_object_or_404(Events, name=self.kwargs["events"])
        return Events.objects.all()


class EventDetailView(DetailView):
    queryset = Events.objects.all()

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        obj.save()
        return obj


class EventCreateView(CreateView):
    model = Events
    fields = ['title', 'city', 'location', 'date', 'end_reg', 'categories', 'description', 'image']


class EventUpdateView(UpdateView):
    model = Events
    fields = ['title', 'city', 'location', 'date', 'end_reg', 'categories', 'description', 'image']
    template_name_suffix = '_update_form'


class EventDeleteView(DeleteView):
    model = Events
    success_url = reverse_lazy('event-list')

