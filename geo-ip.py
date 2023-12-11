from flask import Flask, request, abort
import geoip2.database

app = Flask(__name__)

# Load the GeoIP2 database
reader = geoip2.database.Reader('/path/to/GeoLite2-City.mmdb')
# Remember to replace /path/to/GeoLite2-City.mmdb with the actual path to your downloaded GeoIP2 database file.
# Also, adapt the allowed countries list (allowed_countries) to your requirements.

def get_location(ip_address):
    try:
        response = reader.city(ip_address)
        return response.country.iso_code  # Example: 'US', 'DE', etc.
    except geoip2.errors.AddressNotFoundError:
        return None

def geo_ip_limiter():
    user_ip = request.remote_addr
    country_code = get_location(user_ip)

    # Define allowed countries
    allowed_countries = ['US', 'CA']  # Example: Allow USA and Canada

    if country_code not in allowed_countries:
        abort(403)  # Forbidden access

# Example of route with Geo-IP limiting
@app.route('/')
def home():
    geo_ip_limiter()  # Apply Geo-IP limiting
    return "Welcome to the home page."

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
