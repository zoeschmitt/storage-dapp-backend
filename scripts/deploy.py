import os
from brownie import accounts, config, SimpleStorage, network
import os

def deploy_simple_storage():
    account = get_account() 
    simple_storage = SimpleStorage.deploy({"from": account}) # deploying contract
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1) # 1 is for how many blocks we want to wait for
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    # account = accounts.load('bc-dev') # to get priv key encrypted by brownie
    if network.show_active() == "development":
        return accounts[0] # brownie-made account
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()