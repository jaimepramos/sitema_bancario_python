# 🏦 Sistema Bancário em Python

## 1. Introdução
Este projeto tem como objetivo implementar um **sistema bancário simples** utilizando a linguagem de programação **Python**.  
A atividade visa consolidar conhecimentos de lógica de programação, manipulação de estruturas de dados (listas e dicionários) e boas práticas na organização de funções.

---

## 2. Objetivos do Projeto
- Desenvolver um programa que simule operações bancárias básicas.  
- Aplicar conceitos de **funções**, **parâmetros posicionais e nomeados**, **listas**, **dicionários** e **estruturas de controle**.  
- Proporcionar experiência prática com **construção de menus interativos** no terminal.  
- Estimular a modularização do código, dividindo as responsabilidades em funções bem definidas.  

---

## 3. Funcionalidades Implementadas
O sistema permite ao usuário realizar as seguintes operações:

1. **Depósito (`d`)** → Permite adicionar valores ao saldo da conta.  
2. **Saque (`s`)** → Permite retirar valores da conta, respeitando as seguintes regras:
   - Saldo suficiente para a operação;  
   - Limite máximo de **R$ 500,00 por saque**;  
   - Limite de **3 saques diários**.  
3. **Extrato (`e`)** → Exibe todas as movimentações realizadas e o saldo atual da conta.  
4. **Novo Usuário (`nu`)** → Permite cadastrar clientes informando:
   - CPF,  
   - Nome completo,  
   - Data de nascimento,  
   - Endereço.  
5. **Nova Conta (`nc`)** → Cria uma conta bancária vinculada a um usuário já existente.  
6. **Listar Contas (`lc`)** → Lista todas as contas criadas no sistema, exibindo agência, número e titular.  
7. **Sair (`q`)** → Encerra o programa.  

---

## 4. Metodologia de Desenvolvimento
O projeto foi estruturado utilizando **programação procedural**, com a definição de funções para cada responsabilidade do sistema.  
Foram aplicados os seguintes conceitos:

- **Parâmetros posicionais e nomeados** (`/` e `*`) para reforçar boas práticas no uso de funções;  
- **Listas e dicionários** como estruturas principais de armazenamento de dados;  
- **Controle de fluxo** com condicionais e laços de repetição (`while`);  
- **Validações** para impedir operações inconsistentes (como saque acima do saldo ou criação de usuário duplicado).  

---

## 5. Estrutura do Código
O sistema está organizado em funções principais:

- `menu()` → Exibe o menu de opções.  
- `depositar()` → Realiza depósitos na conta.  
- `sacar()` → Controla regras de saque.  
- `exibir_extrato()` → Mostra as movimentações e o saldo.  
- `criar_usuario()` → Cadastra novos usuários.  
- `filtrar_usuario()` → Busca usuários pelo CPF.  
- `criar_conta()` → Cria novas contas para usuários existentes.  
- `listar_contas()` → Exibe todas as contas cadastradas.  
- `main()` → Função principal que integra todas as funcionalidades.  

---

## 6. Como Executar o Projeto
1. Certifique-se de ter o **Python 3.8 ou superior** instalado.  
2. Salve o código em um arquivo chamado `banco.py`.  
3. No terminal, execute o programa com:  

```bash
python banco.py
