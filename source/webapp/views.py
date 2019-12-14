from django.contrib.auth import authenticate
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


class PhotoCreateView(CreateView):
    model = Photography
    template_name = 'photo/create.html'
    fields = ("photo", "caption")

    def form_valid(self, form):
        self.object = Photography.objects.create(photo=form.cleaned_data["photo"], caption=form.cleaned_data["caption"], photo_author=self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.object.pk})

    # def form_valid(self, form):
    #     print("hhhfhhf")
    #     author = self.request.user
    #     photo = form.cleaned_data["photo"]
    #     caption = form.cleaned_data["caption"]
    #     self.object = Photography.objects.create(photo_author=author, photo=photo, caption=caption)
    #     # form.save()

        # return reverse("webapp:photo_view", kwargs={"pk": self.object.pk})

    # def add_author_to_photo(self, form):
    #     author = self.request.user
    #     photo = form.cleaned_data["photo"]
    #     caption = form.cleaned_data["caption"]
    #     self.object = Photography.objects.create(author=author, photo=photo, caption=caption)
    #     form.save()
    #     print(author)
    #     print(self.object)
    #     return self.get_success_url()


class PhotoUpdateView(UpdateView):
    model = Photography
    template_name = 'photo/update.html'
    fields = ('photo', 'caption')

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(DeleteView):
    model = Photography
    template_name = 'photo/delete.html'

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