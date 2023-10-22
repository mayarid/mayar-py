# mayar-py

Mayar Python Client. **Still in heavy developtment**.

Untuk mulai menggunakan Mayar Headless API, Tentunya kita butuh akun account, untuk membuat akun bisa ke https://myr.id. jika sudah punya akun, API KEY bisa di dapatkan dari https://web.myr.id/api-keys. Bila menemukan bugs mohon di laporkan lewat issue yak sob.


Fitur yang sudah didukung:
  
* Product
  * All product
  * Product by Type
  * Search product by name
  * Detail product
  * Close Product by id
  * Open product by id
* Invoice 
  * create Invoice
  * edit Invoice
  * detail Invoice
  * close invoice
  * all Invoice
  * closed invoice
  * re open invoice
* Single Payment
  * create single payment
  * edit single payment
  * all single payment
  * closed single payment
  * re open single payment
* Transaction
  * paid transaction
  * unpaid transaction
* Customer
  * all customer
* Balance
  * balance account     

## Installasi

```py

pip install git+https://github.com/mayarid/mayar-py.git

```

## Credential

```py

api_key = "your api key"
api_url = "https://api.mayar.club/hl/v1"

# Production menggunakan
api_url = "https://api.mayar.id/hl/v1"

```
## Product

```py
from mayar import Mayar

myr = Mayar(api_key, api_url)
all_product = myr.all_product()
# with pagination (page, page_size)
page_product = myr.all_product(page=1, page_size=10)
# tipe product. untuk detail lengkap tipe product, silahlan merujuk ke dokumentasi mayar
tipe_product = myr.all_product(tipe="generic_link", page=1, page_size=10)
# search product
search_product = myr.search_product("nama produk")
# detail product
detailProduct = myr.detail_product(id="00a1cd6a-0a30-4746-bd30-06d2f619041e")
# close product. 
close_product = myr.detail_product(id="00a1cd6a-0a30-4746-bd30-06d2f619041e", action="closed")
# open product
open_product = myr.detail_product(id="00a1cd6a-0a30-4746-bd30-06d2f619041e",  action="open")

# Jika menggunakan async. 
open_product = await myr.detail_product(id="00a1cd6a-0a30-4746-bd30-06d2f619041e",  action="open")

```

## Invoice

```py
from mayar import Mayar

myr = Mayar(api_key, api_url)
all_invoice = myr.all_invoice()
# with pagination (page, page_size)
page_invoice = myr.all_invoice(page=1, page_size=10)
# sort by open/closed. untuk detail lengkap tipe product, silahlan merujuk ke dokumentasi mayar
tipe_invoice = myr.all_product(sort="closed", page=1, page_size=10) # tipe="open"
# detail product
detail_invoice = myr.detail_invoice(id="00a1cd6a-0a30-4746-bd30-06d2f619041e")
# close product
close_invoice = myr.detail_invoice(id="00a1cd6a-0a30-4746-bd30-06d2f619041e", action="closed")
# open product
open_invoice = myr.detail_invoice(id="00a1cd6a-0a30-4746-bd30-06d2f619041e",  action="open")

# create Invoice

body = {
      "name": "andre",
      "email": "kugutsu.hiruko@gmail.com",
      "mobile": "0857975222",
      "redirectUrl": "https://kelaskami.com/nexst23", # optional, bisa lihat lengkap di dokumentasi mayar
      "description": "isi dari description ini ka",
      "items":[
        {
          "quantity": 3,
          "rate": 15000,
          "description": "ayam jago"
        }
      ]
    }

create_invoice = myr.createInvoice(body)
# edit invoice
# id : gunakan id sebagai id invoice yg ingin diedit
edit_body = {
      "id": "bdf9d972-811f-4472-8fdc-2baae04b5148",
      "name": "andre",
      "email": "kugutsu.hiruko@gmail.com",
      "mobile": "0857975222",
      "redirectUrl": "https://kelaskami.com/okeoce",
      "description": "coba dulu kak",
      "items":[
        {
          "quantity": 3,
          "rate": 12000,
          "description": "ayam jago kecil"
        }
      ]
    }

edit_invoice = myr.edit_invoice(body)
edit_invoice = await myr.edit_invoice(body)

```

## Single Payment

```py
from mayar import Mayar

myr = Mayar(api_key, api_url)

all_single_payment = myr.all_single_payment()
# with pagination (page, page_size)
page_single_payment = myr.all_single_payment(page=1, page_size=10)
# tipe closed/open. untuk detail lengkap tipe product, silahlan merujuk ke dokumentasi mayar
tipe_single_payment= myr.all_single_payment(sort="closed", page=1, page_size=10) # tipe="open"
# detail product
detail_single_payment = myr.detail_single_payment(id="00a1cd6a-0a30-4746-bd30-06d2f619041e")
# close product
close_single_payment = myr.detail_single_payment(id="00a1cd6a-0a30-4746-bd30-06d2f619041e", action="closed")
# open product
open_single_payment = myr.detail_single_payment(id="00a1cd6a-0a30-4746-bd30-06d2f619041e",  action="open")

# menggunakan async
close_single_payment = await myr.detail_single_payment(id="00a1cd6a-0a30-4746-bd30-06d2f619041e", action="closed")

# create Single Payment / Penagihan

body = {
      "name": "andre",
      "email": "kugutsu.hiruko@gmail.com",
      "amount": 170000,
      "mobile": "085797522261",
      "redirectUrl": "https://kelaskami.com/nexst23",
      "description": "cobalah dulu yak gaes"
    }

create = myr.create_single_payment(body)
# edit single reqeust payment / penagihan. selain id opsional, hanya provide data yg ingin diubah
# id : id single request payment yang ingin di buat

body = {
      "id": "bdf9d972-811f-4472-8fdc-2baae04b5148",
      "name": "andre", 
      "email": "kugutsu.hiruko@gmail.com",
      "amount": 270000,
      "mobile": "085797522261",
      "redirectUrl": "https://kelaskami.com/nexst23",
      "description": "cobalah dulu yak gaes"
    }

edit = myr.edit_single_payment(body)

```

## Customer

```py
from mayar import Mayar

# your credential
myr = Mayar(api_key, api_url)
all_customer = myr.all_customer()
# with pagination (page, page_size)
page_customer = myr.all_customer(page=1, page_size=10)

```

## Transaction

```py
from mayar import Mayar

# your credential
myr = Mayar(api_key, api_url)
# paid transaction
paid = myr.paid_transactions()
# unpaid transaction
unpaid = myr.unpaid_transactions(page=1, page_size=10)
```
## Account Balance

```py
from mayar import Mayar

# your credential
myr = Mayar(api_key, api_url)
# paid transaction
balance = myr.balance()

```

