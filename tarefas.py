'''importar o Celery e instanciá-lo'''
from celery import Celery
from random import randint 


app = Celery(broker='redis://127.0.0.1:6379/0')   #instanciar a variável app
##nosso broker é um bd redis, que está rodando localmente, porta 6379, 0 n do banco
##conferindo em qual porta está rodando, comando: redis-cli

@app.task
def exibir():
    #raise Exception('Erro detectado!')
    #return n1 / n2
    x = randint(1, 10)
    if x > 5:
        return 'Ok'
    else:
        raise Exception('Erro!')