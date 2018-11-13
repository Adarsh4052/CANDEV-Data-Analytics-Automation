from django.shortcuts import render

from .models import ConsumerPriceIndex


def index(request):
    data = [
        [index.date.strftime('%B, %Y'), float(index.all_fields), float(index.food), float(index.shelter), float(index.transportation)]
        for index in ConsumerPriceIndex.objects.all()
    ]

    context = {'data': data}
    return render(request, 'indicators/gdp.html', context)
