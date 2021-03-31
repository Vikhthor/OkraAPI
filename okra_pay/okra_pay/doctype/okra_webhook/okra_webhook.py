# -*- coding: utf-8 -*-
# Copyright (c) 2021, Victor Maduforo and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
# from frappe.model.naming import getseries
import frappe.model.rename_doc as rd

class OkraWebhook(Document):
	def autoname(self):
		if self.name1:
			self.name = self.name1
		else:
			self.name = self.customer_id
	def validate(self):
		if self.name1:
			rd.rename_doc(self.doctype, self.name, self.name1, force=True, merge=False, ignore_permissions=False, ignore_if_exists=False)
