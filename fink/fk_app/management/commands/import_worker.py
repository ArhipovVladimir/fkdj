import csv
from django.core.management.base import BaseCommand
from fk_app.models import Employ_position, Worker


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('file_csv', type=str, help='file name')

    def handle(self, *args, **kwargs):
        file_csv = kwargs.get('file_csv')
        with(open(file_csv, 'r', newline='') as f_cvs_red):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            list_empl = []
            for i, row in enumerate(csv_file):
                if i != 0:
                    list_empl.append(Employ_position(name=row[0]))
            # print(list_empl)
            Employ_position.objects.bulk_create(list_empl)

        with(open(file_csv, 'r', newline='') as f_cvs_red):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            list_worker = []
            for i, row in enumerate(csv_file):
                # print(row)
                if i != 0:
                    # print(row[1])
                    list_worker.append(Worker(name=row[1],
                                               employ_position=Employ_position.objects.filter(name=row[0]).first()))
            # print(list_worker)
            Worker.objects.bulk_create(list_worker)




            # list_reestr = []
            # for i, row in enumerate(csv_file):
            #     if i != 0:
            #         list_reestr.append(Reestr(operation=Operation.objects.filter(code_oper=row[2]).first(),
            #                                   employ_contr=Employ_position_contr.objects.filter(name=row[4]).first(),
            #                                   employ_actint=Employ_position_act.objects.filter(name=row[5]).first(),
            #                                   control_action=Control_action.objects.filter(name=row[6]).first(),
            #                                   method=Method.objects.filter(name=row[7]).first()
            #                                   ))
            # Reestr.objects.bulk_create(list_reestr)