from message import Message
# Mensagem utilizada pelo cliente para encerrar uma sessao de usuario.
# Ela deve ser usada quando se deseja reautenticar com outro usuario sem ser necessario inicializar outro cliente.
class LogoutMessage(Message):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "logout"