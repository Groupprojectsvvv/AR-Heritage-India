"""Start the local Flask server, wait until it responds, then open the site."""
import socket
import threading
import time
import urllib.request
import webbrowser
from werkzeug.serving import make_server

HOST = "0.0.0.0"
PORT = 5000
LOCAL_URL = f"http://127.0.0.1:{PORT}"

from app import app

server_holder = []
startup_error = []
ready = threading.Event()

def serve():
    try:
        server = make_server(HOST, PORT, app, threaded=True)
        server_holder.append(server)
    except OSError as error:
        startup_error.append(error)
    finally:
        ready.set()
    if server_holder:
        server_holder[0].serve_forever()

thread = threading.Thread(target=serve, name="ar-heritage-flask", daemon=True)
thread.start()
ready.wait(timeout=5)
if startup_error:
    print(f"Could not start the site on port {PORT}: {startup_error[0]}")
    print("Close the other program using this port, then try again.")
    raise SystemExit(1)
if not server_holder:
    print("The Flask server did not start in time.")
    raise SystemExit(1)

for _ in range(30):
    try:
        with urllib.request.urlopen(f"{LOCAL_URL}/api/health", timeout=1) as response:
            if response.status == 200:
                break
    except OSError:
        time.sleep(0.5)
else:
    server_holder[0].shutdown()
    print("The site did not become ready. Check Python and Flask installation.")
    raise SystemExit(1)

print(f"AR Heritage India is ready at {LOCAL_URL}")
print("PHONE URL (same Wi-Fi): open the exact address below on your phone.")
print("Do not use 127.0.0.1 on the phone; that address means the phone itself.")
phone_addresses = set()
try:
    # A UDP connect selects the active outbound interface without sending a packet.
    probe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        probe.connect(("192.0.2.1", 80))
        address = probe.getsockname()[0]
        if not address.startswith("127."):
            phone_addresses.add(address)
    finally:
        probe.close()
except OSError:
    pass
if not phone_addresses:
    try:
        phone_addresses.update(address for address in {item[4][0] for item in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)} if not address.startswith("127."))
    except OSError:
        pass
for address in sorted(phone_addresses):
    print(f"  http://{address}:{PORT}")
if not phone_addresses:
    print("  Run ipconfig and use this computer's Wi-Fi IPv4 Address with :5000")
print("Keep this window open. Press Ctrl+C here to stop the server.")
webbrowser.open(LOCAL_URL)

try:
    while thread.is_alive():
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping AR Heritage India…")
    server_holder[0].shutdown()
