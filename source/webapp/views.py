from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Photography
from django.contrib.auth import authenticate, login, logout


class IndexView(ListView):
    model = Photography
    template_name = 'index.html'
    ordering = ['-created_date']


class PhotoView(DetailView):
    model = Photography
    template_name = "photo/detail.html"


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photography
    template_name = 'photo/create.html'
    fields = ("photo", "caption")

    def form_valid(self, form):
        self.object = Photography.objects.create(photo=form.cleaned_data["photo"], caption=form.cleaned_data["caption"],
                                                 photo_author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.object.pk})


class PhotoUpdateView(UpdateView):
    model = Photography
    template_name = 'photo/update.html'
    fields = ('photo', 'caption')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.has_perm('webapp.change_photography') or self.object.author != request.user.pk:
            raise PermissionDenied('403 Forbidden')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    model = Photography
    template_name = 'photo/delete.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.has_perm('webapp.delete_photography') or self.object.author != request.user:
            raise PermissionDenied('403 Forbidden')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:index')




def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('webapp:index')