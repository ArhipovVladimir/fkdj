from django import forms
import datetime
from .models import Process, Worker, Reestr, Employ_position_act, Certificate_of_violations, Violation


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
                                                              'type': 'date'})
                           )

    worker = forms.ModelChoiceField(label=' Сотрундик - составитель', queryset=Worker.objects.all(),
                                    # widget=forms.Textarea(attrs={'class': 'form-control',
                                    #                      'placeholder': 'должность сотрудника кто составляет справку'})
                                    )
class VolitionForm(forms.Form):
    certificate_of_violations = forms.ModelChoiceField(label='Справка', queryset=Certificate_of_violations.objects.all())
    reestr = forms.ModelChoiceField(label='Операция', queryset=Reestr.objects.all(),
                                    # widget=forms.Textarea(attrs={'class': 'form-control',
                                    #                              'placeholder': ' Операция с нарушением'})
                                    )
    title = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'содержание нарушения'}))


    # title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control',
    #                                                      'placeholder': 'содержание нарушения'}))


    worker_act = forms.ModelChoiceField(label=' Сотрудник -  нарушитель', queryset=Worker.objects.all()
                                    # ,widget=forms.Textarea(attrs={'class': 'form-control',
                                    #                              'placeholder': 'должность сотрудника в отношении кого справка'})
                                        )

    employ_position_act = forms.ModelChoiceField(label='', queryset=Employ_position_act.objects.all(),
                                    # widget=forms.Textarea(attrs={'class': 'form-control',
                                    #                              'placeholder': ' Сутрудник нарушитель'})
                                                 )

    amount = forms.FloatField(label='Сумма', widget=forms.NumberInput(attrs={'placeholder': 'Сумма нарушения'}))


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


class RegViolationForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today,
                           widget=forms.DateInput(attrs={'class': 'form-control',
                                                         'type': 'date'}))
    violations = forms.ModelChoiceField(label='нарушение', queryset=Violation.objects.filter(register=False))
    measures = forms.CharField(label='принятые меры', widget=forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'принятые меры'}))


# class Journal(models.Model):
#     date = models.DateField(auto_now_add=True)
#     violation = models.ForeignKey(Violation, on_delete=models.PROTECT)
#     measures = models.TextField(max_length=256)
#
#     def __str__(self):
#         return f'date: {self.date}, volation{self.violation} measurse{self.measures}'



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







