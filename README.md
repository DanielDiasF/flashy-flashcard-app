# 📇 Flashy - Flashcard App para Estudo de Idiomas

Este é um aplicativo desktop de Flashcards desenvolvido em Python para ajudar usuários no aprendizado de novos idiomas (Francês/Inglês). O projeto foi desenvolvido como parte dos meus estudos práticos de programação, aplicando conceitos de interface gráfica, manipulação de dados e persistência de arquivos.

---

## 🚀 Funcionalidades

*   **Estudo Interativo:** Cartões dinâmicos que mostram a palavra em francês e revelam a tradução em inglês após 3 segundos.
*   **Contador de Progresso:** Um contador em tempo real que mostra ao usuário quantas palavras ainda faltam para concluir o baralho.
*   **Persistência de Dados:** O aplicativo salva o progresso automaticamente. Se você fechar o programa, ele lembrará quais palavras você já aprendeu da próxima vez que abrir.
*   **Botão de Reinício (Restart):** Permite resetar todo o progresso do aprendizado e recomeçar o baralho do zero com apenas um clique.
*   **Validação de Conclusão:** Tela de parabenização automática quando o usuário zera o baralho de palavras.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando a linguagem **Python** e as seguintes ferramentas:

*   **Tkinter:** Biblioteca nativa para a construção da interface gráfica (janelas, botões, canvas e eventos de tempo).
*   **Pandas:** Biblioteca de alta performance utilizada para a leitura, manipulação e filtragem das listas de palavras armazenadas em arquivos `.csv`.
*   **OS & Random:** Módulos internos para gerenciamento de arquivos no sistema operacional e sorteio aleatório das palavras.

---

## 🗂️ Estrutura do Projeto

Para o funcionamento correto do aplicativo, os arquivos estão organizados da seguinte forma:

```text
├── main.py                # Código principal do aplicativo
├── README.md              # Documentação do projeto
├── data/
│   ├── french_words.csv   # Banco de dados original de palavras
│   └── words_to_learn.csv # Arquivo gerado dinamicamente com o progresso do usuário
└── images/
    ├── card_back.png      # Imagem do verso do cartão
    ├── card_front.png     # Imagem da frente do cartão
    ├── right.png          # Ícone do botão de acerto
    └── wrong.png          # Ícone do botão de erro
```

---

## 🔧 Como Executar o Projeto Localmente

1. Certifique-se de ter o Python instalado na sua máquina.
2. Certifique-se de instalar a biblioteca Pandas rodando o comando no terminal:
   ```bash
   pip install pandas
   ```
3. Baixe esta pasta do projeto e execute o arquivo principal:
   ```bash
   python main.py
   ```

---
💡 *Este projeto demonstra minha capacidade de criar soluções de software completas (Frontend + Lógica de Negócio + Persistência de Dados), estruturando códigos limpos com tratamento de exceções (Try/Except) para garantir uma boa experiência ao usuário.*
