from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.urls import reverse

from .models import ApiGuide,Suggestion
from .utils import unique_slug_generator

from  urllib.parse import urljoin

@receiver(pre_save,sender=ApiGuide)
def get_api_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(post_save,sender=Suggestion)
def send_suggestion(sender,instance,created,**kwrags):
    if created:
        url_ = urljoin(getattr(settings,'BASE_URL'),reverse('main:suggestion-read',kwargs={"pk":instance.id}))
        context = {'obj':instance,'url':url_}
        txt_ = get_template('snippets/suggestion_text_message.txt').render(context)
        html_ = get_template('snippets/suggestion_html_message.html').render(context)
        recipient_list = [getattr(settings,'MAIN_EMAIL')]
        email = send_mail(instance.subject, txt_, instance.email, recipient_list,html_message=html_, fail_silently=False)
        print(email,'sending status')