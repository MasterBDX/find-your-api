from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import User
from .utils import unique_slug_generator


@receiver(pre_save, sender=User)
def get_user_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.get_or_create(user=instance)
