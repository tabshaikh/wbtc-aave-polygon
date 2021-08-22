## Ideally, they have one file with the settings for the strat and deployment
## This file would allow them to configure so they can test, deploy and interact with the strategy

BADGER_DEV_MULTISIG = (
    "0xc388750A661cC0B99784bAB2c55e1F38ff91643b"  # TODO: Maybe needs to be changed
)

WANT = "0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6"  ## wBTC
LP_COMPONENT = "0x5c2ed810328349100a66b82b78a1791b101c9d61"  ## amWBTC
REWARD_TOKEN = "0x0d500b1d8e8ef31e21c99d1db9a6444d3adf1270"  ## wMATIC

PROTECTED_TOKENS = [WANT, LP_COMPONENT, REWARD_TOKEN]
## Fees in Basis Points
DEFAULT_GOV_PERFORMANCE_FEE = 1000
DEFAULT_PERFORMANCE_FEE = 1000
DEFAULT_WITHDRAWAL_FEE = 50

FEES = [DEFAULT_GOV_PERFORMANCE_FEE, DEFAULT_PERFORMANCE_FEE, DEFAULT_WITHDRAWAL_FEE]

REGISTRY = "0xFda7eB6f8b7a9e9fCFd348042ae675d1d652454f"  # Multichain BadgerRegistry
