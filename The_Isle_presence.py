
from __future__ import annotations

import re
import time
import os
import sys
import threading
import ctypes
import ctypes.wintypes
from datetime import datetime
from pathlib import Path

missing = []
try:
    from pypresence import Presence
except ImportError:
    missing.append("pypresence")

try:
    import psutil
except ImportError:
    missing.append("psutil")

try:
    import pystray
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    missing.append("pystray pillow")

if missing:
    print("[ERROR] Missing dependencies. Run:")
    print(f"        pip install {' '.join(missing)}")
    input("Press Enter to exit...")
    sys.exit(1)

import config


GAME_EXE = "TheIsleClient-Win64-Shipping.exe"
LOG_PATH  = Path(os.environ.get("LOCALAPPDATA", "")) / "TheIsle" / "Saved" / "Logs" / "TheIsle.log"


RE_LOADMAP     = re.compile(r"LogLoad: LoadMap: ([\d\.]+:?\d*)/Game/TheIsle/Maps/Game/(\w+)/\w+")
RE_TITLE_MAP   = re.compile(r"LogLoad: LoadMap: /Game/TheIsle/Maps/TitleMap")
RE_SPAWN       = re.compile(r"LogPlayerController: Verbose: ClientRestart_Implementation BP_([A-Za-z]+)_C_\d+")
RE_SAVE_PATH   = re.compile(r"LogTemp: Save File Path: .+/Prelobby/TempData_(.+?)(?:_Storage|-Storage)?\.bin")
RE_CLASSNAME   = re.compile(r"LogTemp:\s+ClassName: (\w+)")
RE_GROWTH      = re.compile(r"LogTemp:\s+CurrentGrowth: ([\d.]+)")
RE_HEALTH      = re.compile(r"LogTemp:\s+CurrentHealth: ([\d.]+)")
RE_HUNGER      = re.compile(r"LogTemp:\s+CurrentHunger: ([\d.]+)")
RE_THIRST      = re.compile(r"LogTemp:\s+CurrentThirst: ([\d.]+)")
RE_SAFE_LOG    = re.compile(r"LogTemp:\s+bWasSafeLog: (true|false)")
RE_TIME_OF_DAY = re.compile(r"LogTemp: Verbose: Time of Day (\w+)")



DIET = {
    
    "Allosaurus":        "\U0001f969",
    "Austroraptor":      "\U0001f969",
    "Baryonyx":          "\U0001f969",
    "Carnotaurus":       "\U0001f969",
    "Ceratosaurus":      "\U0001f969",
    "Deinosuchus":       "\U0001f969",
    "Dilophosaurus":     "\U0001f969",
    "Herrerasaurus":     "\U0001f969",
    "Tyrannosaurus":     "\U0001f969",
    "Troodon":           "\U0001f969",
    "Omniraptor":        "\U0001f969",
    "Pteranodon":        "\U0001f969",
    "Quetzalcoatlus":    "\U0001f969",
    
    "Beipiaosaurus":     "\U0001f356",
    "Gallimimus":        "\U0001f356",
    "Oviraptor":         "\U0001f356",
    
    "Avaceratops":       "\U0001f33f",
    "Diabloceratops":    "\U0001f33f",
    "Dryosaurus":        "\U0001f33f",
    "Hypsilophodon":     "\U0001f33f",
    "Kentrosaurus":      "\U0001f33f",
    "Maiasaura":         "\U0001f33f",
    "Pachycephalosaurus":"\U0001f33f",
    "Stegosaurus":       "\U0001f33f",
    "Tenontosaurus":     "\U0001f33f",
    "Triceratops":       "\U0001f33f",
}



TIME_EMOJI = {
    "morning":   "\U0001f305",
    "afternoon": "\u2600\ufe0f",
    "evening":   "\U0001f306",
    "night":     "\U0001f319",
}



class GameState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.connected   = False
        self.server_ip   = None
        self.server_name = None
        self.dino        = None
        self.growth      = None
        self.health      = None
        self.hunger      = None
        self.thirst      = None
        self.time_of_day = None
        self.spawn_time  = None
        self._pending    = {}

    def commit_save(self):
        p = self._pending
        if "ClassName"     in p: self.dino   = p["ClassName"]
        if "CurrentGrowth" in p: self.growth = p["CurrentGrowth"]
        if "CurrentHealth" in p: self.health = p["CurrentHealth"]
        if "CurrentHunger" in p: self.hunger = p["CurrentHunger"]
        if "CurrentThirst" in p: self.thirst = p["CurrentThirst"]
        self._pending = {}

    def rpc_details(self):
        if not self.connected:
            return "In menus"
        if not self.dino:
            return "Selecting dinosaur..."
        diet   = DIET.get(self.dino, "")
        prefix = f"{diet} " if diet else ""
        if not self.growth:
            return f"{prefix}{self.dino}"
        g = float(self.growth)
        if g >= 1.0:
            return f"{prefix}{self.dino}  \u00b7  Elder"
        return f"{prefix}{self.dino}  \u00b7  {g*100:.0f}% growth"

    def rpc_state(self):
        """Server name — shown with 👥 icon below the timer."""
        if not self.connected or not self.server_name:
            return None
        name = self.server_name.replace("_", " ")

        for sep in [" - ", " | "]:
            if sep in name:
                name = name[:name.index(sep)]
                break
        name = name.strip()
        if len(name) > 128:
            name = name[:127] + "\u2026"
        return name

    def rpc_small_image(self):
        """Time of day as small image key — upload morning/afternoon/evening/night to Discord app assets."""
        if self.time_of_day:
            return self.time_of_day.lower()
        return None

    def rpc_small_text(self):
        """Tooltip shown when hovering the small image."""
        if self.time_of_day:
            emoji = TIME_EMOJI.get(self.time_of_day.lower(), "")
            return f"{emoji} {self.time_of_day.capitalize()}" if emoji else self.time_of_day.capitalize()
        return None

    def rpc_large_text(self):
        if self.health and self.hunger and self.thirst:
            return (f"HP {float(self.health)*100:.0f}%  "
                    f"Hunger {float(self.hunger)*100:.0f}%  "
                    f"Thirst {float(self.thirst)*100:.0f}%")
        return "The Isle \u2014 EVRIMA"

    def rpc_image(self):
        return self.dino.lower() if self.dino else config.FALLBACK_IMAGE

    def tray_tooltip(self):
        if not self.connected:
            return "The Isle \u2014 In menus"
        parts = ["The Isle"]
        if self.dino:
            pct = f" {float(self.growth)*100:.0f}%" if self.growth else ""
            parts.append(f"{self.dino}{pct}")
        if self.time_of_day:
            parts.append(self.time_of_day.capitalize())
        return "  \u00b7  ".join(parts)

    def tray_line1(self):
        return self.rpc_details()

    def tray_line2(self):
        return self.rpc_state() or "Not connected"



def process_line(line, state):
    if RE_TITLE_MAP.search(line):
        if state.connected:
            state.reset()
            log(f"Disconnected \u2014 back in menus")
            return True
        return False

    m = RE_LOADMAP.search(line)
    if m:
        state.reset()
        state.connected  = True
        state.server_ip  = m.group(1)
        state.spawn_time = time.time()
        log(f"Connected to {state.server_ip}")
        return True

    if not state.connected:
        return False

    m = RE_SPAWN.search(line)
    if m:
        new_dino = m.group(1)
        if new_dino != state.dino:
            state.dino       = new_dino
            state.spawn_time = time.time()
            state.growth     = None
            state.health     = None
            state.hunger     = None
            state.thirst     = None
            log(f"Spawned as: {state.dino}")
            return True

    m = RE_SAVE_PATH.search(line)
    if m and state.server_name != m.group(1):
        state.server_name = m.group(1)
        return True

    for pattern, key in [
        (RE_CLASSNAME, "ClassName"),
        (RE_GROWTH,    "CurrentGrowth"),
        (RE_HEALTH,    "CurrentHealth"),
        (RE_HUNGER,    "CurrentHunger"),
        (RE_THIRST,    "CurrentThirst"),
    ]:
        m = pattern.search(line)
        if m:
            state._pending[key] = m.group(1)

    m = RE_SAFE_LOG.search(line)
    if m:
        state.commit_save()
        kind = "Safe-log" if m.group(1) == "true" else "Autosave"
        pct  = f"{float(state.growth)*100:.1f}%" if state.growth else "?"
        log(f"{kind}: {state.dino}, growth={pct}")
        return True

    m = RE_TIME_OF_DAY.search(line)
    if m:
        print(f"[DEBUG] Time of day line seen: {m.group(1)} (current: {state.time_of_day})")
        if m.group(1) != state.time_of_day:
            state.time_of_day = m.group(1)
            log(f"Time of day: {state.time_of_day}")
            return True

    return False




def tail_log(path):
    log(f"Waiting for log file...")
    while not path.exists():
        time.sleep(2)
    log(f"Log found \u2014 reading from start...")
    last_size = 0
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            yield line
        last_size = f.tell()
        log(f"Caught up. Watching for new lines.\n")
        while True:
            line = f.readline()
            if line:
                last_size = f.tell()
                yield line
            else:
                time.sleep(0.5)
                try:
                    if path.stat().st_size < last_size:
                        log(f"Log reset \u2014 game restarted")
                        break
                except FileNotFoundError:
                    time.sleep(2)
                    break



def push_rpc(rpc, state):
    kwargs = {
        "details":     state.rpc_details(),
        "large_image": state.rpc_image(),
        "large_text":  state.rpc_large_text(),
    }
    s = state.rpc_state()
    if s:
        kwargs["state"] = s
    si = state.rpc_small_image()
    if si:
        kwargs["small_image"] = si
        kwargs["small_text"]  = state.rpc_small_text() or ""
    if state.spawn_time and state.connected:
        kwargs["start"] = int(state.spawn_time)


    if state.connected and state.server_name:
        kwargs["party_id"] = "isle"
    try:
        rpc.update(**kwargs)
    except Exception as e:
        log(f"RPC update error: {e}")


def watch_process(stop_event):
    """Exit the app cleanly when The Isle process is gone."""
    was_running = False
    while not stop_event.is_set():
        running = any(p.name() == GAME_EXE for p in psutil.process_iter(["name"]))
        if was_running and not running:
            log("Game process ended \u2014 exiting.")
            time.sleep(1)
            os._exit(0)
        was_running = running
        stop_event.wait(3)



_console_visible = False

kernel32 = ctypes.windll.kernel32
user32 = ctypes.windll.user32

def show_console():
    global _console_visible

    if _console_visible:
        return

    kernel32.AllocConsole()

    sys.stdout = open("CONOUT$", "w", encoding="utf-8")
    sys.stderr = open("CONOUT$", "w", encoding="utf-8")
    sys.stdin  = open("CONIN$", "r", encoding="utf-8")

    hwnd = kernel32.GetConsoleWindow()

    if hwnd:
        user32.ShowWindow(hwnd, 5)

    _console_visible = True

    print("=" * 55)
    print("  The Isle  Discord Rich Presence Companion")
    print("=" * 55)
    print("\n")
    log("Console opened")


def hide_console():
    global _console_visible

    if not _console_visible:
        return

    hwnd = kernel32.GetConsoleWindow()

    if hwnd:
        user32.ShowWindow(hwnd, 0)

    try:
        sys.stdout.close()
        sys.stderr.close()
        sys.stdin.close()
    except Exception:
        pass

    sys.stdout = None
    sys.stderr = None
    sys.stdin = None

    kernel32.FreeConsole()

    _console_visible = False


def toggle_console(icon=None, item=None):
    if _console_visible:
        hide_console()
    else:
        show_console()



def make_tray_image():
    """Create a cleaner dinosaur footprint tray icon."""
    size = 64

    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    
    d.ellipse((0, 0, size - 1, size - 1), fill=(28, 28, 28, 255))

    green = (95, 220, 110, 255)
    dark  = (45, 120, 55, 255)

    
    d.ellipse((16, 28, 48, 54), fill=green)

    
    d.polygon([
        (14, 30),
        (10, 16),
        (18, 8),
        (24, 20),
        (22, 34)
    ], fill=green)

    
    d.polygon([
        (28, 24),
        (26, 8),
        (32, 2),
        (38, 8),
        (36, 24)
    ], fill=green)

    
    d.polygon([
        (42, 34),
        (40, 20),
        (46, 8),
        (54, 16),
        (50, 30)
    ], fill=green)

    
    claw = (220, 255, 220, 255)

    d.polygon([(16, 8), (18, 0), (21, 10)], fill=claw)
    d.polygon([(32, 1), (34, -6), (37, 4)], fill=claw)
    d.polygon([(46, 8), (49, 0), (52, 10)], fill=claw)

    
    d.arc((16, 28, 48, 54), start=200, end=340, fill=dark, width=3)

    return img


def build_menu(state):
    def _menu():
        console_label = "Hide Console" if _console_visible else "Show Console"
        return (
            pystray.MenuItem(state.tray_line1(), None, enabled=False),
            pystray.MenuItem(state.tray_line2(), None, enabled=False),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem(console_label, toggle_console),
            pystray.MenuItem("Exit", lambda icon, item: os._exit(0)),
        )
    return _menu


def run_tray(state, stop_event):
    icon = pystray.Icon(
        "the_isle_presence",
        make_tray_image(),
        title=state.tray_tooltip(),
        menu=pystray.Menu(build_menu(state)),
    )

    
    def refresh_tooltip():
        while not stop_event.is_set():
            icon.title = state.tray_tooltip()
            stop_event.wait(5)

    t = threading.Thread(target=refresh_tooltip, daemon=True)
    t.start()

    icon.run()




def log(msg):
    text = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"

    try:
        if _console_visible and sys.stdout:
            sys.stdout.write(text + "\n")
            sys.stdout.flush()
    except Exception:
        pass




def main():
    

    if config.DISCORD_APP_ID == "YOUR_APP_ID_HERE":
        print("\n[ERROR] Set your Discord App ID in config.py first!")
        print("  1. Go to https://discord.com/developers/applications")
        print("  2. Create an app, copy the Application ID")
        print("  3. Paste it into config.py")
        input("\nPress Enter to exit...")
        sys.exit(1)

    
    log("Connecting to Discord...")
    rpc = None
    while rpc is None:
        try:
            rpc = Presence(config.DISCORD_APP_ID)
            rpc.connect()
            log("Discord connected!")
        except Exception as e:
            log(f"Discord not available ({e}) \u2014 retrying in 10s...")
            rpc = None
            time.sleep(10)

    state     = GameState()
    stop_evt  = threading.Event()

    push_rpc(rpc, state)

    
    hide_console()

    
    threading.Thread(target=watch_process, args=(stop_evt,), daemon=True).start()

    
    def reader_loop():
        while True:
            for line in tail_log(LOG_PATH):
                if process_line(line, state):
                    push_rpc(rpc, state)

    threading.Thread(target=reader_loop, daemon=True).start()

    
    run_tray(state, stop_evt)


def launcher_mode():
 
    import subprocess

    exe = sys.executable

    CREATE_NO_WINDOW = 0x08000000
    DETACHED_PROCESS = 0x00000008

    
    subprocess.Popen(
        [exe],
        creationflags=CREATE_NO_WINDOW | DETACHED_PROCESS,
        close_fds=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    
    subprocess.Popen(
        sys.argv[1:],
        close_fds=True,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    os._exit(0)


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        launcher_mode()

    try:
        main()
    except KeyboardInterrupt:
        log("Stopped.")