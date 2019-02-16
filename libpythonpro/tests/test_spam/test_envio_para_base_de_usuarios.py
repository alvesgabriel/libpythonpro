from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com'),
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'renzo@python.pro.br.',
        'Curso Python Pro',
        'Confira os módulos fantásticos!'
    )
    assert len(sessao.usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gabriel', email='gabriel.alves.monteiro1@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos!',
    )
    enviador.enviar.assert_called_once_with(
        'luciano@python.pro.br',
        'gabriel.alves.monteiro1@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos!',
    )
