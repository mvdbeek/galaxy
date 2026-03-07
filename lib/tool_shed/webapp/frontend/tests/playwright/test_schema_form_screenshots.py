"""Playwright tests that render Galaxy tool parameter forms from JSON Schema
and capture screenshots.

Usage:
    cd lib/tool_shed/webapp/frontend
    python tests/playwright/test_schema_form_screenshots.py

Requires:
    - Node.js and pnpm (for Vite dev server)
    - Python playwright package
    - Chromium browser cached at /root/.cache/ms-playwright/
"""

import json
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
SCHEMAS_FILE = SCRIPT_DIR / "test_tool_schemas.json"
CHROMIUM_PATH = os.environ.get(
    "PLAYWRIGHT_CHROMIUM_PATH",
    os.path.expanduser("~/.cache/ms-playwright/chromium-1194/chrome-linux/chrome"),
)
VITE_PORT = 5199
VITE_URL = f"http://localhost:{VITE_PORT}"


def start_vite_server():
    """Start the Vite dev server for the test harness."""
    env = os.environ.copy()
    proc = subprocess.Popen(
        ["npx", "vite", "--config", str(SCRIPT_DIR / "vite.config.ts"), "--port", str(VITE_PORT)],
        cwd=str(FRONTEND_DIR),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    # Wait for server to be ready
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
    """Take screenshots of all tool schema forms."""
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

    with open(SCHEMAS_FILE) as f:
        schemas = json.load(f)

    tool_ids = list(schemas.keys())
    print(f"Tools to screenshot: {tool_ids}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=CHROMIUM_PATH,
        )
        context = browser.new_context(
            viewport={"width": 900, "height": 800},
            device_scale_factor=2,
        )
        page = context.new_page()

        # Load the test harness page
        page.goto(f"{VITE_URL}/test-harness.html", wait_until="networkidle")
        page.wait_for_selector(".tool-card", timeout=15000)
        # Give JsonForms a moment to fully render
        page.wait_for_timeout(1000)

        # Full page screenshot
        full_path = SCREENSHOTS_DIR / "all_tools_overview.png"
        page.screenshot(path=str(full_path), full_page=True)
        print(f"  Saved full page: {full_path}")

        # Individual tool screenshots
        for tool_id in tool_ids:
            selector = f"#tool-{tool_id}"
            element = page.query_selector(selector)
            if element:
                path = SCREENSHOTS_DIR / f"tool_{tool_id}.png"
                element.screenshot(path=str(path))
                print(f"  Saved: {path}")
            else:
                print(f"  WARNING: Could not find element for {tool_id}")

        browser.close()


def main():
    print("=" * 60)
    print("Galaxy Tool Schema Form Playwright Screenshots")
    print("=" * 60)

    # Check prerequisites
    if not Path(CHROMIUM_PATH).exists():
        print(f"ERROR: Chromium not found at {CHROMIUM_PATH}")
        sys.exit(1)

    if not SCHEMAS_FILE.exists():
        print(f"ERROR: Schemas file not found at {SCHEMAS_FILE}")
        sys.exit(1)

    print("\n1. Starting Vite dev server...")
    vite_proc = start_vite_server()

    try:
        print("\n2. Taking screenshots...")
        take_screenshots()
        print("\n3. Done! Screenshots saved to:")
        for f in sorted(SCREENSHOTS_DIR.glob("*.png")):
            print(f"   {f}")
    finally:
        print("\n4. Stopping Vite server...")
        vite_proc.send_signal(signal.SIGTERM)
        vite_proc.wait(timeout=5)


if __name__ == "__main__":
    main()
