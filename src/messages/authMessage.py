from message import Message
# Mensagem utilizada para enviar os dados de login de um usuario ao jupiterweb.
class AuthMessage(Message):
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        super().__init__()

    def __str__(self) -> str:
        return f"auth {self.username} {self.password}"