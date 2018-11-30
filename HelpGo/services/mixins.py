from django import forms
from django.forms.utils import ErrorList

class FormsUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.username = self.request.user
            return super(FormsUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged'])
            return self.form_invalid(form)

#El modelo se crea cuando el usuario se registra, entonces solo se debe modificar