class PrintCartItemMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path == "/hello/products_cart/" and request.method == "POST":
            item = request.POST.get("item")
            if item:
                print(f'カートに追加された商品: {item}')
        response = self.get_response(request)
        return response