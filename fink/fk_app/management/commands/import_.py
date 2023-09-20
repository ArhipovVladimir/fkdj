import csv
from django.core.management.base import BaseCommand
from fk_app.models import Employ_position_contr, Employ_position_act, Control_action, Method, Process, Operation, Reestr


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('file_csv', type=str, help='file name')

    def handle(self, *args, **kwargs):
        file_csv = kwargs.get('file_csv')
        with(open(file_csv, 'r', newline='') as f_cvs_red,):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            set_empl_contr = set()
            set_empl_act = set()
            set_act = set()
            set_method = set()
            for i, row in enumerate(csv_file):
                if i != 0:
                    set_empl_contr.add(row[4])
                    set_empl_act.add(row[5])
                    set_act.add(row[6])
                    set_method.add(row[7])

            list_item = []
            for name in set_empl_contr:
                list_item.append(Employ_position_contr(name=name))

            # print(list_item)
            Employ_position_contr.objects.bulk_create(list_item)

            list_item = []
            for name in set_empl_act:
                list_item.append(Employ_position_act(name=name))

            # print(list_item)
            Employ_position_act.objects.bulk_create(list_item)

            list_item = []
            for name in set_act:
                list_item.append(Control_action(name=name))

            # print(list_item)
            Control_action.objects.bulk_create(list_item)

            list_item = []
            for name in set_method:
                list_item.append(Method(name=name))

            # print(list_item)
            Method.objects.bulk_create(list_item)

        with(open(file_csv, 'r', newline='') as f_cvs_red, ):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            set_proc = {}
            for i, row in enumerate(csv_file):
                if i != 0:
                    set_proc[row[0]] = row[1]
            print(set_proc)
            list_item = []
            for code, name in set_proc.items():
                list_item.append(Process(code_proc=code, name=name))
            print(list_item)
            Process.objects.bulk_create(list_item)

        with(open(file_csv, 'r', newline='') as f_cvs_red, ):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
            list_oper = []
            for i, row in enumerate(csv_file):
                if i != 0:
                    list_oper.append(Operation(code_oper=row[2], name=row[3],
                                               process=Process.objects.filter(code_proc=row[0]).first()))
            print(list_oper)
            Operation.objects.bulk_create(list_oper)
        with(open(file_csv, 'r', newline='') as f_cvs_red, ):
            csv_file = csv.reader(f_cvs_red, dialect='excel-tab')

            list_reestr = []
            for i, row in enumerate(csv_file):
                if i != 0:

                    list_reestr.append(Reestr(operation=Operation.objects.filter(code_oper=row[2]).first(),
                                              employ_contr=Employ_position_contr.objects.filter(name=row[4]).first(),
                                              employ_actint=Employ_position_act.objects.filter(name=row[5]).first(),
                                              control_action=Control_action.objects.filter(name=row[6]).first(),
                                              method=Method.objects.filter(name=row[7]).first()
                                              ))
            print(list_reestr)
            Reestr.objects.bulk_create(list_reestr)
