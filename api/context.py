from main.models import SiteInfo

def site_name(request):
    obj = SiteInfo.objects.values('title').last()
    if obj:
        return obj
    return {}