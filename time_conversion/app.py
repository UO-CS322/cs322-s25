from flask import Flask, request, jsonify, render_template
import arrow
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main page."""
    return render_template("converter.html")


@app.route("/_convert_times")
def convert_times():
    """Convert local time to UTC and ISO format."""
    try:
        # Get the local time from the request
        local_time_str = request.args.get("local_time", type=str)
        logger.debug("Received time string: %s", local_time_str)

        # Get the local timezone
        local_tz = datetime.now().astimezone().tzinfo
        logger.debug("Local timezone: %s", local_tz)

        # Parse the local time with the local timezone
        local_time = arrow.get(local_time_str).replace(tzinfo=local_tz)
        logger.debug("Parsed local time: %s", local_time)

        # Convert to UTC
        utc_time = local_time.to("UTC")
        logger.debug("UTC time: %s", utc_time)

        # Return the converted times in two different formats
        return jsonify(
            {
                "utc_time": utc_time.format("HH:mm:ss"),
                "iso_format": utc_time.format("YYYY-MM-DDTHH:mm:ssZZ"),
            }
        )

    except arrow.parser.ParserError as e:
        logger.error("Time parsing error: %s", str(e))
        return jsonify({"error": "Invalid time format"}), 400
    except ValueError as e:
        logger.error("Value error: %s", str(e))
        return jsonify({"error": "Invalid time value"}), 400


if __name__ == "__main__":
    app.run(port=5000, debug=True)
