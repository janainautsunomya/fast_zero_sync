from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# a barra seria a raíz do site (root)
# @app.get('/', status_code=HTTPStatus.OK, response_model=Message)
# def read_root():
#     return {'message': 'Olá Mundo!'} #deixar de comentar ctrl + k +c


@app.get(
    '/', response_class=HTMLResponse
)  # a barra seria a raíz do site (root)
def read_root():
    return """
    <html>
        <head>
            <title> Nosso Olá Mundo! </title>
        <body>
            <h1> Olá Mundo! :) </h1>
        </body>
        </head>
    </html>
    """
