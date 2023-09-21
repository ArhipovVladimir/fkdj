from django import forms
import datetime
from .models import Process, Worker, Reestr, Employ_position_act, Certificate_of_violations


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        """Плохой пример. Подмена параметра min_length."""

        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ProcessForm(forms.Form):
    name = forms.CharField(max_length=120, label='Наименование процесса',
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите  наименование процесса'}))


class OperatinForm(forms.Form):
    name = forms.CharField(max_length=120, label='Наименование операции',
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите  наименование операции'}))
    process = forms.ModelChoiceField(label='процессы', queryset=Process.objects.all())


class SertifForn(forms.Form):
    date = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))

    worker = forms.ModelChoiceField(label=' Сотрундик - составитель', queryset=Worker.objects.all(),
                                    # widget=forms.Textarea(attrs={'class': 'form-control',
                                    #                      'placeholder': 'должность сотрудника кто составляет справку'})
                                    )


class VolitionForm(forms.Form):
    certificate_of_violations = forms.ModelChoiceField(label='процессы', queryset=Certificate_of_violations.objects.all())
    reestr = forms.ModelChoiceField(label='Операция', queryset=Reestr.objects.all()          )


    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))

    employ_position_act = forms.ModelChoiceField(label='сотрудник', queryset=Employ_position_act.objects.all())

    worker_act = forms.ModelChoiceField(label=' Сотрундик -  нарушитель', queryset=Worker.objects.all())

    amount = forms.FloatField(label='Сумма', widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Сумма нарушения'}))


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


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
     image = forms.ImageField()


# из домашнего задания

class ProductForm(forms.Form):
    # products = forms.ModelChoiceField(label='Продукты', queryset=Product.objects.all())
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите назв продукта'}))
    description = forms.CharField(max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите описание продукта'}))

    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    image = forms.ImageField()


# class ProductFormUpdate(ProductForm):
#     products = forms.ModelChoiceField(label='Продукты', queryset=Product.objects.all())






