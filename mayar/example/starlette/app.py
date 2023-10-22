# example starlatte/fastapi

import asyncio
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import (Route, Mount)
from mayar import Mayar

API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ZGJhNDk5Ni03ZDc0LTQ4M2UtOTlmZS1iNTJjNjAzNjhjYjUiLCJhY2NvdW50SWQiOiI0Zjk5NWIyNi00NjU1LTRkZDItYjdlNC0xMWY2YzM2MzU5MjQiLCJjcmVhdGVkQXQiOiIxNjk3OTcwODI5MzE1Iiwicm9sZSI6ImRldmVsb3BlciIsInN1YiI6Imt1Z3V0c3UuaGlydWtvQGdtYWlsLmNvbSIsIm5hbWUiOiJhbmRyZWEiLCJsaW5rIjoia29yYmFuLW1vdGl2YXRvciIsImlzU2VsZkRvbWFpbiI6bnVsbCwiaWF0IjoxNjk3OTcwODI5fQ.ZVpOthjNHB3KyvbH4aAJTiQ0VlKj3-IVldZb96_cuBxUzvwdUBsSDc_uwQl3m7zhOizs_z4GCJtZJ01ebFUTVIh_C_9HBQfmfSnL2IGrXdDU5XJbANCBpXsHLXrUFDBT-80OZAPNz_UY93po2cjx9N19Utr7i8hdZ7glQB-7Xb-NL5rw5ocl0fR2r_ZpR_nYkltyNrwq-dEOmW7x2cRKhTNpAP2T2Jat69DXK4CHYUfbg2M6YghRKnIjLX8qgmO859CQRMTBEALremTJvOTU8xVqPXQcmOtakijJch0PHnZRk3WIZE55GlQ7PKAEpwhY-oCDlfE-z-PD7FaO9pHEUA"
# for production use API_URL = "https://api.mayar.id/hl/v1"
API_URL = "https://api.mayar.club/hl/v1"

async def products(request):
    page = 1
    if request.query_params["page"]:
        page = request.query_params["page"]

    page_size = 10
    if request.query_params["page_size"]
        page_size = request.query_params["page_size"]

    myr = Mayar(API_KEY, API_URL)
    page_product = await myr.all_product(page=page, page_size=page_size)
    return JSONResponse(page_product)

async def cretae_invoice(request):
    myr = Mayar(API_KEY, API_URL)
    body = {
      "name": "andre",
      "email": "alikusnadie@gmail.com",
      "mobile": "0857975222",
      "redirectUrl": "https://kelaskami.com/nexst23", 
      "description": "isi dari description ini ka",
      "items":[
        {
          "quantity": 3,
          "rate": 15000,
          "description": "ayam jago"
        }
      ]
    }
    create_invoice = await myr.createInvoice(body)
    return JSONResponse(create_invoice)

app = Starlette(debug=True, routes=[
    Route('/product/', products),
    Route('/invoice/create', cretae_invoice),
    
])
