# Installation guide

## Windows one-click setup

Install Python 3.10 or later and [Cloudflare Tunnel (`cloudflared`)](https://developers.cloudflare.com/tunnel/downloads/) once, extract the archive, then double-click `run.bat`. The script creates a local `.venv`, installs `requirements.txt`, starts Flask, and starts a temporary HTTPS Quick Tunnel. Copy the `https://…trycloudflare.com` link shown in the Cloudflare window to the phone. Keep both windows open during the demo. The tunnel is temporary and anyone with its link can access this read-only demo while it is running; stop it with Ctrl+C in the Cloudflare window. Quick Tunnels are for testing and development ([Cloudflare guide](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/)).

## Manual setup

From the project root:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python backend\app.py
```

Open `http://127.0.0.1:5000`. If PowerShell blocks activation, use `run.bat` or activate the environment from Command Prompt instead.

## Phone preview and AR using HTTPS

Install `cloudflared` on the PC once, then run `run.bat`. It starts the app and a temporary HTTPS tunnel automatically. Open the `https://…trycloudflare.com` URL printed in the separate Cloudflare window. The phone does not need to be on the same Wi-Fi. Keep the server and tunnel windows open; press Ctrl+C in the tunnel window to end public access. Anyone who has the temporary URL can reach the demo, so share it only with intended viewers.

If `cloudflared` is not installed, `run.bat` reports that and still starts the site for a same-Wi-Fi HTTP preview. The launcher prints a `PHONE URL` such as `http://192.168.1.23:5000`; do not use `127.0.0.1` on the phone. Plain LAN HTTP is suitable for the website preview but not WebXR AR.
