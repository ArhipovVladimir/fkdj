import csv
from django.core.management.base import BaseCommand
from fk_app.models import Process, Operation, Violation, Certificate_of_violations


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('cer_vio', type=str, help='file name')

    def handle(self, *args, **kwargs):
        cer_vio = kwargs.get('cer_vio')
        cer_vio_select = Certificate_of_violations.objects.filter(pk=cer_vio).first()
        violations = Violation.objects.filter(pk=cer_vio_select.pk).first()
        print(cer_vio_select)
        print(violations)