# # Criar contato 
# from models.contato import Contato
# from repositories.contato_repository import ContatoRepository

# repo = ContatoRepository()

# novo_contato = Contato(
#     nome="João Silva",
#     telefone="85999999999",
#     empresa="Empresa X",
#     observacoes="Cliente VIP"
# )

# repo.criar(novo_contato)

# print("Contato criado!")

# # Listar contato
# from repositories.contato_repository import ContatoRepository

# repo = ContatoRepository()

# for contato in repo.listar():
#     print(contato)

# # Atualizar 
# from models.contato import Contato
# from repositories.contato_repository import ContatoRepository

# repo = ContatoRepository()

# contato = Contato(
#     id=1,
#     nome="João Silva Atualizado",
#     telefone="85999999999",
#     empresa="Nova Empresa",
#     observacoes="Atualizado"
# )

# repo.atualizar(contato)

# Excluir
#repo.excluir(1)