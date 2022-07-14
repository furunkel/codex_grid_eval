def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest third value.
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
from erpnext.stock.doctype.serial_no.serial_no import get_auto_serial_nos
from erpnext.stock.stock_ledger import get_valuation_rate
from erpnext.stock.doctype.batch.batch import get_batch_qty
from erpnext.stock.doctype.item.item import get_item_details

class NotUpdateStockError(frappe.ValidationError): pass
class StockOverReturnError(frappe.ValidationError): pass
class IncorrectValuationRateError(frappe.ValidationError): pass
class DuplicateEntryForProductionOrderError(frappe.ValidationError): pass
class OperationsNotCompleteError(frappe.ValidationError): pass

from erpnext.controllers.stock_controller import StockController

form_grid_templates = {
	"items": "templates/form_grid/stock_entry_grid.html"
}

class StockEntry(StockController):
	def get_feed(self):
		return _("From {0} to {1}").format(self.from_warehouse, self.to_warehouse)

	def onload(self):
		for item in self.get("items"):
			item.update(get_available_qty(item.item_code, item.s_warehouse))

	def validate(self):
		self.pro_doc = None
		if self.production_order:
			self.pro_doc = frappe.get_