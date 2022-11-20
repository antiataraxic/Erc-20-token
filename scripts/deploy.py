from brownie import DishToken
from scripts.helpful_scripts import get_account
from web3 import Web3

intial_supply = Web3.toWei(10000000000, "ether")


def deploy_token():
    account = get_account()
    token = DishToken.deploy(intial_supply, {"from": account})
    print(token.name())


def main():
    deploy_token()
