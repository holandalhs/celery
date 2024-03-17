### Projeto celery
## Analogia do projeto ao dia a dia de um dev back-end.

## Análise dos arquivos
 > em tarefas.py; define a função exibir decorada com @app.task do Celery, que a transforma em uma tarefa assíncrona que pode ser executada em segundo plano.
 Já a função exibir gera um número aleatório e, se for maior que 6, retorna o número. Caso contrário, ela tenta novamente (retry) com um atraso exponencial baseado no número de tentativas.
 > em tarefas.py; importa a função exibir do arquivo tarefas.py e a chama assincronamente usando exibir.delay().
 > em celery.pyi; define uma classe Celery com métodos para inicializar o broker e definir tarefas assíncronas. Ele fornece anotações de tipo para os argumentos e retornos dos métodos.

 ## Comparativo 
 > A utilidade do uso da ferramenta, por exemplo, para um desenvolvedor responsável por uma aplicação web que precisa processar tarefas demoradas em segundo plano, como enviar e-mails em massa para os usuários. Usando o Celery, você pode criar tarefas assíncronas para lidar com essas operações sem bloquear a execução da aplicação principal.

Com um simples código em Celery podemos notar diversas situações do dia a dia que podem ser impactadas de maneira positiva, como:

    * Processamento em segundo plano: Para executar operações pesadas sem impactar a resposta da aplicação.
    * Tratamento de erros assíncronos: Como no exemplo da função exibir, onde há uma tentativa de retry em caso de erro.
    * Agendamento de tarefas: Definindo horários para executar determinadas operações de forma automática.
    * Escalabilidade: Permitindo distribuir tarefas em vários servidores para lidar com um grande volume de processamento.

Em resumo, o uso do Celery e tarefas assíncronas pode melhorar a eficiência, escalabilidade e confiabilidade de uma aplicação backend, liberando recursos para lidar com mais requisições e processos de forma mais eficiente.