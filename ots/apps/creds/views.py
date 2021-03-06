from uuid import UUID
from django.views.generic import DetailView, CreateView
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from . import forms
from . import qr_utils
from .models import Secret


class ValidateUUIDMixin(object):

    def get_object(self, queryset=None):
        try:
            UUID(self.kwargs.get(self.pk_url_kwarg))
        except Exception:
            raise Http404()
        obj = super().get_object(queryset=None)
        if obj.expired:
            raise Http404("The page has expired.")
        if obj.require_login and not self.request.user.is_authenticated():
            raise Http404("Login required.")
        return obj


class ViewCred(ValidateUUIDMixin, DetailView):
    model = Secret
    template_name = "creds/view_creds.html"
    context_object_name = "secret"

    def get_context_data(self, **kwargs):
        now = timezone.now()
        obj = self.get_object()
        obj.expire_count += 1
        if obj.expire_count >= obj.expire_max_count:
            obj.expire()
        if obj.expire_date and obj.expire_date < now:
            obj.expire()
        obj.save()
        return super().get_context_data(**kwargs)


class ViewCredLink(ValidateUUIDMixin, DetailView):
    model = Secret
    template_name = "creds/view_creds_link.html"


class ViewCredLinkQR(ValidateUUIDMixin, DetailView):
    model = Secret
    template_name = "creds/view_creds_link.html"

    def render_to_response(self, context, **response_kwargs):
        img = qr_utils.gen_qr(self.object.get_secret_url())
        response = HttpResponse(content_type='image/png')
        img.save(response, "PNG")
        return response


class CreateCred(CreateView):
    model = Secret
    template_name = "creds/create_creds.html"
    form_class = forms.SecretForm

    def get_success_url(self):
        return reverse_lazy("view_creds_link", args=[self.object.id])
