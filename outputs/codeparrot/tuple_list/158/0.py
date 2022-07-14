def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return max(lst, key=lst.count)[1]


def main():
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()
<|endoftext|># Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, cstr, nowdate, getdate
from erpnext.stock.utils import get_incoming_rate
from erpnext.stock.stock_ledger import get_previous_sle, NegativeStockError
from erpnext.stock.get_item_details import get_available_qty
from erpnext.stock.doctype.serial_no.serial_no import get_auto_serial_nos, get_serial_nos
from erpnext.stock.stock_ledger import get_valuation_rate
from erpnext.stock.get_item_details import get_available_serial_nos
from erpnext.stock.doctype.batch.batch import get_batch_qty, get_batch_no
from erpnext.stock.doctype.item.item import get_item_details
from erpnext.stock.doctype.stock_entry.stock_entry import get_stock_entry_details

from erpnext.controllers.stock_controller import StockController

class SellingController(StockController):
	def __setup__(self):
		if hasattr(self, "taxes"):
			self.print_templates = {
				"taxes": "templates/print_formats/includes/taxes.html"
			}

	def get_feed(self):
		return _("To {0} | {1} {2}").format(self.customer_name, self.currency,
			self.grand_total)

	def onload(self):
		if self.doctype in ("Sales Invoice", "Purchase Invoice"):
			for item in self.get("items"):
				item.update(get_available_qty(item.item_code,
					item.s_warehouse))

	def