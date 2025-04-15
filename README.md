
# ☎️ Atividade - URA Bancária em Python

Este projeto consiste em uma **Unidade de Resposta Audível (URA)** bancária simulada, desenvolvida em Python, como parte da disciplina de Autômatos. A URA permite aos usuários realizar operações bancárias básicas como consultar saldo, extrato, realizar transferências e pagamentos, além de simular a transferência para um atendente.

---

## 🛠️ Tecnologias Utilizadas

<p align="center"> 
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"/>
<img width="12" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" alt="Visual Studio Code" width="50" height="40"/> 

---

## 🎯 Funcionalidades

- 🔐 **Autenticação:** Usuários inserem o número da conta para acesso.
- 🧭 **Menu Principal:** Consulta de saldo, extrato, transferência, pagamento e atendimento.
- 💰 **Saldo e Extrato:** Exibe informações financeiras da conta.
- 💸 **Transferência e Pagamento:** Valida e executa operações financeiras.
- 📞 **Atendimento:** Simula a transferência para um atendente.
- 🔊 **Geração de Áudio:** Cria arquivos de áudio com as mensagens da URA, se não existirem.

---

## 📦 Dependências

- `playsound`: Para reprodução de arquivos de áudio.
- `gtts`: Para conversão de texto em fala (Text-to-Speech).

---

## 🚀 Como Utilizar o Repositório

1. 📥 Clone o repositório:
```bash
    https://github.com/RaphaelLins6/URA-Automato
```
2. 💻 Acesse a pasta do projeto:
```bash
    cd URA-Automato
```
3. 📦 Instale as dependências:
```bash
  pip install -r requirements.txt
```
4. ▶️ Execute o script:
```bash
  python ura.py
```
5. 🎧 Interaja com a URA:
- Siga as instruções no console.
- Utilize o teclado para navegar pelas opções e realizar as operações.

---

### 🧠 Estrutura do Código

- Classe `URA`:
Gerencia o estado da URA e os dados da conta.
Implementa os métodos para cada estado e funcionalidade da URA.
Utiliza a biblioteca playsound para reproduzir áudios e gtts para gerar novos áudios.

- Função `main()`:
Inicializa a URA e lida com as entradas do usuário.
Utiliza um loop para manter a interação com o usuário.

---

### 🔄 Conceitos de Autômatos Aplicados

Estados: A URA utiliza estados para controlar o fluxo de interação com o usuário (início, autenticação, menu, etc.).

Transições: As transições entre os estados são determinadas pelas entradas do usuário e pelas regras de negócio da URA.
Validação de Entrada: A URA valida as entradas do usuário (número da conta, valores de transferência e pagamento) para garantir a integridade das operações.

---

## 👨‍💻 Autor

- [@RaphaelLins6](https://www.github.com/RaphaelLins6) - Raphael Lins (RGM:27797660)

---

## 📜 Licença

Este projeto é livre para uso e modificação. Contribuições são bem-vindas! 😊

---
