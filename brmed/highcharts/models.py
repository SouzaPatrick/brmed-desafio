from brmed.utils.models import BaseModel
from brmed.users.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models

class Quote(BaseModel):
    url = models.URLField(verbose_name=_("url"), null=True, blank=True)
    quote_brl = models.DecimalField(verbose_name=_("Quote BRL"), max_digits=20, decimal_places=2, null=True, blank=True)
    quote_eur = models.DecimalField(verbose_name=_("Quote EUR"), max_digits=20, decimal_places=2, null=True, blank=True)
    quote_jpy = models.DecimalField(verbose_name=_("Quote JPY"), max_digits=20, decimal_places=2, null=True, blank=True)
    response = models.JSONField(
        verbose_name=_("response"),
        blank=True,
        null=True,
    )
    status_code = models.IntegerField(
        verbose_name=_("status code"),
        default=0,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["id"]
