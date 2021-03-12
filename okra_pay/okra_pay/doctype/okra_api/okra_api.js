// Copyright (c) 2021, Victor Maduforo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Okra API', {
	refresh: function(frm) {
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
					var html;
					console.log(res)
					if (!res.data.accounts){
						html = `<p>${res.message}</p>`
					} else {
						frappe.msgprint(res.data.accounts[0].owner[0])
						let body = ''
						res.data.accounts.forEach(function(account){
							body = body + `
							<tr>
								<td>${account.customer.name}</td>
								<td>${account.customer._id}</td>
								<td>${account.record[0]}</td>
								<td>${account.owner[0]}</td>
								<td>${account._id}</td>
								<td>${account.bank.name}</td>
								<td>${account.nuban}</td>
								<td>${account.balance}</td>
								<td>${account.type}</td>
						  	</tr>
							`
						})
						html = `
							<p>${res.message}</p>
							<table>
								<thead>
									<tr>
										<th>Customer Name</th>
										<th>Customer ID</th>
										<th>Record ID</th>
										<th>Owner ID</th>
										<th>Account ID</th>
										<th>Bank</th>
										<th>NUBAN</th>
										<th>Balance ID</th>
										<th>Account type</th>
									</tr>
								</thead>
								<tbody>
									${body}
								</tbody>
								<tfoot>
								</tfoot>
							</table>
							`
					}
					frm.set_df_property('result', 'options', html)
				}
			})
		}, 'APIs')
		frm.add_custom_button('Validate customer', function(){
			frappe.msgprint('Visit https://app.okra.ng/MMlTswMor')
		}, 'APIs')
	}
});
