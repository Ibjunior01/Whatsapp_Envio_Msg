from repositories.contato_repository import ContatoRepository

repo = ContatoRepository()

contatos = repo.listar()

for contato in contatos:
    print(dict(contato))