from app import app
import pytest
@pytest.fixture
def client(tmp_path):
    app.config["TESTING"]=True; app.config["DATABASE"]=str(tmp_path/"test.sqlite3")
    from app import init_db
    with app.app_context(): init_db()
    return app.test_client()
def test_item_stock_and_shopping(client):
    r=client.post("/api/items",json={"name":"Rice","quantity":3,"unit":"kg","low_stock":1})
    assert r.status_code==201
    item=r.get_json()
    assert client.patch(f"/api/items/{item['id']}/consume",json={"quantity":1}).status_code==200
    assert client.get("/api/shopping").get_json()["low_stock"]
