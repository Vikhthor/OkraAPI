# -*- coding: utf-8 -*-
# Copyright (c) 2021, Victor Maduforo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
from frappe.model.document import Document

class OkraAPI(Document):
	def get_account(self, cust_id=''):
		response = requests.post(
			'https://api.okra.ng/v2/sandbox/accounts/getByCustomer',
			headers={
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			data = f'customer={cust_id}'
		)
		return response.json()
	def validate_cust(self):
		frappe.local.flags.redirect_location = '127.0.0.1:8001/demo-customer'
		raise frappe.Redirect
