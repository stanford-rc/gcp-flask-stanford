import os
import tempfile

import pytest

from gcpflask import server


@pytest.fixture
def client():
    os.environ["FLASKAPP_DATABASE"] = "sqlite"
    _, database_file = tempfile.mkstemp()
    os.environ["FLASKAPP_DATABASE_FILE"] = database_file
    server.app.config["TESTING"] = True

    # Test running init_db
    with server.app.test_client() as client:
        yield client

    os.unlink(database_file)


def test_basic_views(client):
    """Test empty views"""
    for view in ["/", "/cardinal"]:
        rv = client.get(view)
        assert rv.status_code == 200


def test_api(client):
    """Test api endpoints"""
    rv = client.get("/api/")
    for url in ["/api/", "/api/crayons/", "/api/crayons/<string:name>/"]:
        assert url in rv.json

    rv = client.get("/api/crayons/")
    assert len(rv.json) == 120

    rv = client.get("/api/crayons/wild-strawberry/")
    assert rv.json["name"] == "Wild Strawberry"

    rv = client.get("/api/crayons/does-not-exist/")
    assert rv.status_code == 404
