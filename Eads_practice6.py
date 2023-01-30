Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> purchase_amount = input('Please enter the amount of the purhase: ')
>>> payment_installments = input('Please enter the desired number of payment installments: ')
>>> purchase_amount_number = float(purchase_amount)
>>> payment_installments_number = float(payment_installments)
>>> total_amount = (purchase_amount_number * 0.05) + purchase_amount_number
>>> installment_amount = total_amount / payment_installments_number
>>> print('The total purchase amount is: ', total_amount)
>>> print('Each installment will be:', installment_amount)
