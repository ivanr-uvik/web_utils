from django.core.exceptions import BadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
from .utils import is_string_an_url, shorten
from .models import ShortedURL


# Create your views here.


@require_POST
@csrf_exempt
def short_url_view(request):
    # Get Input Params
    full_url = request.POST["url"]
    # Do validation here
    is_url = is_string_an_url(full_url)
    if not is_url:
        raise BadRequest("Not a valid URL")
    # Build shorten URL
    short = shorten(full_url)

    # Find an existing model if any
    shorted_url = ShortedURL.objects.filter(shorted=short).first()
    if shorted_url:
        shorted_url.counter += 1
        shorted_url.save()
    else:
        shorted_url = ShortedURL()
        shorted_url.full_url = full_url
        shorted_url.shorted = short
        shorted_url.counter = 1
        shorted_url.save()

    # Build and return template
    short_url = request.build_absolute_uri(f"/{shorted_url.shorted}")
    result = {"shorted_url": short_url}

    return JsonResponse(result)


@require_GET
def get_shorted_url_view(request, short_url):

    shorted_url = get_object_or_404(ShortedURL, shorted=short_url)

    return redirect(shorted_url.full_url)
