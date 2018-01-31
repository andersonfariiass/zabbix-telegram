#!/usr/bin/python
#_*_coding: utf-8_*_

#Script para alerta via telegram no zabbix server.
#Fonte: https://raw.githubusercontent.com/janssenlima/scripts-zabbix/master/alertscripts/alerta_telegram.py

import telebot as tb
import sys

API_TOKEN='510104967:AAG8-x8MNSQhj12JSvTVVRn0XHM5wsDu4pE'
DESTINATARIO=sys.argv[1]
ASSUNTO=sys.argv[2]
MENSAGEM=sys.argv[3].replace('/n','\n')

alerta = tb.TeleBot(API_TOKEN)
alerta.send_message(DESTINATARIO, ASSUNTO + '\n' + MENSAGEM, disable_web_page_preview=True, parse_mode='HTML')
