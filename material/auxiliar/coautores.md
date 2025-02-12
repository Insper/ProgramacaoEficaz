# Commit com coautores

Responsável: Licia Sales

Commits com coautores permitem atribuir crédito a mais de uma pessoa por uma mudança feita em um repositório Git. Essa funcionalidade é útil em trabalhos em grupo.

No histórico do commit, cada coautor é listado, garantindo a visibilidade e reconhecimento às pessoas envolvidas.


### **Por que usar Commits com Coautores?**

1. **Reconhecimento:** Mostra o envolvimento de cada membro na colaboração.
2. **Rastreamento:** Facilita identificar quem contribuiu com ideias ou mudanças específicas.
3. **Documentação:** Melhora o histórico de commits, refletindo de forma clara a colaboração.
4. **Transparência:** Garante que os contribuidores sejam creditados adequadamente.


### **Como Criar um Commit com Coautores no Git?**

1. **Pelo terminal**
    - Adicione uma linha para cada coautor na mensagem do commit com o seguinte formato:

```
git commit -m "Corrigindo bug crítico no sistema

Co-authored-by: Maria Silva <maria@example.com>
Co-authored-by: João Santos <joao@example.com>"

```


### **Usar Coautores no VSCode**

Quando estiver pronto para realizar o commit, vá para o menu lateral de controle de fonte no VSCode (ícone de ramificação).

![image.png](coautores0.png)

Digite a mensagem do commit no campo fornecido.

![image.png](coautores1.png)

Adicione os coautores no seguinte formato:

```
Correção de erros no processamento de dados.

Co-authored-by: Alice Martins <alice@example.com>
Co-authored-by: Rafael Costa <rafael@example.com>

```

Clique no botão para confirmar o commit, assim, o commit será criado com os coautores especificados.


### **Dicas Extras**

Estude a documentação para realizar personalizações para facilitar essa funcionalidade:

[https://code.visualstudio.com/docs/sourcecontrol/github](https://code.visualstudio.com/docs/sourcecontrol/github)

[https://docs.github.com/pt/pull-requests/](https://docs.github.com/pt/pull-requests/)