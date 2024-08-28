from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from app.forms import ResourceForm
from app.models import Resource
from app.service.yandex_disk import get_meta_data, get_items, download_item


@login_required
def resource_list(request):
    resources = request.user.resources.all()
    return render(request, 'app/resource/list.html', {
        'resources': resources
    })


@login_required
def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            try:
                resource = form.save(commit=False)
                resource.yd_created_at = datetime.strptime(request.POST.get('yd_created_at'), '%Y-%m-%dT%H:%M:%S%z')
                resource.user = request.user
                resource.save()
                messages.success(request, 'Диск сохранен')
            except:
                messages.error(request, 'Данный диск уже создан')
        else:
            messages.error(request, 'Ошибка при сохранении формы')
    return redirect(reverse('app:resource_list'))


@login_required
def resource_detail(request, public_url):
    resource = get_object_or_404(Resource, user=request.user, public_url=public_url)
    items = get_items(resource.public_url)
    return render(request, 'app/resource/detail.html', {
        'resource': resource,
        'items': items
    })


@login_required
def delete_resource(request, public_url):
    resource = get_object_or_404(Resource, user=request.user, public_url=public_url)
    resource.delete()
    messages.error(request, 'Ресурс удален')
    return redirect(reverse('app:resource_list'))


@login_required
def download_resource_item(request, public_key, path):
    url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}?path={path}'
    return redirect(url)


@login_required
def resource_meta_data(request, public_url: str):
    meta_data = get_meta_data(public_url)
    if meta_data:
        return JsonResponse(
            {
                'name': meta_data.get('name'),
                'public_key': meta_data.get('public_key'),
                'public_url': meta_data.get('public_url'),
                'yd_created_at': meta_data.get('created'),
                'owner': meta_data.get('owner', {}).get('display_name'),
                'total': meta_data.get('_embedded', {}).get('total', 0),
                'is_found': True
            }
        )
    return JsonResponse({})
