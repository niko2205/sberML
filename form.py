# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:00:41 2021

@author: risev
"""

import cgi
from CreditPaymentsModule import CreditPayments
from xmlrpc import client
from lxml import etree

form = cgi.FieldStorage()
deal_id = form.getfirst("deal_id", "none")
pay_date = form.getfirst("pay_date", "none")

pObject = CreditPayments()
calc_res = pObject.getRestOfCredit(deal_id, pay_date)
summ = pObject.getSummOfCredit(deal_id)

inn_client = client.ServerProxy("http://localhost:9000")
inn = inn_client.get_inn(deal_id)
fio = inn_client.get_fio(inn)

risk_client = client.ServerProxy("http://localhost:9090")
history = risk_client.get_history(inn)

req = pay_date.split(".")
req = req[0] + "/01/" + req[1]

tree = etree.parse('http://www.cbr.ru/scripts/XML_daily.asp?date_req={}'.format(req))
root = tree.getroot()

for valute in root.getchildren():
    for descr in valute.getchildren():
        if descr.text == "USD":
          usd = valute.getchildren()[4].text
          
usd = usd.replace(',', '.')
summ = summ / float(usd)
calc_res = calc_res / float(usd)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <!-- <meta charset="utf-8" -->
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h1>Остаток кредита по договору №{} на дату {} составляет: </h1>".format(deal_id, pay_date))
print("<h2>{} тыс. дол.</h2>".format(calc_res))
print("<h2>Сумма кредита: {} тыс. долл.</h2>".format(summ))
print("<h2>Курс доллара ЦБ РФ: {} руб.</h2>".format(usd))
print("ИНН: <b>{}</b>".format(inn))
print("ФИО: <b>{}</b>".format(fio))
print("Кредитная история: <b>{}</b>".format(history))
print("""<body>
        </html>""")