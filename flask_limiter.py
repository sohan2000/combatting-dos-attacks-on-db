from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Initialize Flask app
app = Flask(__name__)

# Initialize Flask-Limiter
limiter = Limiter(
    app,
    key_func=get_remote_address,  # Use the remote address as the key for rate limiting
    default_limits=["200 per day", "50 per hour"]  # Global rate limits
)

# Route with a specific rate limit
@app.route('/limited')
@limiter.limit("5 per minute")
def limited_route():
    return "This route is rate-limited to 5 requests per minute."

# Exempted route from rate limiting
@app.route('/exempt')
@limiter.exempt
def exempt_route():
    return "This route is exempt from rate limits."

# A regular route (subject to global rate limits)
@app.route('/')
def home():
    return "Welcome to the home page. Global rate limits apply."

# Error handler for rate limiting
@app.errorhandler(429)
def ratelimit_handler(e):
    return "Rate limit exceeded. Please try again later.", 429

# Run the Flask app
if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080))
