
# Atividade

* Este projeto consiste em uma Unidade de Resposta Audível (URA) bancária simulada, desenvolvida em Python, como parte da disciplina de Autômatos. A URA permite aos usuários realizar operações bancárias básicas, como consultar saldo, extrato, realizar transferências e pagamentos, além de simular a transferência para um atendente.

### Funcionalidades:

- Autenticação: Permite que usuários insiram o número da conta para autenticação.
- Menu Principal: Oferece opções para consulta de saldo, extrato, transferência, pagamento e atendimento.
- Saldo e Extrato: Exibe o saldo e o extrato da conta autenticada.
- Transferência e Pagamento: Permite realizar transferências e pagamentos, validando o saldo disponível.
- Atendimento: Simula a transferência para um atendente.
- Geração de Áudio: Gera arquivos de áudio para cada interação da URA, caso não existam.

### Dependências

- `playsound`: Para reprodução de arquivos de áudio.
- `gtts`: Para conversão de texto em fala (Text-to-Speech).

### Como Executar

- Instale as dependências:
pip install playsound gtts

- Execute o script:
python seu_script.py

Interaja com a URA: Siga as instruções exibidas no console e utilize o teclado para inserir os dados solicitados.

### Estrutura do Código

- URA Class:
Gerencia o estado da URA e os dados da conta.
Implementa os métodos para cada estado e funcionalidade da URA.
Utiliza a biblioteca playsound para reproduzir áudios e gtts para gerar novos áudios.

- main Function:
Inicializa a URA e lida com as entradas do usuário.
Utiliza um loop para manter a interação com o usuário.

### Conceitos de Autômatos Aplicados

Estados: A URA utiliza estados para controlar o fluxo de interação com o usuário (início, autenticação, menu, etc.).

Transições: As transições entre os estados são determinadas pelas entradas do usuário e pelas regras de negócio da URA.
Validação de Entrada: A URA valida as entradas do usuário (número da conta, valores de transferência e pagamento) para garantir a integridade das operações.
## Autores

- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)

