from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from openai import ChatCompletion

from .forms import PromptForm


@login_required
def chat(request):
    if request.method == 'POST':
        prompt_form = PromptForm(data=request.POST)
        if prompt_form.is_valid():
            pass
    else:
        prompt_form = PromptForm()
    return render(request,
                  'account/edit.html',
                  {'prompt_form': prompt_form})
