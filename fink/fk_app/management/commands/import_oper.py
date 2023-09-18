import csv
from django.core.management.base import BaseCommand
from fk_app.models import Process, Operation


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('file_csv', type=str, help='file name')

    def handle(self, *args, **kwargs):
        file_csv = kwargs.get('file_csv')
        # self.stdout.write(file_csv)
        with(open(file_csv, 'r', newline='') as f_cvs_red,):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            list_oper = []
            for i, row in enumerate(csv_file):
                if i != 0:
                   list_oper.append(Operation(code_oper=row[2], name=row[3],
                                               process=Process.objects.filter(code_proc=row[0]).first()))
            Operation.objects.bulk_create(list_oper)
