#!/usr/bin/env python

from telethon.sync import TelegramClient
from telethon import functions, types
import random

line = "___________"

name = ''
api_id = 1234567
api_hash = ''

def check(phone):
    if phone[0] == '+' and len(phone) >= 10:
        with TelegramClient(name, api_id, api_hash) as client:
            contacts = [types.InputPhoneContact(
                client_id=random.randrange(-2**63, 2**63),
                phone=phone,
                first_name='Name',
                last_name='(checker)')]
            result = str(client(functions.contacts.ImportContactsRequest(contacts)))
            if result.find('username=') != -1:
                username = client.get_entity(phone).username
                if username == None:
                    print(line+'\n'*2+"Номер найден, но у пользователя отсутствует username!"+'\n'+line+'\n')
                    print("User info: "+result+'\n'+line+'\n')
                else:
                    result = client(functions.contacts.DeleteContactsRequest(id=[username]))
                    print(line+'\n'*2+phone+" - номер найден! Пользователь известен как: @"+username+'\n'+line+'\n')
            else: print(line+'\n'*2+phone+" - номер не зарегестрирован в тг!"+'\n'+line+'\n')
    else: print(line+'\n'*2+phone+" - номер некорректен! Введите номер в международном формате!"+'\n'+line+'\n')

def singleMode(): 
    check(input("\nНомер для проверки: "))

def multiMode():
    for phone in open('phones.txt', 'r').read().split(): check(phone)
