def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    return max(lst, key=lst.count)


def main():
    """
    The main function.
    """
    print(f([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()
<|endoftext|># Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, getdate, nowdate, cstr
from erpnext.stock.utils import get_incoming_rate
from erpnext.stock.stock_ledger import get_previous_sle, NegativeStockError
from erpnext.stock.get_item_details import get_available_qty
from erpnext.stock.doctype.serial_no.serial_no import get_auto_serial_nos, get_serial_nos
from erpnext.stock.stock_ledger import get_valuation_rate
from erpnext.stock.doctype.batch.batch import get_batch_qty
from erpnext.stock.doctype.item.item import get_item_details
from erpnext.stock.doctype.stock_entry.stock_entry import get_stock_and_rate
from erpnext.stock.stock_ledger import get_valuation_rate
from erpnext.stock.doctype.serial_no.serial_no import get_auto_serial_nos, get_serial_nos
from erpnext.stock.doctype.stock_reconciliation.stock_reconciliation import StockReconciliation
from erpnext.stock.stock_reconciliation.stock_adjustment import get_adjustment_factor
from erpnext.manufacturing.doctype.bom.bom import validate_bom_no
from erpnext.stock.doctype.work_order.work_order import get_item_details
from erpnext.manufacturing.doctype.work_order.work_order import get_item_details_for_work_order
from erpnext.stock.stock_balance import get_planned_qty, update_bin_qty, get_reserved_qty
from erpnext.stock.utils import get_bin
from