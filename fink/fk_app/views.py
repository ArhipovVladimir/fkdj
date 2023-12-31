from django.shortcuts import render
from django.http import HttpResponse
from .models import Process, Operation, Reestr, Certificate_of_violations, Violation, Journal
# from .models import Process
from .forms import ProcessForm, OperatinForm, SertifForn, \
    VolitionForm, RegViolationForm, VolitionGetForm, VolitionFormUpdate, UpdateRegViolationForm, VolitionFormThe
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



# добавление справки о нарушении
def add_sertif(request):
    name = 'Регистрация справки'
    if request.method == 'POST':
        form = SertifForn(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            date = form.cleaned_data['date']
            worker = form.cleaned_data['worker']
            certificate_of_violations = Certificate_of_violations(date=date, worker=worker)
            certificate_of_violations.save()
            message = 'Сохранено'
    else:
        form = SertifForn()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})


# добавление строки в справку о нарушении
def add_violation(request):
    name = 'Регистрация строки в справку'
    if request.method == 'POST':
        form = VolitionForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            cer_vio = form.cleaned_data['certificate_of_violations']
            cer_vio_select = Certificate_of_violations.objects.filter(pk=cer_vio.pk).first()
            reestr = form.cleaned_data['reestr']
            title = form.cleaned_data['title']
            worker_act = form.cleaned_data['worker_act']
            employ_position_act = form.cleaned_data['employ_position_act']
            amount = form.cleaned_data['amount']
            violation = Violation(certificate_of_violations=cer_vio_select ,reestr=reestr, title=title,
                                  employ_position_act=employ_position_act, worker=worker_act, amount=amount)
            violation.save()
            message = 'Сохранено'
    else:
        form = VolitionForm()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})

def add_violation_the(request, oper_id):
    name = 'Регистрация строки в справку'
    if request.method == 'POST':
        form = VolitionFormThe(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            cer_vio = form.cleaned_data['certificate_of_violations']
            cer_vio_select = Certificate_of_violations.objects.filter(pk=cer_vio.pk).first()
            reestr = Reestr.objects.filter(pk=oper_id).first()
            title = form.cleaned_data['title']
            worker_act = form.cleaned_data['worker_act']
            employ_position_act = form.cleaned_data['employ_position_act']
            amount = form.cleaned_data['amount']
            violation = Violation(certificate_of_violations=cer_vio_select ,reestr=reestr, title=title,
                                  employ_position_act=employ_position_act, worker=worker_act, amount=amount)
            violation.save()
            message = 'Сохранено'
    else:
        form = VolitionFormThe()
        message = Reestr.objects.filter(pk=oper_id).first()

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message.operation.name, 'name': name})


# Изменеие строки нарушения
def update_violation(request):
    name = 'Изменение нарушения'
    if request.method == 'POST':
        form = VolitionFormUpdate(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            volition = form.cleaned_data['volitions']
            old_violation = Violation.objects.filter(pk=volition.pk).first()
            old_violation.reestr = form.cleaned_data['reestr']
            old_violation.title = form.cleaned_data['title']
            old_violation.worker_act = form.cleaned_data['worker_act']
            old_violation.employ_position_act = form.cleaned_data['employ_position_act']
            old_violation.amount = form.cleaned_data['amount']
            old_violation.save()
            message = 'Нарушение изменено'
    else:
        form = VolitionFormUpdate()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html', {'form': form, 'message': message, 'name': name})


# class Violation(models.Model):
#     certificate_of_violations = models.ForeignKey(Certificate_of_violations, on_delete=models.PROTECT)
#     reestr = models.ForeignKey(Reestr, on_delete=models.PROTECT)
#     title = models.TextField(max_length=256)
#     employ_position_act = models.ForeignKey(Employ_position_act, on_delete=models.PROTECT)
#     worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
#     amount = models.FloatField(max_length=256)
#     register = models.BooleanField(default=False)

def reg_violation_jurnal(request):
    name = 'Регистрация  нарушения в жупнал'
    if request.method == 'POST':
        form = RegViolationForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            date = form.cleaned_data['date']
            vio = form.cleaned_data['violations']
            vio_select = Violation.objects.filter(pk=vio.pk).first()
            measures = form.cleaned_data['measures']
            content = form.cleaned_data['content']
            journal = Journal(violation=vio_select, date=date, content=content, measures=measures)
            journal.save()
            vio_select.register = True
            vio_select.save()
            message = 'Сохранено'
    else:
        form = RegViolationForm()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})

def update_reg_violation_jurnal(request):
    name = 'изменение  нарушения в журнале'
    if request.method == 'POST':
        form = UpdateRegViolationForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            vio = form.cleaned_data['violations']
            date = form.cleaned_data['date']
            vio_select = Violation.objects.filter(pk=vio.pk).first()
            measures = form.cleaned_data['measures']
            content = form.cleaned_data['content']
            journal = Journal(violation=vio_select, date=date, content=content, measures=measures)
            journal.save()
            message = 'Сохранено'
    else:
        form = UpdateRegViolationForm()
        message = 'Заполните форму'

    return render(request, 'fk_app/add_object.html',
                  {'form': form, 'message': message, 'name': name})

def get_certif_all(request):
    violations = Violation.objects.all()
    dict_certif = {}
    for violation in violations:
        dict_certif.setdefault(violation.certificate_of_violations, [violation]).append(violation)

    # print(dict_certif)
    context = {
        "certifs": dict_certif
    }
    return render(request, "fk_app/certif.html", context)

def get_sertif(request):
    name = 'Выберите справку'
    if request.method == 'POST':
        form = VolitionGetForm(request.POST, request.FILES)
        # message = 'Ошибка в данных'
        if form.is_valid():
            cer_vio = form.cleaned_data['certificate_of_violations']
            cer_vio_select = Certificate_of_violations.objects.filter(pk=cer_vio.pk).first()
            name = cer_vio_select
            violations_2 = Violation.objects.filter(certificate_of_violations__pk=cer_vio.pk)
            print(cer_vio_select)
            message = 'Справка'
    else:
        form = VolitionGetForm()
        # message = 'Заполните форму'
        violations_2 = None

    return render(request, 'fk_app/certif_one.html',
                {'form': form, 'name': name, 'volits':violations_2})
                # {'form': form, 'message': message, 'name': name, 'volits':violations_2})


def get_journal(request):
    journal = Journal.objects.all()
    print(journal)
    context = {
        "journals": journal
    }
    return render(request, "fk_app/journal.html", context)

#
# class Journal(models.Model):
#     date = models.DateField(auto_now_add=True)
#     violation = models.ForeignKey(Violation, on_delete=models.PROTECT)
#     measures = models.TextField(max_length=256)
#
#     def __str__(self):
#         return f'date: {self.date}, volation{self.violation} measurse{self.measures}'

# class Certificate_of_violations(models.Model):
#     date = models.DateField(auto_now_add=True)
#     worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
#
#






# class SertisForm(forms.Form):
#     worker = forms.ModelChoiceField(label=' Сотрундик - составитель', queryset=Worker.objects.all(), widget=forms.Textarea(attrs={'class': 'form-control',
#                                                          'placeholder': 'должность сотрудника кто подписывает справку'}))
#
#     reestr = forms.ModelChoiceField(label='Операция', queryset=Reestr.objects.all(),
#                                     widget=forms.Textarea(attrs={'class': 'form-control',
#                                                                  'placeholder': ' Операция с нарушением'}))
#     title = forms.CharField(max_length=50,
#                            widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'Введите имя пользователя'}))
#
#     employ_position_act = forms.ModelChoiceField(label='сотрудник', queryset=Employ_position_act.objects.all(),
#                                     widget=forms.Textarea(attrs={'class': 'form-control',
#                                                                  'placeholder': ' Сутрудник нарушитель'}))
#
#     worker_act = forms.ModelChoiceField(label=' Сотрундик -  нарушитель', queryset=Worker.objects.all(),
#                                     widget=forms.Textarea(attrs={'class': 'form-control',
#                                                                  'placeholder': 'должность сотрудника в отношении кого справка'}))
#
#     amount = forms.FloatField(label='Сумма', widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'Сумма нарушения'}))




#
# class Certificate_of_violations(models.Model):
#     date = models.DateField(auto_now_add=True)
#     worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
#
#
# class Violation(models.Model):
#     certificate_of_violations = models.ForeignKey(Certificate_of_violations, on_delete=models.PROTECT)
#     reestr = models.ForeignKey(Reestr, on_delete=models.PROTECT)
#     title = models.TextField(max_length=256)
#     employ_position_contr = models.ForeignKey(Employ_position_contr, on_delete=models.PROTECT)
#     worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
#     amount = models.FloatField(max_length=256)


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