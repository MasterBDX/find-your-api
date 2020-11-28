from django.db import models


class APIGuideManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)