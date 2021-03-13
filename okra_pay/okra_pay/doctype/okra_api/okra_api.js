// Copyright (c) 2021, Victor Maduforo and contributors
// For license information, please see license.txt

frappe.ui.form.on('Okra API', {
	refresh: function(frm) {
		frm.add_custom_button('Get customers', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_customers',
				args: {},
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.customers.forEach(function(cust){
							body = body + `
							<tr>
								<td>${cust.name}</td>
								<td>${cust._id}</td>
								<td>${cust.credentials[0].bank.name}</td>
								<td>${cust.record[0]}</td>
								<td>${cust.email[0]}</td>
								<td>${cust.phone[0]}</td>
								<td>${cust.blocked}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Customer name</th>
										<th>Customer ID</th>
										<th>Bank name</th>
										<th>Record ID</th>
										<th>Email</th>
										<th>Phone no</th>
										<th>Blocked</th>
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
		}, 'Customer info')
		frm.add_custom_button('Validate customer', function(){
			frappe.msgprint('Visit https://app.okra.ng/MMlTswMor')
		}, 'Customer info')
		frm.add_custom_button('Auth customer', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_auth',
				args: {
					cust_id: frm.doc.customer_id
				},
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.auths){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.auths.forEach(function(auth){
							body = body + `
							<tr>
								<td>${auth._id}</td>
								<td>${auth.customer.name}</td>
								<td>${auth.bank.name}</td>
								<td>${auth.validated}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Auth ID</th>
										<th>Customer name</th>
										<th>Bank</th>
										<th>Validated</th>
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
		}, 'Customer info')
		frm.add_custom_button('Get account', function(){
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
						// frappe.msgprint(res.data.accounts[0].owner[0])
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
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
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
					res.data.accounts.forEach(function(account){
						frappe.db.insert({
							doctype: "Customer Account",
							customer: frm.doc.customer,
							customer_id: frm.doc.customer_id,
							record_id: account['record'][0],
							account_id: account['_id'],
							bank: account['bank']['name'],
							nuban: account['nuban'],
							account_type: account['type'],
							balance_id: account['balance']
						})
					})		
				}
			})
		}, 'Customer info')
		frm.add_custom_button('Get identity', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_identity',
				args: { cust_id: frm.doc.customer_id },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.identity){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.identity.forEach(function(id){
							body = body + `
							<tr>
								<td>${id.firstname}</td>
								<td>${id.lastname}</td>
								<td>${id.bvn}</td>
								<td>${id.email[0]}</td>
								<td>${id.address}</td>
								<td>${id.phone}</td>
								<td>${id.verified}</td>
								<td>${id.marital_status}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>First name</th>
										<th>Last name</th>
										<th>BVN</th>
										<th>Email</th>
										<th>Address</th>
										<th>Phone</th>
										<th>Verified</th>
										<th>Marital status</th>
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
		}, 'Customer info')
		frm.add_custom_button('Get BVN identity', function(){
			frappe.call({
				method: 'okra_pay.api.api.verify_bvn',
				args: { cust_id: frm.doc.bvn },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data){
						html = `<p>${res.message}</p>`
					} else {
						body = `
						<tr>
							<td>${res.data.firstname}</td>
							<td>${res.data.lastname}</td>
							<td>${res.data.bvn}</td>
							<td>${res.data.email[0]}</td>
							<td>${res.data.address[0]}</td>
							<td>${res.data.phone[0]}</td>
							<td>${res.data.verified}</td>
							<td>${res.data.status}</td>
						</tr>
						`
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>First name</th>
										<th>Last name</th>
										<th>BVN</th>
										<th>Email</th>
										<th>Address</th>
										<th>Phone</th>
										<th>Verified</th>
										<th>Status</th>
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
		}, 'Customer info')
		frm.add_custom_button('Get balance', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_balance',
				args: { cust_id: frm.doc.customer_id },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.balance){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.balance.forEach(function(bal){
							body = body + `
							<tr>
								<td>${bal._id}</td>
								<td>${bal.account.nuban}</td>
								<td>${bal.account.bank.name}</td>
								<td>${bal.available_balance}</td>
								<td>${bal.ledger_balance}</td>
								<td>${bal.currency}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Balance ID</th>
										<th>NUBAN</th>
										<th>Bank</th>
										<th>Available Bal</th>
										<th>Ledger Bal</th>
										<th>Currency</th>
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
		}, 'Customer info')
		frm.add_custom_button('Get income', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_income',
				args: { cust_id: frm.doc.customer_id },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.income){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.income.forEach(function(inc){
							body = body + `
							<tr>
								<td>${inc.customer.name}</td>
								<td>${inc.streams[0].account}</td>
								<td>${inc.streams[0].avg_monthly_income}</td>
								<td>${inc.streams[0].monthly_income}</td>
								<td>${inc.streams[0].income_type}</td>
								<td>${inc.number_of_income_streams}</td>
								<td>${inc.projected_yearly_income}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Name</th>
										<th>Account ID</th>
										<th>Avg. Monthly (NGN)</th>
										<th>Monthly (NGN)</th>
										<th>Type</th>
										<th>No. of streams</th>
										<th>Yearly (NGN)</th>
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
		}, 'Customer info')
		frm.add_custom_button('Get transaction', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_transaction',
				args: { cust_id: frm.doc.customer_id },
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.transaction){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.transaction.forEach(function(txn){
							body = body + `
							<tr>
								<td>${txn._id}</td>
								<td>${txn.notes.desc}</td>
								<td>${txn.trans_date}</td>
								<td>${txn.debit || ''}</td>
								<td>${txn.credit || ''}</td>
								<td>${txn.bank.name}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Transaction ID</th>
										<th>Description</th>
										<th>Txn date</th>
										<th>Debit (NGN)</th>
										<th>Credit (NGN)</th>
										<th>Bank</th>
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
		}, 'Customer info')
		frm.add_custom_button('Initiate payment', function(){
			frappe.call({
				method: 'okra_pay.api.api.initiate_pay',
				args: { 
					debit: frm.doc.debit_account,
					credit: frm.doc.credit_account,
					amount: frm.doc.amount,
					currency: frm.doc.currency
				},
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.payment){
						html = `<p>${res.message}</p>`
					} else {
						var pay = res.data;
						var body =`
							<tr>
								<td>${pay.payment.id}</td>
								<td>${pay.payment.link}</td>
								<td>${pay.customer.name}</td>
								<td>${pay.customer.account.nuban}</td>
								<td>${pay.customer.account.id}</td>
								<td>${pay.customer.account.bank.name}</td>
								<td>${pay.payment.status}</td>
						  	</tr>
							`
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Payment ID</th>
										<th>Payment link</th>
										<th>Customer</th>
										<th>NUBAN</th>
										<th>Account ID</th>
										<th>Bank</th>
										<th>Status</th>
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
		}, 'Payments')
		frm.add_custom_button('Verify payment', function(){
			frappe.call({
				method: 'okra_pay.api.api.verify_pay',
				args: { 
					pay_id: frm.doc.payment_id
				},
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.payment_status){
						html = `<p>${res.message}</p>`
					} else {
						var pay = res.data.payment_status;
						var body =`
							<tr>
								<td>${pay._id}</td>
								<td>${pay.customer}</td>
								<td>${pay.currency}</td>
								<td>${pay.status}</td>
						  	</tr>
							`
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Payment ID</th>
										<th>Customer ID</th>
										<th>Currency</th>
										<th>Status</th>
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
		}, 'Payments')
		frm.add_custom_button('Bank support', function(){
			frappe.call({
				method: 'okra_pay.api.api.get_banks',
				args: {},
				freeze: true,
				btn: $('.primary-action'),
				async: true,
				callback: function(result){
					// var res = JSON.parse(result);
					var res = result.message;
					var html;
					console.log(res)
					if (!res.data.banks){
						html = `<p>${res.message}</p>`
					} else {
						let body = ''
						res.data.banks.forEach(function(bank){
							body = body + `
							<tr>
								<td>${bank.id}</td>
								<td>${bank.name}</td>
								<td>${bank.status}</td>
								<td>${bank.ussd}</td>
								<td>${bank.products.includes('auth')}</td>
								<td>${bank.products.includes('balance')}</td>
								<td>${bank.products.includes('identity')}</td>
								<td>${bank.products.includes('direct-debit')}</td>
								<td>${bank.products.includes('transactions')}</td>
								<td>${bank.products.includes('income')}</td>
						  	</tr>
							`
						})
						html = `
							<h3>${res.message}</h3><hr>
							<table border="1" bordercolor="green">
								<thead>
									<tr>
										<th>Bank ID</th>
										<th>Bank name</th>
										<th>Status</th>
										<th>USSD</th>
										<th>Auth</th>
										<th>Balance</th>
										<th>Identity</th>
										<th>Direct debit</th>
										<th>Transactions</th>
										<th>Income</th>
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
		})
	}
});
