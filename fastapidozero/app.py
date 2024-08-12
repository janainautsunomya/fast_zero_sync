from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # a barra seria a raíz do site (root)
def read_root():
    return {'message': 'Olá Mundo!'}
