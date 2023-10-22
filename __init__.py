from universalasync import wrap
from typing import Any, Dict

import httpx

client = httpx.AsyncClient()

@wrap
class Mayar:
    def __init__(self, api_key: str, api_url: str) -> None:
        """
        Initializes a new Maya credential.

        Args:
            api_key: The API key for authentication.
            api_url: The URL for the API endpoint.
        """
        self.api_key = api_key
        self.api_url = api_url
        
    async def get_mayar(self, url) -> Dict[str, Any]:
        """
        Gets the JSON response from the Mayar API.

        Args:
            url (str): The endpoint URL to make the API request to.

        Returns:
            dict: The JSON response from the API.

        Raises:
            httpx.RequestError: If there is an error making the API request.
            httpx.HTTPStatusError: If the API returns a non-successful status code.
        """
        # Set the authorization header with the API key
        headers = {"Authorization": f"barier {self.api_key}"}

        # Make the API request
        response = await client.get(self.api_url + url, headers=headers)
            
        # Parse and return the JSON response
        return response.json()
    
    async def post_mayar(self, url, data) -> Dict[str, Any]:
        """
        Posts a JSON request to the Mayar API and returns the JSON response.

        Args:
            url (str): The URL for the API endpoint.
            data (Dict[str, Any]): The JSON data to be sent in the request.

        Returns:
            Dict[str, Any]: The JSON response from the API.

        Raises:
            httpx.HTTPError: If there is an error during the HTTP request.
        """
        # Set the headers for the request
        headers = {"Authorization": f"barier {self.api_key}"}

        # Send an HTTP POST request to the API endpoint with the specified URL, headers, and JSON data
        response = await client.post(self.api_url + url, headers=headers, json=data)

        # Convert the response to a JSON object and return it
        return response.json()

    async def all_product(self, tipe="all", page=1, page_size=10) -> Dict[str, Any]:
        """
        Gets all products from the Mayar API. Support parameter page & page size
        """
        url = f"/product?page={page}&page_size={page_size}"
        if tipe != "all":
            url = f"/product/type/{type}/?page={page}&page_size={page_size}"
        return self.get_mayar(url)
    
    async def detail_product(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single product from the Mayar API. You can also close or re open the product
        """
        url = f"/product/{id}"
        if action != "detail":
            url = f"/product/{action}/{id}"

        return self.get_mayar(url)
    
    async def search_product(self, query) -> Dict[str, Any]:
        """
        Search all product by query from the Mayar API.
        """
        return self.get_mayar(f"/product/?search={query}")
    
    async def create_invoice(self, data) -> Dict[str, Any]:
        """
        Create a new product from the Mayar API.
        """
        return self.post_mayar(f"/invoice/create", data)
    
    async def edit_invoice(self, data) -> Dict[str, Any]:
        """
        Edit a product from the Mayar API.
        """
        return self.post_mayar(f"/invoice/edit", data)
    
    async def all_invoice(self, sort="all", page=1, pageSize=10) -> Dict[str, Any]:
        """
        Gets all invoices from the Mayar API. You can also sort. eg: 
        """
        url = f"/invoice/?page={page}&pageSize={pageSize}"
        if sort != "all":
            url = f"/invoice/?sort={sort}&page={page}&pageSize={pageSize}"

        return self.get_mayar(url)
    async def detail_invoice(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single invoice from the Mayar API. You can also close or re open the product
        """
        url = f"/invoice/{id}"
        if action != "detail":
            url = f"/invoice/{action}/{id}"

        return self.get_mayar(url)

    async def create_single_payment(self, data) -> Dict[str, Any]:
        """
        Create a single payment reqeust from the Mayar API.
        """
        return self.post_mayar(f"/payment/create", data)
    
    async def edit_single_payment(self, data) -> Dict[str, Any]:
        """
        Create a single payment reqeust from the Mayar API.
        """
        return self.post_mayar(f"/payment/edit", data)
    
    async def all_single_payment(self, sort="all", page=1, pageSize=10) -> Dict[str, Any]:
        """
        Gets all payments from the Mayar API. You can also sort. eg: ?sort=closed
        """
        url = f"/payment/?page={page}&pageSize={pageSize}"
        if sort != "all":
            url = f"/payment/?sort={sort}&page={page}&pageSize={pageSize}"
        
        return self.get_mayar(url)
    
    async def detail_single_payment(self, id, action="detail") -> Dict[str, Any]:
        """
        Gets a single payment from the Mayar API. You can also close or re open the product
        """
        url = f"/payment/{id}"
        if action != "detail":
            url = f"/payment/{action}/{id}"
            
        return self.get_mayar(url)    
    
    async def balance(self) -> Dict[str, Any]:
        """
        Gets the balance from the Mayar API.
        """
        return self.get_mayar("/balance")
    
    async def paid_transaction(self, page=1, pageSize=10) -> Dict[str, Any]:
        """
        Gets the paid transaction from the Mayar API.
        """
        return self.get_mayar(f"/transactions/?page={page}&pageSize={pageSize}")
    
    async def unpaid_transaction(self, page=1, pageSize=10) -> Dict[str, Any]:
        """
        Gets the unpaid transaction from the Mayar API.
        """
        return self.get_mayar(f"/transactions/unpaid/?page={page}&pageSize={pageSize}") 

    async def all_customer(self, page=1, pageSize=10) -> Dict[str, Any]:
        """
        Gets the customer from the Mayar API.
        """
        return self.get_mayar(f"/customer/?page={page}&pageSize={pageSize}")     