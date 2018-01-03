from bs4 import BeautifulSoup
from flask import Flask, request
import os
import traceback
import requests
import json
import urllib.request
import entradaUser 

token = "EAAL34wXGjT4BAAMceRhqZCNB4ZCld5B9JC9Ja59lsAlWCGmLqLbhfZAuUtXZA8Cu5WWPUM0tz3hZA5IqDxPy3uM6Cu1Bh7aI0JAkZCuECunMW0ZB0yfehACeYZCemnWOArYyVndOoEsZBqf4xFCxYsCZAQMH17L06FlJcOvfw6ZBXcHfwZDZD"
app = Flask(__name__)

linkGrafh ='https://graph.facebook.com/v2.6/me/messages/?access_token='

#Entradas de recebimentos de usuarios.

entrada = ['olá','oi','bom dia','ola','i aew','iae','blz']
sentimentos = ['bom?','tudo bom?','esta bem?','como vai voce','como vai','voce esta legal','bem?']
megasena = ['resultado da mega','resultado da mega sena','resultado da megasena','numeros da megasena','megasena','sena']
trabalho = ['quando começou a trabalhar?','trabalha desde quando','voce trabalha ?','trabalha?']
tchau = ['ate mais','tchau','xau']
vindo = ['bem']

@app.route('/', methods=['GET', 'POST'])



def webhook():
    if request.method == 'POST':

        try:
            data = json.loads(request.data)
            text = data['entry'][0]['messaging'][0]['message']['text'] # mensagem recebida
            msg = str(text.lower()) #mensagem json para string
            sender = data['entry'][0]['messaging'][0]['sender']['id'] # id do mensageiro
            

            
                        
            
            
            print(id)
            if msg in entrada:
                
                retorno = 'Olá tudo bem,em que posso lhe ajuda ? :)'#Mensagem de retorno ao usuario
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} #Envio para o Usuario
                
                r = requests.post(linkGrafh + token, json=payload)
            elif msg in megasena:
                source = requests.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/').text

                soup = BeautifulSoup(source,'lxml')
                #class numbers mega-sena
                numeros = soup.find('ul',class_='numbers mega-sena')

                num = numeros.text
                #tratamento de string
                for i in range(0,12,2):
                    numeros = soup.find('ul',class_='numbers mega-sena')
                    num += '-'+numeros.text[i:i+2]

                result = num[14:31]
                concurso = soup.find('div',class_='title-bar clearfix')
                resConc = concurso.h2.span.text
                retorno = ('O resultado do ultimo \n'+resConc+' \nfoi:'+result+' \n\nSaiba mais aqui. \nhttp://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/\n')
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
                r = requests.post(linkGrafh + token, json=payload) 
            elif msg in vindo:
                p = entradaUser()
                p.bemVindo(sender)

            elif msg in trabalho:
                retorno = 'Eu trabalho desde o dia 12 de dezembro de 2017'
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
                r = requests.post(linkGrafh + token, json=payload) 

            elif msg in sentimentos:
                retorno = 'Estou muito Bem :) Obrigada.'
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
                r = requests.post(linkGrafh + token, json=payload)

            elif msg in tchau:
                retorno = 'Até mais :), estou a sua disposição'
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
                r = requests.post(linkGrafh + token, json=payload)
                           
            
            elif msg in entrada or trabalho or sentimentos or tchau:
                retorno='Isso nao faz parte da minha função'
                payload = {'recipient': {'id': sender}, 'message': {'text': retorno}} 
                r = requests.post(linkGrafh + token, json=payload)
             

        except Exception as e:
           print(traceback.format_exc())

    elif request.method == 'GET': # Para a verificação inicial
        if request.args.get('hub.verify_token') == 'testaqui':
            return request.args.get('hub.challenge')
        return render_template('home.html')
    return "Nada retornado"

def location_quick_reply(sender):
    return {
        "recipient": {
            "id": sender
        },
        "message": {
            "text": "Compartilhe sua localização:",
            
            
        }
    }
def boas(sender):
    return {
        "recipient": {
            "id": sender
        },
        "message": {
            "text": "Olá tudo Bem",
            
        }
    }
def botoes(sender):
    return{
        "recipient": {
            "id":sender
        },
        "message":{
            "attachment":{
            "type":"template",
            "payload":{
                "template_type":"button",
                "text":"What do you want to do next?",
                "buttons":[
                {
                    "type":"web_url",
                    "url":"https://www.messenger.com",
                    "title":"Visit Messenger"
                },
                {
                    ...
                },
                {...}
                ]
            }
            }
        }
    }

if __name__ == '__main__':
    app.run(debug=True)

#