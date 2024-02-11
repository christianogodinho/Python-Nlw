from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with http
    '''

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        # lógica de regra de negócio
        print("Estou na minha view")
        print(product_code)
        # retorno http
        return HttpResponse(status_code= 200, body={"hello": "world"})
    