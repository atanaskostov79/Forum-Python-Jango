from app.models import Theme


def getThemes(request):
    # themes = Theme.objects.all()
    themes = {}
    return {'themes': themes}

