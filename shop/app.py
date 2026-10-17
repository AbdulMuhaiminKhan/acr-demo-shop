from flask import Flask, abort, jsonify, redirect, request, session

from .db import get_db, get_product

app = Flask(__name__)
app.secret_key = "change-me"  # loaded from the environment in production


@app.get("/products/<int:product_id>")
def product(product_id: int):
    row = get_product(get_db(), product_id)
    if row is None:
        abort(404)
    return jsonify(dict(row))


@app.post("/login")
def login():
    session["user"] = request.form["user"]
    return redirect(request.args.get("next", "/"))


@app.get("/admin/orders")
def admin_orders():
    from .db import search_orders

    rows = search_orders(get_db(), request.args.get("customer", ""), request.args.get("status", "open"))
    return jsonify([dict(r) for r in rows])
