import secrets

def generate_api_key():
  api_key = secrets.token_hex(16)
  # store the API key in a database or file
  return api_key

api_key = generate_api_key()

print(api_key)
