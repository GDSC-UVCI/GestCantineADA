from cantine.models.menu_model import MenuModel
from django.shortcuts import render, redirect
from cantine.forms.menu_forms import MenuForm


def menu_list(request):
    menus = MenuModel.objects.all()
    context = {
        'menus': menus,
        'total': menus.count(),
        'title': 'Menus'
    }
    return render(request, 'menus.html', context)


def menu_add_and_edit(request, pk=None):
    if pk:
        menu = MenuModel.objects.get(pk=pk)
    else:
        menu = None

    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('cantine:menu_list')
    else:
        form = MenuForm(instance=menu)
    context = {
        'form': form,
        'title': 'Menus'
    }
    return render(request, 'forms.html', context)