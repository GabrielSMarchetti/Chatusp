from message import Message
# Mensagem utilizada para enviar uma mensagem ao chatbot pelo cliente. 
class ChatMessage(Message):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__()

    def __str__(self) -> str:
        return f"chat {self.message}"