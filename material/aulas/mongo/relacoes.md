# Como modelar relações entre documentos no MongoDB usando **Embeddings**

## O que são relações em bancos de dados?

Em qualquer banco de dados, seja relacional (como MySQL) ou não relacional (como MongoDB), **relacionar dados** significa **ligar informações de diferentes entidades**.

Por exemplo:
- Um usuário pode ter um endereço.
- Um pedido pode ter uma lista de produtos.
- Um aluno pode estar matriculado em várias disciplinas.

Essas **relações entre entidades** são essenciais para organizar, consultar e manter os dados de forma eficiente.


## Formas de representar relações no MongoDB

O MongoDB oferece duas abordagens principais para representar relações entre documentos:

1. **Referências**: armazenar o `id` de um documento dentro de outro (semelhante a uma foreign key).
2. **Embeddings (documentos embutidos)**: **inserir um documento dentro de outro**.

Embedding é a técnica de armazenar um documento inteiro como um campo dentro de outro documento.
Ou seja, em vez de manter os dados separados em coleções diferentes (como tabelas), você aninha um documento dentro de outro para mantê-los juntos no mesmo registro. Da mesma forma como fazíamos dicionários contendo outros dicionários.

> A própria documentação do MongoDB recomenda:
> > **“What you use together, store together.”**  
> Se você sempre acessa duas entidades juntas, **considere embutir** os dados!


## Quando usar **embeddings**?

Use embeddings quando:
- A relação for do tipo **um-para-um (1:1)** ou **um-para-poucos (1:N)**.
- Os dados embutidos **não forem compartilhados** com outros documentos.
- Você **acessa essas informações juntas com frequência**.


## Exemplo prático: relação **1:1**

Imagine que você tem um sistema de biblioteca. Cada **leitor** possui um **endereço**. Essa é uma relação **um-para-um**: cada leitor tem exatamente um endereço.

### Sem embedding (documentos separados):

```json
// Documento da coleção "leitores"
{
   _id: "joe",
   name: "Joe Bookreader"
}

// Documento da coleção "enderecos"
{
   patron_id: "joe",
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}
```

Nesse caso, para buscar o endereço de Joe, seria necessário juntar manualmente(join manual) os dados de duas coleções. Isso é possível, mas menos performático.

### Com embedding (documento único):

```json
// Documento da coleção "leitores"
{
   _id: "joe",
   name: "Joe Bookreader",
   address: {
      street: "123 Fake Street",
      city: "Faketon",
      state: "MA",
      zip: "12345"
   }
}
```

Agora, todos os dados do leitor estão juntos em um único documento, como um dicionário de dicionários. Isso torna a leitura de dados muito mais rápida e simples!

## Benefícios do uso de embeddings

- Mais performance em leitura (menos buscas no banco)
- Estrutura de dados mais natural e compacta
- Ideal para dados que pertencem fortemente ao “dono” (como o endereço de um usuário)

## Quando não usar embeddings?

Evite embeddings se:

- O dado embutido cresce demais (ex: milhares de comentários em um post).
- O dado embutido precisa ser acessado independentemente ou em massa.
- Você precisa atualizar os dados embutidos com muita frequência.

## Referencias:

- [Relacionamentos um para um](https://www.mongodb.com/docs/manual/tutorial/model-embedded-one-to-one-relationships-between-documents/)

- [Relacionamentos um para muitos](https://www.mongodb.com/pt-br/docs/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/)

- [Relacionamentos muitos para muitos](https://www.mongodb.com/pt-br/docs/manual/tutorial/model-embedded-many-to-many-relationships-between-documents/)