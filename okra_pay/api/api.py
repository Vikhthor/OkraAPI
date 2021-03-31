import frappe
import requests

@frappe.whitelist(allow_guest=True)
def get_account(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/accounts/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_identity(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/identity/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def verify_bvn(bvn):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/products/kyc/bvn-verify',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'bvn={bvn}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_banks():
    response = requests.get(
			'https://api.okra.ng/v2/sandbox//banks/list',
			headers={
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_balance(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/balance/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}&page=1&limit=1'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_income(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/income/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_customer(key, value):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/customers/find-customers-by',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'key={key}&value={value}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_customers():
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/customers/list',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8',
				'data': 'page=1&limit=3'
			}
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_transaction(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/transactions/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def get_auth(cust_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/auth/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def initiate_pay(debit, amount, currency, credit=None):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/pay/initiate',
			headers={
				'Content-Type': 'application/json',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			json={
    			"account_to_debit": debit,
				"account_to_credit": credit,
    			"amount": amount, 
    			"currency": currency,
			}
		)
    return response.json()

@frappe.whitelist(allow_guest=True)
def verify_pay(pay_id):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/pay/verify',
			headers={
				'Content-Type': 'application/json',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			json={
    			"payment_id": pay_id,
			}
		)
    return response.json()
@frappe.whitelist(allow_guest=True)
def initiate_recurring(debit, amount, currency, interval, start_date, end_date, credit=None):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/pay/initiate',
			headers={
				'Content-Type': 'application/json',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			json={
    			"account_to_debit": debit,
				"account_to_credit": credit,
				"type": 'recurring',
				"schedule": {
					"interval": interval,
					"startDate": start_date,
					"endDate": end_date
				},
    			"amount": amount, 
    			"currency": currency,
			}
		)
    return response.json()
@frappe.whitelist(allow_guest=True)
def initiate_recurring_paylink(name, amount, currency, interval, start_date, end_date, credit="60643e1e4f03af09a5e043ad"):
    response = requests.post(
			'https://api.okra.ng/v2/sandbox/pay/link/create',
			headers={
				'Content-Type': 'application/json',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			json={
				"name": name,
				"account": credit,
				"type": 'recurring',
				"note": "Test payment",
				"countries": ["NG"],
				"schedule": {
					"interval": interval,
					"startDate": start_date,
					"endDate": end_date
				},
    			"amount": amount, 
    			"currency": currency,
				"data": True,
				"success_url": "http://localhost:8000/demo-customer",
				"callback_url": "https://blooming-anchorage-51722.herokuapp.com/api/webhook",
				"continue_cta": "Please continue"
			}
		)
    return response.json()