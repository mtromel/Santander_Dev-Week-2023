'''
Desafio Santander Dev Week 2023 (ETL com Python)
Marcos Cristiano Trömel

'''
import pandas as pd
import requests
import json

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

def generate_ai_news(user):
  news = ""
  if user['id'] == 4573: 
    news = "Isa, faça seu dinheiro trabalhar para você. Invista com confiança! #CrescimentoFinanceiro"
  
  if user['id'] == 4614: 
    news = "André, invista no seu futuro financeiro! Seu banco está pronto para ajudar. #Investimentos"
  
  if user['id'] == 4615: 
    news = "Lapontele, invista agora e assegure seu amanhã financeiro. #CresçaSeuPatrimônio"
  
  if user['id'] == 4667: 
    news = "Travis, invista sabiamente, construa seu futuro. Seu banco está aqui para orientar! #CresçaSeuPatrimônio"
  
  if user['id'] == 4722: 
    news = "Marceleta, invista agora e prepare-se para um futuro financeiro sólido. #InvistaHoje"

  return news

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

for user in users:
  news = generate_ai_news(user)
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })

  for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")