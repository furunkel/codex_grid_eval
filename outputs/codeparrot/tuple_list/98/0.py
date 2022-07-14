def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return max(lst, key=lst.count)[1]


def main():
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()
<|endoftext|># Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, getdate, formatdate, get_link_to_form, \
	comma_or, get_fullname
from erpnext.accounts.report.financial_statements import (get_period_list, get_columns, get_data)

def execute(filters=None):
	period_list = get_period_list(filters.from_fiscal_year, filters.to_fiscal_year,
		filters.periodicity, filters.accumulated_values, filters.company)

	income = get_data(filters.company, "Income", "Credit", period_list, filters=filters)

	income_data = get_data(filters.company, "Income", "Credit", period_list, filters=filters)

	columns, expense_accounts, tax_accounts = get_columns(income_data, expense_accounts)

	net_profit_loss = get_net_profit_loss(income_data, expense_accounts)

	data = []
	for d in expense_accounts:
		row = [d.name, d.account, d.posting_date, d.supplier, d.supplier_name, d.bill_no, d.bill_date,
			d.remarks, d.cost_center, d.project_name, d.company, d.sales_order, d.delivery_note, d.income_account,
			d.cost_center, d.qty, d.base_rate, d.base_amount]

		if net_profit_loss:
			row += [net_profit_loss]

		row += [