from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic

from .models import User


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class IndexUserView(generic.ListView):
    template_name = 'agendapp/index.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()

class CreateUserView(SuccessMessageMixin, generic.CreateView):
    model = User
    fields = '__all__'
    template_name = 'agendapp/create.html'
    success_url = reverse_lazy('agendapp:index')
    success_message = "User %(name)s created!"

class EditUserView(SuccessMessageMixin, generic.UpdateView):
    model = User
    fields = '__all__'
    template_name = 'agendapp/edit.html'
    success_url = reverse_lazy('agendapp:index')
    success_message = "User %(name)s updated!"

class DeleteUserView(SuccessMessageMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy('agendapp:index')
    success_message = "User deleted!"