from datetime import UTC, datetime

from flask import Flask

app = Flask(__name__)


@app.route("/time")
def get_current_time():
    current_time = datetime.now(tz=UTC)
    return {"time": current_time.isoformat("T", "seconds")}
