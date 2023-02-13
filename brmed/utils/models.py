from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(null=False, blank=True, default=timezone.now)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if kwargs.get("update_fields"):
            kwargs["update_fields"] = list(
                set(list(kwargs["update_fields"]) + ["updated_at"])
            )
        return super().save(*args, **kwargs)
