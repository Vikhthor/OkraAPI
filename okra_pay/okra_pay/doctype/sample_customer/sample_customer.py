# -*- coding: utf-8 -*-
# Copyright (c) 2021, Victor Maduforo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import requests
from frappe.model.document import Document

class SampleCustomer(Document):
	def before_save(self):
		response = requests.post(
			'https://api.okra.ng/v2/sandbox/customers/create',
			headers={
				'Content-Type': 'application/json',
				'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDQ4Y2Q5YzI5NzYzODFiMjA4NTgxZjMiLCJpYXQiOjE2MTUzODM5NjV9.x9gkonVoV22TaYjJpk59jqpXAZRwKz9NLbnlvrMoA_8'
			},
			json=[{
    			"noOfAccount": self.noofaccount,
				"name": self.fullname,
    			"bank": self.bank, 
    			"username": self.username,
    			"password": self.password,
    			"type": self.type,
    			"volume": self.volume,
    			"identity": self.identity,
    			"internetSpeed": 4
			}]
		)
		res = response.json()
		customer = res['data']['customers'][0]
		doc = frappe.new_doc('Customer Credentials')
		doc.id = customer['_id']
		doc.full_name = customer['identity']['name']
		doc.email = customer['identity']['email']
		doc.customer_id = customer['customer']
		doc.bvn = customer['identity']['bvn']
		doc.account_type = customer['identity']['type']
		doc.bank_id = customer['account']['bank']
		doc.username = customer['account']['username']
		doc.password = customer['account']['password']
		doc.otp = customer['account']['OTP']
		doc.pin = customer['account']['pin']
		doc.token = customer['account']['token']
		doc.bank_name = customer['account']['bankDetails']['name']
		doc.nubans = customer['account']['nuban'][0] + ' ' + customer['account']['nuban'][1]
		doc.insert()
