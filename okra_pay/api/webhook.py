import frappe
# import requests
from okra_pay.api import api

@frappe.whitelist(allow_guest=True)
def webhook(data):
    # print('Hello world')
    method = data['method']
    code = data['code']
    if method == "AUTH" and code == "AUTH_SUCCESS":
        res = api.get_customer('_id', data.customerId)
        customer = res['data']
        try:
            doc = frappe.get_doc({'doctype':'Customer Credentials', 'customer_id': customer['_id']})
            doc.full_name = customer['name']
            doc.email = customer['email']
            doc.phone = customer['phone']
            doc.bank_name = data['bankName']
            doc.bank_id = data['bankId']
            doc.record_id = data['record']
            doc.save()
        except 'DoesNotExistError':
            doc = frappe.new_doc('Customer Credentials')
            doc.customer_id = customer['_id']
            doc.full_name = customer['name']
            doc.email = customer['email']
            doc.phone = customer['phone']
            doc.bank_name = data['bankName']
            doc.bank_id = data['bankId']
            doc.record_id = data['record']
            doc.insert()
    if method == "IDENTITY" and code == "PRODUCT_IS_READY":
        try:
            doc = frappe.get_doc({'doctype':'Customer Credentials', 'customer_id': data['identity']['customer']})
            doc.bvn = data['identity']['bvn']
            doc.dob = data['identity']['dob']
            doc.gender = data['identity']['gender']
            doc.save()
        except 'DoesNotExistError':
            doc = frappe.new_doc('Customer Credentials')
            doc.bvn = data['identity']['bvn']
            doc.dob = data['identity']['dob']
            doc.gender = data['identity']['gender']
            doc.insert()

