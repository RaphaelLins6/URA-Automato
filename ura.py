from playsound import playsound
from gtts import gTTS
import os

#integrates que fizeram o codigo: Raphael Lins e João Gabriel K Torres

class URA:
    def __init__(self):
        # Inicializa o estado da URA, dados da conta autenticada, saldo, extrato e contas válidas
        self.state = 'inicio'
        self.conta_autenticada = None
        self.saldo = 1000.00
        self.extrato = []
        self.contas_validas = ['12345', '67890']  # Exemplo de contas válidas
    
    def process_input(self, entrada):
        # Processa a entrada do usuário com base no estado atual da URA
        if self.state == 'inicio':
            return self.inicio()
        elif self.state == 'autenticacao':
            return self.autenticacao(entrada)
        elif self.state == 'menu_principal':
            return self.menu_principal(entrada)
        elif self.state == 'saldo_conta':
            return self.saldo_conta()
        elif self.state == 'extrato_conta':
            return self.extrato_conta()
        elif self.state == 'transferencia_dinheiro':
            return self.transferencia_dinheiro(entrada)
        elif self.state == 'pagamento_contas':
            return self.pagamento_contas(entrada)
        elif self.state == 'falar_atendente':
            return self.falar_atendente()
        else:
            return "Estado inválido."

    def inicio(self):
        # Estado inicial: solicita a autenticação do usuário
        self.state = 'autenticacao'
        playsound('bem_vindo.mp3')
        playsound('digite_numero_conta.mp3')
        return "Digite o número da sua conta para autenticação: "
    
    def autenticacao(self, entrada):
        # Autentica o usuário com base na entrada do número da conta
        try:
            if entrada in self.contas_validas:
                self.conta_autenticada = entrada
                self.state = 'menu_principal'
                tts = gTTS('hello')
                playsound('autenticacao_sucesso.mp3')
                playsound('menu_principal.mp3')
                return ("Autenticação bem-sucedida. Por favor, selecione uma das opções: \n"
                        "1. Saldo da conta \n"
                        "2. Extrato da conta \n"
                        "3. Transferência de dinheiro \n"
                        "4. Pagamento de contas \n"
                        "5. Falar com um atendente")
            else:
                # Se a conta não for válida, retorna a mensagem de erro
                playsound('opcao_invalida.mp3')
                return "Conta inválida. Por favor, tente novamente: "
        except Exception as err:
            print("Erro: ", err)

    def menu_principal(self, entrada):
        # Menu principal: processa a escolha do usuário
        if entrada == '1':
            self.state = 'saldo_conta'
            return self.saldo_conta()
        elif entrada == '2':
            self.state = 'extrato_conta'
            return self.extrato_conta()
        elif entrada == '3':
            self.state = 'transferencia_dinheiro'
            playsound('transferencia_digite_valor.mp3')
            return "Digite o valor a ser transferido: "
        elif entrada == '4':
            self.state = 'pagamento_contas'
            playsound('pagamento_digite_valor.mp3')
            return "Digite o valor a ser pago: "
        elif entrada == '5':
            self.state = 'falar_atendente'
            return self.falar_atendente()
        else:
            # Opção inválida: reproduz áudio e retorna ao menu principal
            playsound('opcao_invalida.mp3')
            return ("Opção inválida. Tente novamente. \n"
                    "1. Saldo da conta \n"
                    "2. Extrato da conta \n"
                    "3. Transferência de dinheiro \n"
                    "4. Pagamento de contas \n"
                    "5. Falar com um atendente")
    
    def saldo_conta(self):
        # Exibe o saldo da conta autenticada
        self.state = 'menu_principal'
        playsound('saldo_conta.mp3')
        playsound('menu_principal.mp3')
        return f"O saldo da conta {self.conta_autenticada} é R$ {self.saldo:.2f}. Voltando ao menu principal."
    
    def extrato_conta(self):
        # Exibe o extrato da conta autenticada
        self.state = 'menu_principal'
        extrato_str = "\n".join(self.extrato) if self.extrato else "Nenhuma transação realizada."
        playsound('extrato_conta.mp3')
        playsound('menu_principal.mp3')
        return f"Extrato da conta {self.conta_autenticada}:\n{extrato_str}\nVoltando ao menu principal."
    
    def transferencia_dinheiro(self, entrada):
        # Realiza a transferência de dinheiro
        try:
            valor = float(entrada)
            if valor <= 0:
                raise ValueError("O valor deve ser positivo.")
            if valor > self.saldo:
                self.state = 'menu_principal'
                playsound('saldo_insuficiente.mp3')
                playsound('menu_principal.mp3')
                return "Saldo insuficiente. Voltando ao menu principal."
            self.saldo -= valor
            self.extrato.append(f"Transferência de R$ {valor:.2f}")
            self.state = 'menu_principal'
            playsound('transferencia_sucesso.mp3')
            playsound('menu_principal.mp3')
            return f"Transferência de R$ {valor:.2f} realizada com sucesso. Voltando ao menu principal."
        except ValueError:
            # Se o valor for inválido, retorna ao menu principal
            self.state = 'menu_principal'
            playsound('valor_invalido.mp3')
            playsound('menu_principal.mp3')
            return "Valor inválido. Voltando ao menu principal."
    
    def pagamento_contas(self, entrada):
        # Realiza o pagamento de contas
        try:
            valor = float(entrada)
            if valor <= 0:
                raise ValueError("O valor deve ser positivo.")
            if valor > self.saldo:
                self.state = 'menu_principal'
                playsound('saldo_insuficiente.mp3')
                playsound('menu_principal.mp3')
                return "Saldo insuficiente. Voltando ao menu principal."
            self.saldo -= valor
            self.extrato.append(f"Pagamento de conta de R$ {valor:.2f}")
            self.state = 'menu_principal'
            playsound('pagamento_sucesso.mp3')
            playsound('menu_principal.mp3')
            return f"Pagamento de R$ {valor:.2f} realizado com sucesso. Voltando ao menu principal."
        except ValueError:
            # Se o valor for inválido, retorna ao menu principal
            self.state = 'menu_principal'
            playsound('valor_invalido.mp3')
            playsound('menu_principal.mp3')
            return "Valor inválido. Voltando ao menu principal."
    
    def falar_atendente(self):
        # Simula a transferência para um atendente
        self.state = 'menu_principal'
        playsound('transferindo_atendente.mp3')
        return "Transferindo para um atendente. Por favor, aguarde."
    

    def gerar_audio(self):
        #Gera audio caso nao exista
        audios = {
            "bem_vindo.mp3": "Bem-vindo ao nosso serviço de atendimento automático.",
            "digite_numero_conta.mp3": "Para continuar, por favor, digite o número da sua conta para autenticação.",
            "autenticacao_sucesso.mp3": "Autenticação bem-sucedida.",
            "menu_principal.mp3": """Menu Principal. Para consultar o saldo da sua conta, digite 1. 
                                Para obter o extrato da sua conta, digite 2. 
                                Para realizar uma transferência, digite 3. 
                                Para pagamento de contas, digite 4. 
                                Para falar com um atendente, digite 5.""",
            "saldo_conta.mp3": "O saldo da sua conta é de X reais.",
            "extrato_conta.mp3": "Seu extrato será enviado para o seu e-mail cadastrado.",
            "transferencia_digite_valor.mp3": "Para realizar uma transferência, digite o valor a ser transferido.",
            "pagamento_digite_valor.mp3": "Para pagar uma conta, digite o valor do pagamento.",
            "saldo_insuficiente.mp3": "Saldo insuficiente. Voltando ao menu principal.",
            "transferencia_sucesso.mp3": "Transferência realizada com sucesso. Voltando ao menu principal.",
            "pagamento_sucesso.mp3": "Pagamento realizado com sucesso. Voltando ao menu principal.",
            "valor_invalido.mp3": "Valor inválido. Voltando ao menu principal.",
            "opcao_invalida.mp3": "Opção inválida. Tente novamente.",
            "transferindo_atendente.mp3": "Transferindo para um atendente. Por favor, aguarde."
        }

        for filename, texto in audios.items():
            if not os.path.exists(filename):
                tts = gTTS(texto, lang='pt')
                tts.save(filename)
                print(f"Arquivo '{filename}' criado com sucesso.")
            else:
                print(f"Arquivo '{filename}' já existe e não será recriado.")


def main():
    # Função principal que inicializa a URA e lida com as entradas do usuário
    ura = URA()
    ura.gerar_audio()
    entrada = ''
    while True:
        # Processa a entrada atual e exibe a mensagem correspondente
        mensagem = ura.process_input(entrada)
        print(mensagem)
        # Coleta a próxima entrada do usuário com base no estado atual da URA
        if ura.state == 'menu_principal':
            entrada = input("Escolha uma opção: ")
        elif ura.state in ['autenticacao', 'transferencia_dinheiro', 'pagamento_contas']:
            entrada = input("Digite o valor: ")
        else:
            break

if __name__ == "__main__":
    main()