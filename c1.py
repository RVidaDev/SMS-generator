from twilio.rest import Client

account_sid = "conta de exemplo"
auth_token = "token de exemplo"
twilio_phone_number = "numero do telefone do Twilio"

def send_sms(destinatario, mensagem):
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=mensagem,
            _from=twilio_phone_number,
            to=destinatario
        )
        print(f"Mensagem enviada para {destinatario} com SID: {message.sid}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {str(e)}")

if __name__ == "__main__":
    destinatario = input("Informe o número de telefone do destinatário: ")
    mensagem = input("Digite sua mensagem: ")
    
    send_sms(destinatario, mensagem)