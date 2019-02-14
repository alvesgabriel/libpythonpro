from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    from libpythonpro.spam.modelos import Usuario
    usuario = Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com'),
        Usuario(nome='Renzo', email='renzo@python.pro.br'),
        Usuario(nome='Luciano', email='luciano@python.pro.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
