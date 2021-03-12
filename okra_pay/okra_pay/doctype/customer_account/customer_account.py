# -*- coding: utf-8 -*-
# Copyright (c) 2021, Victor Maduforo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
from frappe.model.document import Document
from okra_pay.api.api import get_account

class CustomerAccount(Document):
	def before_save(self):
		#response = get_account(self.customer_id)
		response = requests.post(
			'https://api.okra.ng/v2/sandbox/accounts/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={self.customer_id}'
		)
		res = response.json()
		#frappe.throw(res['data']['accounts'][0]['_id'])
		for account in res['data']['accounts']:
			doc = frappe.new_doc('Customer Account')
			doc.record_id = account['record'][0]
			doc.account_id = account['_id']
			doc.bank = account['bank']['name']
			doc.nuban = account['nuban']
			doc.account_type = account['type']
			doc.balance_id = account['balance']
			doc.insert()
		frappe.throw("Accounts saved successfully")
		