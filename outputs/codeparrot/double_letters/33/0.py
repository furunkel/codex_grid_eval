
def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every number.
    All other characters should be output a single time each.
    """

def main():
    """
    Main function.
    """
    # Get the input
    input_string = sys.stdin.readline().strip()
    # Split the input into words
    words = input_string.split()
    # Create a list of all the words
    words_list = []
    # For each word in the list
    for word in words:
        # Add the word to the list
        words_list.append(word)
    # Sort the list
    words_list.sort()
    # Print the words
    print_words(words_list)

if __name__ == "__main__":
    main()
<|endoftext|># Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint, cstr, nowdate, getdate, formatdate
from erpnext.stock.get_item_details import get_bin_details
from erpnext.stock.utils import get_incoming_rate
from erpnext.stock.stock_ledger import get_previous_sle, NegativeStockError
from erpnext.stock.get_item_details import get_conversion_factor
from erpnext.stock.doctype.batch.batch import get_batch_no
from erpnext.stock.doctype.item.item import get_item_details
from erpnext.stock.doctype.serial_no.serial_no import get_serial_nos, get_auto_serial_nos
from erpnext.stock.doctype.stock_reconciliation.stock_reconciliation import StockReconciliation
from erpnext.stock.stock_reconciliation.stock_reconciliation import StockRenumberingError
from erpnext.stock.doctype.purchase_receipt.purchase_receipt import (get_item_details as get_item_details_from_purchase_receipt)
from erpnext.stock.stock_reconciliation.stock_reconciliation import (get_item_details as get_item_details_from_stock_reconciliation)
from erpnext.stock.stock_reconciliation.stock_reconciliation