from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import ApiGuide
from .utils import unique_slug_generator


@receiver(pre_save,sender=ApiGuide)
def get_api_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
