
def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2B hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return blake2b(text.encode('utf-8'), digest_size=32).hexdigest()


def hash_to_string(hash):
    """
    Given a BLAKE2B hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.
    """
    if hash is None:
        return ''
    else:
        return hash.decode('utf-8')


def get_hash_of_block(block):
    """
    Given a block, return its hash.
    """
    return string_to_hash(json.dumps(block, sort_keys=True))


def is_valid_block(block, previous_hash):
    """
    Check if block is valid by comparing the previous_hash and block_hash.
    """
    if previous_hash != block['previous_hash']:
        return False
    return get_hash_of_block(block) == block['block_hash']


def add_block(transactions, chain):
    """
    Create a new Block in the Blockchain
    """
    previous_block = chain[-1]
    previous_hash = get_hash_of_block(previous_block)

    block = {
        'block_number': previous_block['block_number'] + 1,
        'timestamp': time.time(),
        'transactions': transactions,
        'previous_hash': previous_hash,
    }

    block['block_hash'] = get_hash_of_block(block)
    chain.append(block)


def make_a_transaction(transaction_amount, sender_address, recipient_address):
    """
    Create a transaction to go into the next mined Block
    """
    return {
        'transaction_amount': transaction_amount,
        'sender_address': sender_address,
        'recipient_address': recipient_address,
    }


def get_balance(participant):
    """
    Calculate and return the balance for a participant.
    """
    tx_sender = [[tx['transaction_