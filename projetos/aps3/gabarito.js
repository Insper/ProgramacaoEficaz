// 1
db.livros.find({ disponivel: true })
// 2
db.livros.find({ autor: "Machado de Assis" })
// 3
db.livros.updateOne(
    { titulo: "Poemas para um Mundo Novo 5" },
    { $set: { disponivel: false } }
  )
// 4
db.livros.deleteMany({ ano: { $lt: 1900 } })
// 5
db.livros.insertOne({
    titulo: "O Pequeno Príncipe",
    autor: "Antoine de Saint-Exupéry",
    ano: 1943,
    disponivel: true
  })
// 6
db.livros.insertMany([
    {
      titulo: "1984",
      autor: "George Orwell",
      ano: 1949,
      disponivel: true
    },
    {
      titulo: "A Revolução dos Bichos",
      autor: "George Orwell",
      ano: 1945,
      disponivel: true
    },
    {
      titulo: "O Senhor dos Anéis",
      autor: "J.R.R. Tolkien",
      ano: 1954,
      disponivel: true
    }
  ])
// 7
db.usuarios.updateOne(
    { nome: "Ana" },
    { $push: { emprestimos: { titulo: "A Revolução dos Bichos", data_emprestimo: "2024-08-15" } } }
  )
// 8
db.usuarios.find({ "emprestimos.0": { $exists: true } })
// 9
db.usuarios.find(
    { nome: "Ana" },
    { nome: 1, "emprestimos.titulo": 1, _id: 0 }
  )
// 10
db.usuarios.find({
    emprestimos: {
      $elemMatch: { titulo: "Mistérios de Pedra 1" }
    }
  })
  // ou
db.usuarios.find({ "emprestimos.titulo": "Mistérios de Pedra 1" })
// 11
db.usuarios.aggregate([
    { $unwind: "$emprestimos" },
    { $group: { _id: "$emprestimos.titulo" } },
    { $project: { _id: 0, titulo: "$_id" } }
  ])
  