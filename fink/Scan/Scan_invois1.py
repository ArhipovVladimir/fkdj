# Шаг 1: Импортируйте библиотеки

import pdftotext
import re

# Шаг 2. Прочтите PDF-файл
with open('sample-invoice.pdf', 'rb') as f:
	pdf = pdftotext.PDF(f)
	text = 'nn'.join(pdf)

# Шаг 3. Используйте регулярные выражения для сопоставления текста в счетах-фактурах.

#Мы используем регулярные выражения для извлечения номера счета, общей суммы к оплате,
#даты счета и срока оплаты из текста счета. Мы компилируем регулярные выражения, используя
#re.compile() функция и используйте search() Функция для поиска первого вхождения шаблона в тексте.
#Мы используем group() функция для извлечения соответствующего текста из шаблона, а strip()
#функция для удаления любых начальных или конечных пробелов из совпавшего текста.
#Если совпадение не найдено, мы устанавливаем соответствующее значение None.


invoice_number = re.search(r'Invoice Numbers*ns*n(.+?)s*n', text).group(1).strip()
total_amount_due = re.search(r'Total Dues*ns*n(.+?)s*n', text).group(1).strip() # Extract the invoice date
invoice_date_pattern = re.compile(r'Invoice Dates*ns*n(.+?)s*n')
invoice_date_match = invoice_date_pattern.search(text)

if invoice_date_match:
	invoice_date = invoice_date_match.group(1).strip()
else:
	 invoice_date = None # Extract the due date
due_date_pattern = re.compile(r'Due Dates*ns*n(.+?)s*n')
due_date_match = due_date_pattern.search(text)

if due_date_match:
	due_date = due_date_match.group(1).strip()
else:
	due_date = None

print('Invoice Number:', invoice_number)
print('Date:', date)
print('Total Amount Due:', total_amount_due)
print('Invoice Date:', invoice_date)
print('Due Date:', due_date)

#Результат

#Invoice Date: January 25, 2016
#Due Date: January 31, 2016
#Invoice Number: INV-3337
#Date: January 25, 2016
#Total Amount Due: $93.50

