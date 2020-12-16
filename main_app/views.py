from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Winery, Wine, Grape
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')


class WineryCreate(LoginRequiredMixin, CreateView):
  model = Winery
  fields = ['name', 'address', 'region', 'county', 'city', 'state', 'zipcode', 'img_url', 'logo_url']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WineryUpdate














##This is the logic for the map page
  # template_name = '{TEMPLATE_NAME.html}' 

  # def get_context_data(self, **kwargs):
  #     context = super(IndexView, self).get_context_data(**kwargs)
  #     context['plot'] = map_us.render_map()
  #     return context
  
  
  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

