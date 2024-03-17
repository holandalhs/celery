### Projeto Celery

## Analogia do Projeto ao Dia a Dia de um Desenvolvedor Back-end

## Análise dos Arquivos
- **tarefas.py:**
  - Define a função _exibir_ decorada com _@app.task_ do Celery, transformando-a em uma tarefa assíncrona que pode ser executada em segundo plano.
  - A função _exibir_ gera um número aleatório e, se for maior que 6, retorna o número. Caso contrário, ela tenta novamente (retry) com um atraso exponencial baseado no número de tentativas.

- **app.py:**
  - Importa a função _exibir_ do arquivo _tarefas.py_ e a chama assincronamente usando _exibir.delay()_.

- **celery.pyi:**
  - Define uma classe _Celery_ com métodos para inicializar o broker e definir tarefas assíncronas. Fornece anotações de tipo para os argumentos e retornos dos métodos.
    _Acessando o flower da apliação:_
![imagemflower](https://github.com/holandalhs/celery/assets/153955937/a213228c-ceee-44df-9f44-5ef021da92f0)


## Comparativo
A utilidade do uso da ferramenta, por exemplo, para um desenvolvedor responsável por uma aplicação web que precisa processar tarefas demoradas em segundo plano, como enviar e-mails em massa para os usuários. Usando o Celery, você pode criar tarefas assíncronas para lidar com essas operações sem bloquear a execução da aplicação principal.

Com um simples código em Celery, podemos notar diversas situações do dia a dia que podem ser impactadas de maneira positiva, como:

:arrow_right:**Processamento em segundo plano:**
  Para executar operações pesadas sem impactar a resposta da aplicação.
  
:arrow_right:**Tratamento de erros assíncronos:**
  Como no exemplo da função _exibir_, onde há uma tentativa de retry em caso de erro.
  
:arrow_right:**Agendamento de tarefas:**
  Definindo horários para executar determinadas operações de forma automática.
  
:arrow_right:**Escalabilidade:**
  Permitindo distribuir tarefas em vários servidores para lidar com um grande volume de processamento.

Em resumo, o uso do Celery e tarefas assíncronas pode melhorar a eficiência, escalabilidade e confiabilidade de uma aplicação backend, liberando recursos para lidar com mais requisições e processos de forma mais eficiente.
