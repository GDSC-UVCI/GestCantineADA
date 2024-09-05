from django.shortcuts import render, redirect
from cantine.models.dishe_model import DishesModel
from cantine.forms.dishe_forms import DishesForm

def dishes_list(request):
    dishes = DishesModel.objects.all()
    context = {
        'dishes': dishes,
        'total': dishes.count(),
        'title': 'Plats'
    }
    return render(request, 'plats.html', context)


def dishes_add_and_edit(request, pk=None):
    if pk:
        dish = DishesModel.objects.get(pk=pk)
    else:
        dish = None

    if request.method == 'POST':
        form = DishesForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('cantine:dishes_list')
    else:
        form = DishesForm(instance=dish)
    context = {
        'form': form,
        'title': 'Plats'
    }
    return render(request, 'forms.html', context)

def dishes_delete(request, pk):
    dish = DishesModel.objects.get(pk=pk)
    dish.delete()
    return redirect('cantine:dishes_list')