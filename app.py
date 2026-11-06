import os, sqlite3
from datetime import date
from flask import Flask, request, jsonify, render_template

app=Flask(__name__); app.config["DATABASE"]=os.environ.get("DATABASE","pantryledger.sqlite3")
def db():
    c=sqlite3.connect(app.config["DATABASE"]); c.row_factory=sqlite3.Row; return c
def init_db():
    with db() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY,name TEXT NOT NULL,category TEXT NOT NULL DEFAULT 'Other',
        quantity REAL NOT NULL CHECK(quantity>=0),unit TEXT NOT NULL DEFAULT 'pcs',
        expiry_date TEXT,low_stock REAL NOT NULL DEFAULT 1,updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)""")
        c.execute("""CREATE TABLE IF NOT EXISTS shopping(
        id INTEGER PRIMARY KEY,item_name TEXT NOT NULL,quantity TEXT NOT NULL DEFAULT '1',done INTEGER NOT NULL DEFAULT 0)""")
@app.get("/")
def home(): return render_template("index.html")
@app.get("/api/items")
def items():
    with db() as c: rows=c.execute("SELECT * FROM items ORDER BY CASE WHEN quantity<=low_stock THEN 0 ELSE 1 END,expiry_date,name").fetchall()
    return jsonify([dict(x) for x in rows])
@app.post("/api/items")
def add_item():
    d=request.get_json(silent=True) or {}
    try:
        name=str(d.get("name","")).strip(); category=str(d.get("category","Other")).strip() or "Other"
        unit=str(d.get("unit","pcs")).strip() or "pcs"; qty=float(d.get("quantity",0)); low=float(d.get("low_stock",1))
        expiry=d.get("expiry_date") or None
        if not name or qty<0 or low<0: raise ValueError()
        if expiry: date.fromisoformat(expiry)
    except (ValueError,TypeError): return jsonify(error="Enter a name, valid quantity, threshold and expiry date."),400
    with db() as c:
        cur=c.execute("INSERT INTO items(name,category,quantity,unit,expiry_date,low_stock) VALUES(?,?,?,?,?,?)",(name,category,qty,unit,expiry,low))
        row=c.execute("SELECT * FROM items WHERE id=?",(cur.lastrowid,)).fetchone()
    return jsonify(dict(row)),201
@app.patch("/api/items/<int:item_id>/consume")
def consume(item_id):
    d=request.get_json(silent=True) or {}
    try: qty=float(d.get("quantity",0)); assert qty>0
    except (ValueError,TypeError,AssertionError): return jsonify(error="Consumption quantity must be positive."),400
    with db() as c:
        row=c.execute("SELECT * FROM items WHERE id=?",(item_id,)).fetchone()
        if not row: return jsonify(error="Item not found."),404
        if qty>row["quantity"]: return jsonify(error="Not enough stock."),409
        c.execute("UPDATE items SET quantity=quantity-?,updated_at=CURRENT_TIMESTAMP WHERE id=?",(qty,item_id))
        updated=c.execute("SELECT * FROM items WHERE id=?",(item_id,)).fetchone()
    return jsonify(dict(updated))
@app.delete("/api/items/<int:item_id>")
def delete_item(item_id):
    with db() as c: cur=c.execute("DELETE FROM items WHERE id=?",(item_id,))
    return ("",204) if cur.rowcount else (jsonify(error="Item not found."),404)
@app.get("/api/shopping")
def shopping():
    with db() as c:
        low=c.execute("SELECT name,CAST(MAX(1,low_stock-quantity) AS TEXT) quantity FROM items WHERE quantity<=low_stock").fetchall()
        manual=c.execute("SELECT * FROM shopping ORDER BY done,id").fetchall()
    return jsonify(low_stock=[dict(x) for x in low],manual=[dict(x) for x in manual])
@app.post("/api/shopping")
def add_shopping():
    d=request.get_json(silent=True) or {}; name=str(d.get("item_name","")).strip(); qty=str(d.get("quantity","1")).strip()
    if not name: return jsonify(error="Item name required."),400
    with db() as c:
        cur=c.execute("INSERT INTO shopping(item_name,quantity) VALUES(?,?)",(name,qty))
        row=c.execute("SELECT * FROM shopping WHERE id=?",(cur.lastrowid,)).fetchone()
    return jsonify(dict(row)),201
@app.patch("/api/shopping/<int:item_id>")
def toggle_shopping(item_id):
    with db() as c:
        row=c.execute("SELECT * FROM shopping WHERE id=?",(item_id,)).fetchone()
        if not row: return jsonify(error="List item not found."),404
        c.execute("UPDATE shopping SET done=? WHERE id=?",(0 if row["done"] else 1,item_id))
        updated=c.execute("SELECT * FROM shopping WHERE id=?",(item_id,)).fetchone()
    return jsonify(dict(updated))
with app.app_context(): init_db()
if __name__=="__main__": app.run(debug=os.environ.get("FLASK_DEBUG")=="1")
