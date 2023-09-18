import csv


def create_csv_json(file_csv):
    # with(open(file_csv, 'r', encoding='utf-8', newline='') as f_cvs_red,
    with(open(file_csv, 'r', newline='') as f_cvs_red,

    ):
        csv_file = csv.reader(f_cvs_red, dialect='excel-tab')
        set_oper = set()
        for i, row in enumerate(csv_file):
            if i != 0:
                set_oper.add(row[2])
        print(set_oper)
        # Operation.objects.bulk_create(set_oper)

if __name__ == '__main__':
    create_csv_json('_reestr.csv')