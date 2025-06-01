from web3 import Web3
import json
from app.config import CONTRACT_ADDRESS, PRIVATE_KEY, AIRDROP_WALLET

w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org/"))
contract_abi = json.loads("""[ABI اینجا]""")
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def send_tokens(to_address, amount):
    tx = contract.functions.transfer(to_address, amount).build_transaction({
        'gas': 200000,
        'gasPrice': w3.to_wei('5', 'gwei'),
        'nonce': w3.eth.get_transaction_count(AIRDROP_WALLET),
    })
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.to_hex(tx_hash)
