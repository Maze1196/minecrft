from pyngrok import ngrok, conf
import json
import time

# Load configuration from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

def set_auth_token(auth_token):
    """Set the Ngrok authentication token."""
    conf.get_default().auth_token = auth_token
    print("Auth token set successfully.")

def create_tcp_tunnel(port):
    """Create a TCP tunnel on the specified port."""
    tcp_tunnel = ngrok.connect(port, "tcp")
    public_url = tcp_tunnel.public_url
    print(f"Public TCP URL: {public_url}")
    return public_url

# Set the Ngrok auth token from config.json
set_auth_token(config["authtoken"])

# Open a TCP tunnel on the port specified in config.json
public_url = create_tcp_tunnel(config["port"])

# Keep the script running indefinitely
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTerminating tunnel...")

# Disconnect the tunnel when done
ngrok.disconnect(public_url)