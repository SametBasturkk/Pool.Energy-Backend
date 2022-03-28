import pytest
from unittest.mock import AsyncMock


class WalletRpcClient(object):
    async def create_signed_transaction(self):
        pass


@pytest.fixture(scope="module")
def wallet_rpc_client():
    return AsyncMock(WalletRpcClient)
