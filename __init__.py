from universalasync import get_event_loop, wrap
from typing import Any, Dict

import httpx

@wrap
class Mayar:
    def __init__(self, api_key, api_url, **kwargs):
        """
        Initializes a new instance of the class.
        """
        self.api_key = api_key
        self.api_url = api_url
        
    def get_mayar(self, url) -> Dict[str, Any]:
        """
        Gets the JSON response from the Mayar API.
        """
        headers = {"Authorization": f"barier {self.api_key}"}
        response = httpx.get(self.api_url + url, headers=headers)
        return response.json()
    
    def post_mayar(self, url, data) -> Dict[str, Any]:
        """
        Posts the JSON response from the Mayar API.
        """
        headers = {"Authorization": f"barier {self.api_key}"}
        response = httpx.post(self.api_url + url, headers=headers, json=data)
        return response.json()
    
    def all_product(self, tipe="all", page=1, page_size=10) -> Dict[str, Any]:
        """
        Gets all products from the Mayar API. Support parameter page & page size
        """
        url = f"/product?page={page}&page_size={page_size}"
        if tipe != "all":
            url = f"/product/type/{type}/?page={page}&page_size={page_size}"
        return self.get_mayar(url)
    
    def detail_product(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single product from the Mayar API. You can also close or re open the product
        """
        url = f"/product/{id}"
        if action != "detail":
            url = f"/product/{action}/{id}"

        return self.get_mayar(url)
    
    def search_product(self, query) -> Dict[str, Any]:
        """
        Search all product by query from the Mayar API.
        """
        return self.get_mayar(f"/product/?search={query}")
    
    def create_invoice(self, data) -> Dict[str, Any]:
        """
        Create a new product from the Mayar API.
        """
        return self.post_mayar(f"/invoice/create", data)
    
    def edit_invoice(self, data) -> Dict[str, Any]:
        """
        Edit a product from the Mayar API.
        """
        return self.post_mayar(f"/invoice/edit", data)
    
    def invoices(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single product from the Mayar API. You can also close or re open the product
        """
        url = f"/invoice/{id}"
        if action != "detail":
            url = f"/invoice/{action}/{id}"

        return self.get_mayar(url)
    def detail_invoice(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single product from the Mayar API. You can also close or re open the product
        """
        url = f"/invoice/{id}"
        if action != "detail":
            url = f"/invoice/{action}/{id}"

        return self.get_mayar(url)

    