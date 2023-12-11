from flask import Flask, request, abort

app = Flask(__name__)

# List of blacklisted IP addresses
BLACKLISTED_IPS = ['192.168.0.1', '10.0.0.1']  # Example IPs
# In this example, BLACKLISTED_IPS contains the attacker IP addresses that was used for the demo and this is to be blocked.
# The blackhole_routing decorator checks the IP address of the incoming request against this list.
# If the IP address is found in the blacklist, the request is aborted with a 404 error, simulating that the resource does not exist.

def blackhole_routing(func):
    def wrapper(*args, **kwargs):
        if request.remote_addr in BLACKLISTED_IPS:
            abort(404)  # You can use any status code here. 404 makes it look like the resource doesn't exist
        return func(*args, **kwargs)
    return wrapper

@app.route('/blackhole')
@blackhole_routing
def home():
    return "Welcome to the home page."

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
