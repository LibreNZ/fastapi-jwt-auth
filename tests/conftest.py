import logging
logging.basicConfig(level=logging.DEBUG)
import pytest
from libre_fastapi_jwt import AuthJWT
from libre_fastapi_jwt.config import LoadConfig


@pytest.fixture(scope="module")
def Authorize():
    return AuthJWT()


@pytest.fixture(autouse=True)
def reset_config():
    """
    Resets config to default to
    guarantee that config is unchanged after test.
    """
    yield

    @AuthJWT.load_config
    def default_conf():
        return LoadConfig(
            authjwt_secret_key="secret",
            authjwt_cookie_samesite="strict",
            authjwt_cookie_secure=True,
        )
