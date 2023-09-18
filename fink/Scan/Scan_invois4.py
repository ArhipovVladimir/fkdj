#Распознавание именованных сущностей (NER) — это метод обработки естественного языка,
#который можно использовать для извлечения структурированной информации из неструктурированного текста.
#контексте извлечения счетов NER можно использовать для идентификации ключевых объектов,
#таких как номера счетов, даты и суммы.

import spacy
# Load the English pre-trained model with NER
nlp = spacy.load('en_core_web_sm')

with open('sample-invoice.pdf', 'r') as f:
	text = f.read() # Apply the NER model to the invoice text
doc = nlp(text)

# Шаг 3. Извлеките номер счета, дату и общую сумму к оплате.

#Затем мы перебираем обнаруженные объекты в тексте счета, используя цикл
#for. Мы используем label_ attribute каждого объекта, чтобы проверить, соответствует ли
#он номеру счета-фактуры, дате или общей сумме к оплате. Мы используем сопоставление строк и
#перевод в нижний регистр, чтобы идентифицировать эти объекты на основе их контекстуальных подсказок.

invoice_number = None
invoice_date = None
total_amount_due = None


for ent in doc.ents:
    if ent.label_ == 'INVOICE_NUMBER':
        invoice_number = ent.text.strip()
    elif ent.label_ == 'DATE':
        if ent.text.strip().lower().startswith('invoice'):
            invoice_date = ent.text.strip()
    elif ent.label_ == 'MONEY':
        if 'total' in ent.text.strip().lower():
            total_amount_due = ent.text.strip()

print('Invoice Number:', invoice_number)
print('Invoice Date:', invoice_date)
print('Total Amount Due:', total_amount_due)



