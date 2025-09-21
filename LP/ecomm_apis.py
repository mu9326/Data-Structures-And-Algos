from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory "DB" for demo purposes
widgets_db = {
    "homepage": [
        {
            "widget_id": "row_001",
            "type": "ROW",
            "size": "scale",
            "is_active": True,  # feature flag
            "elements": [
                {
                    "widget_id": "prod_link_001",
                    "type": "product_link",
                    "product_id": 10123,
                    "title": "Apple iPhone 15 Pro",
                    "price": "$999",
                    "image": "https://example.com/images/iphone15pro.png",
                    "link": "/product/10123",
                },
                {
                    "widget_id": "banner_001",
                    "type": "standalone",
                    "title": "Festival Sale – Up to 60% Off",
                    "image": "https://example.com/images/festival_banner.png",
                    "link": "/sale/festival",
                },
            ],
        }
    ]
}


# -----------------------------
# FRONTEND APIs (Read-only)
# -----------------------------
@app.route("/api/widgets/<screen_id>", methods=["GET"])
def get_widgets(screen_id):
    screen_widgets = widgets_db.get(screen_id, [])
    # Only return active widgets
    active_widgets = [w for w in screen_widgets if w.get("is_active", True)]
    return jsonify({"screen_id": screen_id, "widgets": active_widgets})


@app.route("/api/widgets/<screen_id>/<widget_id>", methods=["GET"])
def get_widget(screen_id, widget_id):
    screen_widgets = widgets_db.get(screen_id, [])
    for w in screen_widgets:
        if w["widget_id"] == widget_id and w.get("is_active", True):
            return jsonify(w)
    abort(404, description="Widget not found")


# -----------------------------
# ADMIN APIs (CRUD + Feature Flag)
# -----------------------------
@app.route("/api/admin/widgets/<screen_id>", methods=["POST"])
def create_widget(screen_id):
    data = request.json
    if not data.get("widget_id"):
        abort(400, description="widget_id is required")
    widgets_db.setdefault(screen_id, []).append(data)
    return jsonify({"message": "Widget created", "widget": data}), 201


@app.route("/api/admin/widgets/<screen_id>/<widget_id>", methods=["PUT"])
def update_widget(screen_id, widget_id):
    data = request.json
    screen_widgets = widgets_db.get(screen_id, [])
    for idx, w in enumerate(screen_widgets):
        if w["widget_id"] == widget_id:
            w.update(data)
            return jsonify({"message": "Widget updated", "widget": w})
    abort(404, description="Widget not found")


@app.route("/api/admin/widgets/<screen_id>/<widget_id>", methods=["DELETE"])
def delete_widget(screen_id, widget_id):
    screen_widgets = widgets_db.get(screen_id, [])
    for idx, w in enumerate(screen_widgets):
        if w["widget_id"] == widget_id:
            screen_widgets.pop(idx)
            return jsonify({"message": "Widget deleted"})
    abort(404, description="Widget not found")


@app.route("/api/admin/widgets/<screen_id>/<widget_id>/toggle", methods=["POST"])
def toggle_widget(screen_id, widget_id):
    screen_widgets = widgets_db.get(screen_id, [])
    for w in screen_widgets:
        if w["widget_id"] == widget_id:
            w["is_active"] = not w.get("is_active", True)
            status = "ON" if w["is_active"] else "OFF"
            return jsonify({"widget_id": widget_id, "status": status})
    abort(404, description="Widget not found")


if __name__ == "__main__":
    app.run(debug=True)
