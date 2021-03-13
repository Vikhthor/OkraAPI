// Copyright (c) 2021, Victor Maduforo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Account', {
	/*refresh: function(frm) {
		frm.add_custom_button('Get Account', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_account',
				args: { cust_id: frm.doc.customer_id },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					console.log(res)
					if (!res.data.accounts){
						frappe.throw('No results')
					} else {
						frappe.msgprint("Accounts retrieved successfully")
						res.data.accounts.forEach(function(account){
							frm.doc.record_id = account['record'][0]
							frm.doc.account_id = account['_id']
							frm.doc.bank = account['bank']['name']
							frm.doc.nuban = account['nuban']
							frm.doc.account_type = account['type']
							frm.doc.balance_id = account['balance']
							frm.save()
						})
					}
				}
			})
		})
	}*/
});
