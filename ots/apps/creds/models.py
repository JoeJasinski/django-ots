import uuid
from django.db import models
from django.urls import reverse_lazy
from django.contrib.sites.models import Site
from django_cryptography.fields import encrypt
from . import SITE_SCHEME, PAGE_REFRESH


class Secret(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    text = encrypt(models.TextField(help_text="Secret message."))
    expire_date = models.DateTimeField(
        "Expiration Date",
        help_text=(
            "The date and time that the secret will expire. "
            "If empty, it will not expire based on time."),
        blank=True, null=True)
    expire_count = models.PositiveSmallIntegerField(
        "Expire Count",
        help_text=(
            "The number of times this secret has been viewed"),
        default=0)
    expire_max_count = models.PositiveSmallIntegerField(
        help_text=(
            "The number of times this secret can be viewed before it expires. "
            "The default is 1."),
        default=1)
    expired = models.BooleanField(default=False)
    require_login = models.BooleanField(
        help_text="If checked, the user must be logged in to view.",
        default=False)
    page_refresh = models.PositiveIntegerField(
        help_text=(
            "If an integer is provided, the page will refresh after "
            "the given number of seconds. The default is {} seconds.".format(
                PAGE_REFRESH)),
        default=PAGE_REFRESH,
    )

    def get_secret_url(self):
        domain = Site.objects.get_current().domain
        scheme = SITE_SCHEME
        return "{}://{}{}".format(
            scheme, domain, reverse_lazy("view_creds", args=[self.id]))

    def get_absolute_url(self):
        return reverse_lazy("view_creds_link", args=[self.id])

    def expire(self, save=True):
        self.expired = True
        self.text = ""
        if save:
            self.save()

    def __str__(self):
        return self.text
