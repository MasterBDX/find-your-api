from main.models import SiteInfo

def site_name(request):
    obj = SiteInfo.objects.order_by().values('title','portfolio_url').last()
    if obj:
        return obj
    return {}