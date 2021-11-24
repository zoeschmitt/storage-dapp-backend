import os
from brownie import accounts, config, SimpleStorage
import os

def deploy_simple_storage():
    account = accounts[0] # brownie-made account
    # account = accounts.load('bc-dev')
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from": account}) # deploying contract
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1) # 1 is for how many blocks we want to wait for
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def main():
    deploy_simple_storage()