from django.conf import settings


PAGE_REFRESH = getattr(settings, "PAGE_REFRESH", 500)

SITE_SCHEME = getattr(settings, "SITE_SCHEME", "https")
