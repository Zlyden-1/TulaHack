from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Events
from account.models import UserPreferences


def index(request):
    return render(request, 'recommendations/index.html')


class UnloggedEventsListView(ListView):
    template_name = "recommendations/index.html"

    def get_queryset(self):
        self.events = get_object_or_404(Events, name=self.kwargs["events"])
        return Events.objects.all()[:6]


@login_required
class LoggedEventsListView(ListView):
    template_name = "recommendations/index.html"

    def get_queryset(self):
        user = self.request.user
        interests = UserPreferences.objects.filter(profile=user.profile)
        self.events = get_object_or_404(Events, name=self.kwargs["events"])
        # events = Events.objects.all
        #
        # events_dict = {event: sum([user.])/len() for event in Events.objects.all}
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

