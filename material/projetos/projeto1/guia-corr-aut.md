# Configuração da Correção Automática

1. Acesse a página do repositório do projeto no GitHub e clique na aba `Settings`/`Configurações`.

    <figure markdown="span">
        ![Configurações do repositório](webhook-config-01.png){ width="100%" }
        <figcaption>Configurações do repositório</figcaption>
    </figure>

2. No menu lateral, clique em `Webhooks`
    
    <figure markdown="span">
        ![Menu Webhooks](webhook-config-02.png){ width="100%" }
        <figcaption>Menu Webhooks</figcaption>
    </figure>

3. Clique no botão `Add webhook`/`Adicionar webhook`.
    
    <figure markdown="span">
        ![Adicionar Webhook](webhook-config-03.png){ width="100%" }
        <figcaption>Adicionar Webhook</figcaption>
    </figure>

4. Preencha os campos conforme a seguir:

    - Payload URL: 
        ``` 
        http://3.130.178.228/progeficaz/Projeto1
        ```
    - Content type: `application/json`
    - Secret: `progeficaz20252`

    <!-- <figure markdown="span">
        ![URL do payload](webhook-config-04.png){ width="100%" }
        <figcaption>URL do payload</figcaption>
    </figure> -->

    - Which events would you like to trigger this webhook?: `Let me select individual events`
        - Deixe {==**APENAS**==} a opção `Releases` selecionada.

        <!-- <figure markdown="span">
            ![opções marcadas](webhook-config-05.png){ width="100%" }
            <figcaption>Opções Selecionadas</figcaption>
        </figure> -->

        - {==**DESMARQUE**==} a opção `Pushes` caso esteja selecionada.
        
        <figure markdown="span">
            ![opção pushes](webhook-config-05b.png){ width="100%" }
        </figure>

    - E por fim, deixe a opção `Active` selecionada e clique no botão `Add webhook`/`Adicionar webhook`.
        <figure markdown="span">
            ![opções Active](webhook-config-06.png){ width="100%" }
        </figure>

    
5. Clone o seu repositório do Github.
    
    Altere o arquivo `README.md` e adicione o nome do seu repositório no GitHub, conforme o exemplo abaixo:

    ```html title="Conteúdo do README.md"
    ## Status da Entrega
    <img 
        src="http://3.130.178.228/progeficaz/Projeto1/svg/insper-classroom/NOME DO SEU REPOSITORIO" 
        alt="svg" 
        width="100%" 
        height="300px"
    />
    ```

    <figure markdown="span">
        ![Nome do Repositório](webhook-config-07.png){ width="50%" }
        <figcaption>Nome do Repositório</figcaption>
    </figure>

    O valor do atributo `src` deve ser alterado com o nome do seu repositório.

6. Faça o commit e o push do arquivo `README.md` para o repositório do Github.

[Fazendo submissões](submetendo.md){ .md-button }

    

    