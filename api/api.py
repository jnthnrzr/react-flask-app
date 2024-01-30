from datetime import UTC, datetime

from flask import Flask

app = Flask(
    __name__,
    static_folder="../build",
    static_url_path="/",
)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/time")
def get_current_time():
    current_time = datetime.now(tz=UTC)
    return {"time": current_time.isoformat("T", "seconds")}
