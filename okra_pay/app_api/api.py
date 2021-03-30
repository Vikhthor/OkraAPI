import frappe
import json

@frappe.whitelist(allow_guest=True)
def activity_log():
    try:
        data = json.loads(frappe.request.data)
        first_name = ''
        if 'email' in data:
            first_name = frappe.db.get_value('Contact', {'email_id': data['email']}, 'first_name')
        elif 'phone' in data:
            first_name = frappe.db.get_value('Contact', {'phone': data['phone']}, 'first_name')
        if first_name:
            log = frappe.new_doc('Activity Log')
            log.subject = f'Mobile: {first_name} login'
            log.operation = 'Login'
            log.status = data['status']
            log.content = data['message']
            log.communication_date = frappe.utils.now()
            log.full_name = first_name
            log.insert()
            frappe.db.commit()
        elif not first_name:
            log = frappe.new_doc('Activity Log')
            log.subject = f'Mobile: User None login'
            log.operation = 'Login'
            log.status = data['status']
            log.content = data['message']
            log.communication_date = frappe.utils.now()
            log.insert()
            frappe.db.commit()
        return 'Activity logged successfully'
    except Exception as e:
        return frappe.throw(e)
    
