import csv
from django.core.management.base import BaseCommand
from fk_app.models import Process


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('file_csv', type=str, help='file name')

    def handle(self, *args, **kwargs):
        file_csv = kwargs.get('file_csv')
        # self.stdout.write(file_csv)
        with(open(file_csv, 'r', newline='') as f_cvs_red,):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            set_oper = {}
            for i, row in enumerate(csv_file):
                if i != 0:
                    set_oper[row[0]] = row[1]
        list_item = []
        for code, name in set_oper.items():
            list_item.append(Process(code_proc=code, name=name))


        Process.objects.bulk_create(list_item)

