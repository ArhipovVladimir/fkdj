#Извлечение таблиц из электронных счетов в формате PDF может быть простой задачей
#благодаря таким библиотекам, как Tabula и Camelot. В следующем коде показано,
#как использовать эти библиотеки для извлечения таблиц из счета в формате PDF.


from tabula import read_pdf
from tabulate import tabulate

file = "sample-invoice.pdf"
df = read_pdf(file ,pages="all")
print(tabulate(df[0]))
print(tabulate(df[1]))

# Результат

#- ------------ ----------------
#0 Order Number 12345
#1 Invoice Date January 25, 2016
#2 Due Date January 31, 2016
#3 Total Due $93.50
#- ------------ ---------------- - - ------------------------------- ------ ----- ------
#0 1 Web Design $85.00 0.00% $85.00 This is a sample description...
#- - ------------------------------- ------ ----- ------





