import socket
MAX_BYTES_THRESHOLD = 2048

class Server:

    def __init__(self, port) -> None:
        self.port = port

    def run_server(self):
        # Cria socket IPV4 e TCP
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind("localhost", self.port)
        server.listen()
        while True:
            conn, addr = server.accept()
            self.send_intro_message(conn)
            with conn:
                while True:
                    # O ideal seria termos uma fila com as mensagens para que elas fossem processadas sem perda
                    # Para o EP iremos supor que o cliente sempre espera a resposta do servidor antes de enviar uma nova mensagem
                    data = conn.recv(MAX_BYTES_THRESHOLD)
                    response = self.handle_client_message(data)
                    conn.sendall(response.encode())

    def send_intro_message(self, conn):
        intro_message = """
            Ola, bem vindo ao CHATUSP, o seu assistente academico personalizado !
            Para comecar, e necessario os dados de login do aluno que quer fazer uso do servico.
            envie uma mensagem: 'auth [usuario] [senha]' para fazer o login.

            comandos suportados: 
            'auth [usuario] [senha]' - Utilizado para realizar o login no jupiterweb
            'chat [mensagem]' - Envia uma mensagem para o CHATUSP te responder
            'logout' - Sinaliza o servidor para terminar a sessao do usuario e solicitar um novo login
        """
        conn.sendall(intro_message.encode())
        return

    def handle_client_message(self, data) -> str:
        pass