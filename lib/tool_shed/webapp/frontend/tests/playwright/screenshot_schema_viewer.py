"""Take a screenshot of the standalone schema-viewer app.

Usage:
    cd lib/tool_shed/webapp/frontend
    python tests/playwright/screenshot_schema_viewer.py
"""

import os
import signal
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).parent
FRONTEND_DIR = SCRIPT_DIR.parent.parent
SCREENSHOTS_DIR = SCRIPT_DIR / "screenshots"
CHROMIUM_PATH = os.environ.get(
    "PLAYWRIGHT_CHROMIUM_PATH",
    os.path.expanduser("~/.cache/ms-playwright/chromium-1194/chrome-linux/chrome"),
)
VITE_PORT = 5199
VITE_URL = f"http://localhost:{VITE_PORT}"


def start_vite_server():
    env = os.environ.copy()
    proc = subprocess.Popen(
        ["npx", "vite", "--config", str(SCRIPT_DIR / "vite.config.ts"), "--port", str(VITE_PORT)],
        cwd=str(FRONTEND_DIR),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    start = time.time()
    while time.time() - start < 30:
        try:
            line = proc.stdout.readline()
            if line:
                print(f"  [vite] {line.rstrip()}")
            if f"localhost:{VITE_PORT}" in line or f"127.0.0.1:{VITE_PORT}" in line:
                print("  Vite server is ready!")
                return proc
        except Exception:
            pass
        if proc.poll() is not None:
            raise RuntimeError("Vite server exited unexpectedly")
        time.sleep(0.2)
    raise TimeoutError("Vite server did not start within 30s")


def take_screenshots():
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=CHROMIUM_PATH)
        context = browser.new_context(viewport={"width": 1200, "height": 900}, device_scale_factor=2)
        page = context.new_page()

        # Load schema viewer - empty state
        page.goto(f"{VITE_URL}/schema-viewer.html", wait_until="networkidle")
        page.wait_for_timeout(500)
        path = SCREENSHOTS_DIR / "schema_viewer_empty.png"
        page.screenshot(path=str(path), full_page=True)
        print(f"  Saved: {path}")

        # Click on "color_param" example chip
        page.click("button.chip >> text=color_param")
        page.wait_for_timeout(1000)
        path = SCREENSHOTS_DIR / "schema_viewer_color_param.png"
        page.screenshot(path=str(path), full_page=True)
        print(f"  Saved: {path}")

        # Click on "disambiguate_cond" example chip
        page.click("button.chip >> text=disambiguate_cond")
        page.wait_for_timeout(1000)
        path = SCREENSHOTS_DIR / "schema_viewer_disambiguate_cond.png"
        page.screenshot(path=str(path), full_page=True)
        print(f"  Saved: {path}")

        browser.close()


def main():
    print("=" * 60)
    print("Galaxy Schema Viewer - Screenshot Capture")
    print("=" * 60)

    if not Path(CHROMIUM_PATH).exists():
        print(f"ERROR: Chromium not found at {CHROMIUM_PATH}")
        sys.exit(1)

    print("\n1. Starting Vite dev server...")
    vite_proc = start_vite_server()

    try:
        print("\n2. Taking screenshots...")
        take_screenshots()
        print("\n3. Done! Screenshots:")
        for f in sorted(SCREENSHOTS_DIR.glob("schema_viewer_*.png")):
            print(f"   {f}")
    finally:
        print("\n4. Stopping Vite server...")
        vite_proc.send_signal(signal.SIGTERM)
        vite_proc.wait(timeout=5)


if __name__ == "__main__":
    main()
