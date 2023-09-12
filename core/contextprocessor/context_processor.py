from core.models import Settings

def get_settings(request):
    context = {
        'settings' : Settings.objects.first(),
    }
    return context