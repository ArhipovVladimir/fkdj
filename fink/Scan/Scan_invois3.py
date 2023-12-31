
#Идентификация макетов счетов-фактур для применения OCR
#Шаг 1: Импортируйте необходимые библиотеки

#Сначала импортируем необходимые библиотеки: OpenCV (cv2) для обработки
#изображений и pytesseract для OCR. Мы также импортируем класс Output из pytesseract,
#чтобы указать выходной формат результатов OCR.

import cv2
import pytesseract
from pytesseract import Output

#Шаг 2. Прочтите образец изображения счета-фактуры

#Затем мы читаем образец изображения счета-фактуры sample-invoice.jpg,
#используя cv2.imread() и сохраните его в переменной img.

img = cv2.imread('sample-invoice.jpg')

#Шаг 3. Выполните распознавание текста на изображении и получите результаты в формате словаря.

#Далее мы используем pytesseract.image_to_data() выполнить распознавание изображения и получить
#словарь информации об обнаруженном тексте.
#output_type=Output.DICT аргумент указывает, что мы хотим, чтобы результаты были в формате словаря.

#Затем мы печатаем ключи результирующего словаря, используя функцию keys(), чтобы
#увидеть доступную информацию, которую мы можем извлечь из результатов OCR.

d = pytesseract.image_to_data(img, output_type=Output.DICT)
# Print the keys of the resulting dictionary to see the available information
print(d.keys())


#Шаг 4. Визуализируйте обнаруженный текст, нарисовав ограничивающие рамки

#Чтобы визуализировать обнаруженный текст, мы можем построить ограничивающие рамки
#каждого обнаруженного слова, используя информацию в словаре. Сначала мы получаем количество
#обнаруженных текстовых блоков, используя len() функцию, а затем перебрать каждый блок.
#Для каждого блока мы проверяем, превышает ли показатель достоверности обнаруженного текста
#60 (т. е. обнаруженный текст с большей вероятностью будет правильным), и если это так,
#мы извлекаем информацию о ограничивающей рамке и рисуем прямоугольник вокруг текста, используя
#cv2.rectangle(). Затем мы отображаем полученное изображение, используя cv2.imshow() и подождите,
#пока пользователь нажмет клавишу, прежде чем закрыть окно.

n_boxes = len(d['text'])
for i in range(n_boxes):
	if float(d['conf'][i]) > 60:
	# Check if confidence score is greater than 60
		(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
		img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
	cv2.imshow('img', img)
cv2.waitKey(0)

#---------------------------