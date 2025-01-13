import requests

def request_api():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado 4xx/5xx
        return response.json()  # Devolver directamente el JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

res = request_api()
if res:
    print(res)
