import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['renzo@pythonpro.com.br', 'lucino@pythonpro.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'gabriel.alves.monteiro1@gmail.com',
        'Curso Python Pro',
        '''Olá, Gabriel.
        Seja bem-vindo a primeira turma Guido Van Rossum.'''
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['renzo', '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'gabriel.alves.monteiro1@gmail.com',
            'Curso Python Pro',
            '''Olá, Gabriel.
            Seja bem-vindo a primeira turma Guido Van Rossum.'''
        )
