from bs4 import BeautifulSoup
from flask import Flask, request
import os
import traceback
import requests
import json
import urllib.request


def bemVindo(sender):
    retorno = 'Olá tudo bem,em que posso lhe ajuda ? :)'#Mensagem de retorno ao usuario
    payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} #Envio para o Usuario
    return(requests.post(linkGrafh + token, json=payload))