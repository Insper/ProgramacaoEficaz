from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {
        "id": 1,
        "title": "Receita de miojo",
        "content": "Bata com um martelo antes de abrir o pacote. Misture o tempero, coloque em uma vasilha e aproveite seu snack :)"
    },
    {
        "id": 2,
        "title": "Pão doce",
        "content": "Abra o pão e coloque o seu suco em pó favorito."
    },
    {
        "id": 3,
        "title": "Sorvete com cristais de leite",
        "content": "Sirva o seu sorvete favorito em uma vasilha e jogue leite em cima."
    },
    {
        "id": 4,
        "title": "Iogurte natural",
        "content": "Deixe o leite fora da geladeira (esse é mentira, não faça isso)."
    },
    {
        "id": 5,
        "title": "Homer Simpson",
        "content": "~( 8(|)"
    },
    {
        "id": 6,
        "title": "Numero mágico",
        "content": "142857"
    },
    {
        "id": 7,
        "title": "Série da Fundação - Isaac Asimov",
        "content": "É boa, leia."
    }
]

# Obter todas as notas
@app.route("/api/notes/", methods=["GET"])
def get_notes():
    return jsonify(notes)

# Obter uma nota pelo ID
@app.route("/api/notes/<int:note_id>/", methods=["GET"])
def get_note(note_id):
    note = next((n for n in notes if n["id"] == note_id), None)
    if note:
        return jsonify(note)
    return jsonify({"error": "Nota não encontrada"}), 404

# Criar uma nova nota
@app.route("/api/notes/", methods=["POST"])
def create_note():
    data = request.json
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    new_id = max([n["id"] for n in notes], default=0) + 1
    new_note = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"],
    }
    notes.append(new_note)
    return jsonify(new_note), 201

# Atualizar uma nota existente
@app.route("/api/notes/<int:note_id>/", methods=["PUT"])
def update_note(note_id):
    data = request.json
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return jsonify({"error": "Nota não encontrada"}), 404

    note["title"] = data.get("title", note["title"])
    note["content"] = data.get("content", note["content"])
    return jsonify(note)

# Deletar uma nota
@app.route("/api/notes/<int:note_id>/", methods=["DELETE"])
def delete_note(note_id):
    global notes
    updated_notes = [n for n in notes if n["id"] != note_id]
    if len(updated_notes) == len(notes):
        return jsonify({"error": "Nota não encontrada"}), 404
    notes = updated_notes
    return jsonify({"message": "Nota deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
