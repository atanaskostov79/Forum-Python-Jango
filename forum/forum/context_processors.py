from app.models import Theme


def getThemes(request):
    themes = Theme.objects.all()

    return {'themes': themes}

