import frappe
# import requests
import json
from okra_pay.api import api

@frappe.whitelist(allow_guest=True)
def webhook():
    # print(frappe.request.data)
    data = json.loads(frappe.request.data)
    # data = json.loads(data)
    # data = frappe.local.form_dict.data
    method = data['method']
    if method == "AUTH":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.bank = data["bankName"]
            doc.auth_status = data["status"]
            doc.save()
            return "Webhook received successfully"
        except frappe.exceptions.DoesNotExistError:
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.bank = data["bankName"]
            doc.auth_status = data["status"]
            doc.insert()
            return "Webhook received successfully"
    elif method == "IDENTITY":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.identity_status = data["status"]
            doc.identity_id = data['identity']['id']
            doc.bvn = data['identity']['bvn']
            doc.name1 = data['identity']['name']
            doc.phone = data['identity']['phone'][0]
            doc.email = data['identity']['email'][0]
            doc.save()
            return "Webhook received successfully"
        except frappe.exceptions.DoesNotExistError:
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.identity_status = data["status"]
            doc.identity_id = data['identity']['id']
            doc.bvn = data['identity']['bvn']
            doc.name1 = data['identity']['name']
            doc.phone = data['identity']['phone'][0]
            doc.email = data['identity']['email'][0]
            doc.insert()
            return "Webhook received successfully"
    elif method == "PAYMENT":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.pay_status = data['status']
            doc.append('history', {
                'payment_id': data['paymentId'],
                'customer': data['customerId'],
                'bank': data['bankName'],
                'amount': data['schedule']['current_amount'],
                'status': data['status'],
                'datetime': data['ended_at']        
            })
            doc.save()
            return "Webhook received successfully"
        except frappe.exceptions.DoesNotExistError:
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.pay_status = data['status']
            doc.append('history', {
                'payment_id': data['paymentId'],
                'customer': data['customerId'],
                'bank': data['bankName'],
                'amount': data['schedule']['current_amount'],
                'status': data['status'],
                'datetime': data['ended_at']        
            })
            doc.insert()
            return "Webhook received successfully"
    elif method == "BALANCE" or method == "PERIODIC_BALANCE":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.bal_status = data['status']
            doc.save()
        except frappe.exceptions.DoesNotExistError:
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.bal_status = data['status']
            doc.insert()
        finally:
            return "Webhook received successfully"
    elif method == "TRANSACTIONS":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.txn_status = data['status']
            doc.save()
        except frappe.exceptions.DoesNotExistError:
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.txn_status = data['status']
            doc.insert()
        finally:
            return "Webhook received successfully"
    elif method == "INCOME":
        try:
            doc = frappe.get_doc('Okra Webhook', data["customerId"])
            doc.inc_status = data['status']
            doc.save()
        except 'DoesNotExistError':
            doc = frappe.new_doc('Okra Webhook')
            doc.customer_id = data["customerId"]
            doc.inc_status = data['status']
            doc.insert()
        finally:
            return "Webhook received successfully"
