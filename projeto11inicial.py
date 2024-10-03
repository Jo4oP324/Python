import google.generativeai as genai

GEMINI_API_KEY = 'AIzaSyDGBbPDb67IucJkMGmas1MSINPgbi3DV-w'
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def gerar_resposta(prompt):
  response = model.generate_content(prompt)
  return response.text

def iniciar_chat():
  print('Bem-vindo ao chat com a Gemini!')
  print('Tecle "sair" para encerrar o chat.')
  print('x'*20,end='\n\n')
  
  while True:
    usuario = input("Você: ")
    if usuario.lower() == 'sair':
      break
    resposta = gerar_resposta(usuario)
    print("Gemini:", resposta)

if __name__ == "__main__":
  iniciar_chat()
