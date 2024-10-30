from datetime import datetime
import random
import os
import platform
from time import sleep

class Usuario:
    def __init__(self, nome, idade, login, senha):
        self._nome = nome
        self._idade = idade
        self._login = login
        self._senha = senha
        self._saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(Cores.GREEN + f"Depósito de R$ {valor:.2f} realizado com sucesso!" + Cores.RESET)
        else:
            print(Cores.RED + "Erro: O valor do depósito deve ser positivo." + Cores.RESET)

    def exibir_saldo(self):
        print(Cores.GREEN + f"Seu saldo atual é: R$ {self._saldo:.2f}" + Cores.RESET)
        sleep(4)

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor):
        self._saldo = valor

    def get_senha(self):
        return self._senha

    def get_nome(self):
        return self._nome

class Cores:
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

def limpar_terminal():
    if platform.system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

class CadastroLogin:
    def __init__(self):
        self._usuarios = {}

    def _calcular_idade(self, ano_nascimento):
        ano_atual = datetime.today().year
        return ano_atual - ano_nascimento

    def cadastrar_usuario(self):
        limpar_terminal()
        print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
        print(Cores.CYAN + "   === Cadastro de Usuário ===" + Cores.RESET)
        print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
        nome = input(Cores.YELLOW + "\nDigite seu nome: " + Cores.RESET)

        while True:
            ano_nascimento = input(Cores.YELLOW + "Digite seu ano de nascimento (aaaa): " + Cores.RESET)
            try:
                ano_nascimento = int(ano_nascimento)
                
                data_atual = datetime.now().year
                if ano_nascimento >= data_atual + 1:
                    print(Cores.RED + "Informe um ano de nascimento válido." + Cores.RESET)
                    continue
                
                idade = self._calcular_idade(ano_nascimento)
                if idade < 18:
                    print(Cores.RED + "Erro: Somente maiores de 18 anos podem se cadastrar." + Cores.RESET)
                    continue
                
                if ano_nascimento < 1920:
                    print(Cores.RED + "Informe um ano de nascimento válido." + Cores.RESET)
                    continue
                
                break
                
            except ValueError:
                print(Cores.RED + "Informe um ano de nascimento válido." + Cores.RESET)
                sleep(4)
        
        login = input(Cores.YELLOW + "Escolha um login: " + Cores.RESET)
        senha = input(Cores.YELLOW + "Escolha uma senha: " + Cores.RESET)

        if login in self._usuarios:
            print(Cores.RED + "Erro: Esse login já está em uso. Tente outro." + Cores.RESET)
        else:
            usuario = Usuario(nome, idade, login, senha)
            self._usuarios[login] = usuario
            print(Cores.GREEN + f"Usuário {nome} cadastrado com sucesso!" + Cores.RESET)

    def fazer_login(self):
        limpar_terminal()
        print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
        print(Cores.CYAN + "           === Login ===" + Cores.RESET)
        print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
        login = input(Cores.YELLOW + "\nDigite seu login: " + Cores.RESET)
        senha = input(Cores.YELLOW + "Digite sua senha: " + Cores.RESET)

        if login in self._usuarios and self._usuarios[login].get_senha() == senha:
            print(Cores.GREEN + f"Bem-vindo, {self._usuarios[login].get_nome()}!" + Cores.RESET)
            sleep(3)
            return self._usuarios[login]
        else:
            print(Cores.RED + "Erro: Login ou senha incorretos." + Cores.RESET)
            sleep(3)
            return None

    def realizar_deposito(self, usuario):
        limpar_terminal()
        print(Cores.CYAN + "\n----------- REALIZAR DEPÓSITO -----------" + Cores.RESET)
        valor = float(input(Cores.YELLOW + "\nDigite o valor para depósito: R$ " + Cores.RESET))
        usuario.depositar(valor)

class Rolo:
    def __init__(self):
        self._frutas = ['🍒', '🍋', '🍊', '🍇', '🍉', '🍓', '🍍']
        self._simbolo_atual = None

    def girar(self):
        self._simbolo_atual = random.choice(self._frutas)
        return self._simbolo_atual

class Maquina:
    def __init__(self, nome):
        self._nome = nome
        self._ativo = True

    def iniciar_maquina(self):
        if self._ativo:
            print(Cores.GREEN + f"A máquina {self._nome} está iniciando..." + Cores.RESET)
        else:
            print(Cores.RED + f"A máquina {self._nome} está desativada." + Cores.RESET)

    def desativar_maquina(self):
        self._ativo = False
        print(Cores.RED + f"A máquina {self._nome} foi desativada." + Cores.RESET)

class MaquinaCacaNiquel(Maquina):
    def __init__(self):
        super().__init__("Caça-Níquel")
        self._rolo1 = Rolo()
        self._rolo2 = Rolo()
        self._rolo3 = Rolo()

    def girar_todos_os_rolos(self):
        return [
            self._rolo1.girar(),
            self._rolo2.girar(),
            self._rolo3.girar()
        ]

    def iniciar_maquina(self):
        super().iniciar_maquina()
        print(Cores.GREEN + "Os rolos estão prontos para girar!" + Cores.RESET)

class JogoCacaNiquel:
    def __init__(self, usuario):
        self._usuario = usuario
        self._maquina = MaquinaCacaNiquel()

    def jogar(self):
        limpar_terminal()
        while True:
            if self._usuario.get_saldo() <= 0:
                print(Cores.RED + "Saldo insuficiente, verifique seu saldo!" + Cores.RESET)
                sleep(4)
                break

            print(Cores.GREEN + f"\nSeu saldo atual é: R${self._usuario.get_saldo():.2f}" + Cores.RESET)

            try:
                aposta = float(input(Cores.YELLOW + "\nDigite o valor da sua aposta: R$" + Cores.RESET))
                
                if aposta > self._usuario.get_saldo():
                    print(Cores.RED + "Você não tem saldo suficiente para essa aposta!" + Cores.RESET)
                    sleep(3)
                    continue
                if aposta <= 0:
                    print(Cores.RED + "Aposta inválida! Por favor, insira um valor positivo." + Cores.RESET)
                    sleep(3)
                    continue
            except ValueError:
                print(Cores.RED + "Por favor, insira um valor válido." + Cores.RESET)
                sleep(3)
                continue

            self._maquina.iniciar_maquina()
            resultado = self._maquina.girar_todos_os_rolos()

            for i in range(1, 4):
                limpar_terminal()
                print(Cores.YELLOW + f'\n[ {i} ] PREPARANDO RESULTADO' + Cores.RESET)
                sleep(2)
                limpar_terminal()
            
            print(Cores.GREEN + f"\nResultado: {resultado[0]} | {resultado[1]} | {resultado[2]}" + Cores.RESET)

            if resultado[0] == resultado[1] == resultado[2]:
                premio = aposta * 20
                self._usuario.set_saldo(self._usuario.get_saldo() + premio)
                print(Cores.GREEN + f"\nMEUS PARABÉNS, VOCE GANHOU O PREMIO DE R${premio:.2f}!" + Cores.RESET)
            else:
                self._usuario.set_saldo(self._usuario.get_saldo() - aposta)
                print(Cores.RED + f"\nNÃO FOI DESSA VEZ, VOCE PERDEU R${aposta:.2f}. QUEM SABE NA PRÓXIMA!" + Cores.RESET)

            print(Cores.GREEN + f"Seu saldo agora é: R${self._usuario.get_saldo():.2f}" + Cores.RESET)

            continuar = input(Cores.YELLOW + "\nDeseja continuar jogando? \n[1] SIM: \n[2] NÃO: " + Cores.RESET)
            limpar_terminal()
            if continuar == '2':
                break

class Cassino:
    def __init__(self):
        self._cadastro_login = CadastroLogin()

    def iniciar(self):
        while True:
            limpar_terminal()
            print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
            print(Cores.CYAN + "=== SISTEMA DE CADASTRO E LOGIN ===" + Cores.RESET)
            print(Cores.CYAN + " "*3 + "="*28 + Cores.RESET)
            print(Cores.YELLOW + "\n[ 1 ] - CADASTRAR NOVO USUÁRIO" + Cores.RESET)
            print(Cores.YELLOW + "[ 2 ] - FAZER LOGIN" + Cores.RESET)
            print(Cores.YELLOW + "[ 3 ] - SAIR" + Cores.RESET)

            opcao = input(Cores.YELLOW + "\nESCOLHA UMA OPÇÃO: " + Cores.RESET)

            if opcao == "1":
                self._cadastro_login.cadastrar_usuario()
            elif opcao == "2":
                usuario = self._cadastro_login.fazer_login()
                if usuario:
                    self.menu_cassino(usuario)
            elif opcao == "3":
                print(Cores.GREEN + "SAINDO DO SISTEMA..." + Cores.RESET)
                sleep(2)
                break
            else:
                print(Cores.RED + "OPÇÃO INVALIDA! TENTE NOVAMENTE" + Cores.RESET)

    def menu_cassino(self, usuario):
        while True:
            limpar_terminal()
            print(Cores.CYAN + " "*3 + "="*14 + Cores.RESET)
            print(Cores.CYAN + "=== MENU CASSINO ===" + Cores.RESET)
            print(Cores.CYAN + " "*3 + "="*14 + Cores.RESET)
            print(Cores.YELLOW + "\n[ 1 ] - INICIAR JOGO DE CAÇA-NÍQUEL" + Cores.RESET)
            print(Cores.YELLOW + "[ 2 ] - VERIFICAR SALDO" + Cores.RESET)
            print(Cores.YELLOW + "[ 3 ] - FAZER UM DEPÓSITO" + Cores.RESET)
            print(Cores.YELLOW + "[ 4 ] - SAIR DO JOGO" + Cores.RESET)

            opcao = input(Cores.YELLOW + "\nESCOLHA UMA OPÇÃO: " + Cores.RESET)

            if opcao == "1":
                jogo = JogoCacaNiquel(usuario)
                jogo.jogar()
            elif opcao == "2":
                usuario.exibir_saldo()

            elif opcao == "3":
                self._cadastro_login.realizar_deposito(usuario)
            elif opcao == "4":
                print(Cores.GREEN + "Saindo do cassino..." + Cores.RESET)
                break
            else:
                print(Cores.RED + "Opção inválida! Tente novamente." + Cores.RESET)


if __name__ == "__main__":
    cassino = Cassino()
    cassino.iniciar()
