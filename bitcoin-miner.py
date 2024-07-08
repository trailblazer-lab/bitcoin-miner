import hashlib

NONCE_LIMIT = 10000000000000
zeroes = 4

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
    return -1  # This should be outside the for loop

block_number = 24
transactions = '71627261cas82n2'
previous_hash = '81827218ss2yg0'

mine (block_number, transactions, previous_hash)                       

combined_text = str(block_number) + transactions + previous_hash 
print(hashlib.sha256(combined_text.encode()).hexdigest())