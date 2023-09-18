from django.shortcuts import render
from django.http import HttpResponse
from .models import Process, Operation, Reestr
# from .models import Process
from .forms import ProcessForm, OperatinForm
import logging
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


def reestr(request):
    str_reestr = Reestr.objects.all()
    # print(str_reestr)
    context = {
        "reestr": str_reestr
    }
    return render(request, "fk_app/reestr.html", context)


def add_process(request):
    name = 'Добавление процесса'
    if request.method == 'POST':
        form = ProcessForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            # logger.info(f'Получили {name=}, {email=}, {age=}.')
            process = Process(name=name)
            process.save()
            message = 'Процес сохранён'
    else:
        form = ProcessForm()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})

def add_operation(request):
    name = 'Добавление операции'
    if request.method == 'POST':
        form = OperatinForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            process = form.cleaned_data['process']
            operation = Operation(name=name, process=process)
            operation.save()
            message = 'Операция сохр.'
    else:
        form = OperatinForm()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})

#
# def update_product(request):
#     name = 'Изменение продукта'
#     if request.method == 'POST':
#         form = ProductFormUpdate(request.POST, request.FILES)
#         message = 'Ошибка в данных'
#         if form.is_valid():
#             product = form.cleaned_data['products']
#             old_product = Product.objects.filter(pk=product.pk).first()
#             name = form.cleaned_data['name']
#             description = form.cleaned_data['description']
#             price = form.cleaned_data['price']
#             quantity = form.cleaned_data['quantity']
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#             # logger.info(f'Получили {name=}, {email=}, {age=}.')
#             # old_product(name=name, description=description, price=price, quantity=quantity, image=image.name)
#             old_product.name = name
#             old_product.description = description
#             old_product.price = price
#             old_product.quantity = quantity
#             old_product.image = image.name
#             old_product.save()
#             message = 'product сохранён'
#     else:
#         form = ProductFormUpdate()
#         message = 'Заполните форму'
#
#     return render(request, 'hw4/product.html', {'form': form, 'message': message, 'name': name})

#
def index(request):
    return render(request, 'fk_app/index.html')


def about(request):
    return render(request, 'fk_app/about.html')