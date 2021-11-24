from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # -1 to always work with the most recent deployment of the contract

def main():
    read_contract()