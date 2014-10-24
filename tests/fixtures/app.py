import pytest

from gatlin import create_app
from gatlin.extensions import db



@pytest.yield_fixture(autouse=True)
def application():
    """application with context."""
    app = create_app()

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()



@pytest.yield_fixture()
def database():
    """database setup."""
    db.create_all()  # Maybe use migration instead?

    yield db

    db.drop_all()
