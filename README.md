# 🦕 The Isle Presence

> Discord Rich Presence companion for **The Isle — EVRIMA**

![Banner](images/banner.png)

Automatically displays your current dinosaur, server, growth stage, and time of day in your Discord profile — with no memory reading, no anti-cheat risk, and no game file modifications.

---

## Preview

![Discord presence card showing a Troodon at 36% growth](images/preview_card.png)

---

## Features

- 🦕 **Dinosaur species** — detected automatically at spawn
- 📈 **Growth percentage** — updated every autosave, shows `Elder` at cap
- 🥩🌿🍖 **Diet indicator** — carnivore, herbivore, or omnivore emoji
- 🌙 **Time of day** — shown as a small image icon (morning / afternoon / evening / night)
- 🖥️ **Server name** — trimmed cleanly to just the server's actual name
- ⏱️ **Elapsed timer** — resets on each new life
- 🔇 **Runs silently** — lives in your system tray, no console window
- 🎮 **Steam integration** — launches automatically with the game, closes when you quit

---

## How It Works

The Isle Presence reads The Isle's log file in real time — no memory reading, no DLL injection, and nothing that EasyAntiCheat can object to. A small tweak to `Engine.ini` enables the verbose logging the app depends on, which the installer handles automatically.

![Diagram showing log file → app → Discord](images/diagram.png)

---

## Installation

### Requirements
- Windows 10 or later
- The Isle (EVRIMA) on Steam
- Discord desktop app

### Steps

1. Download the latest release from the [Releases](../../releases) page
2. Run `The_Isle_presence_installer.exe`
3. Follow the installer steps — it will:
   - Patch your `Engine.ini` automatically
   - Install the companion app
   - Configure Steam launch options (optional, recommended)

![Installer screenshot — welcome page](images/installer_welcome.png)
![Installer screenshot — Engine.ini patch page](images/installer_patch.png)
![Installer screenshot — install type selection](images/installer_type.png)
![Installer screenshot — Steam configuration page](images/installer_steam.png)

> ⚠️ **Do not install inside The Isle's game folder.** EasyAntiCheat monitors processes launched from the game directory. Install anywhere else — the default (`C:\The_Isle_presence`) is fine.

---

## Manual Setup (without installer)

If you prefer to set things up yourself:

### 1. Patch Engine.ini

Add the following to:
```
%LOCALAPPDATA%\TheIsle\Saved\Config\WindowsClient\Engine.ini
```

```ini
[Core.Log]
LogTemp=VeryVerbose
LogGameMode=VeryVerbose
LogSpawn=VeryVerbose
LogPlayerController=VeryVerbose
LogConfig=VeryVerbose
LogTheIsle=VeryVerbose
LogTheIsleServer=VeryVerbose
LogTheIsleAdmin=VeryVerbose
LogTheIsleJoinData=VeryVerbose
LogTheIsleChatData=VeryVerbose
LogTheIsleKillData=VeryVerbose
LogTheIsleCommandData=VeryVerbose
LogTheIsleAntiCheat=VeryVerbose
```

Then lock the file as read-only so the game can't reset it on exit:
```
Right-click Engine.ini → Properties → check Read-only → OK
```

### 2. Create a Discord Application

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Click **New Application** and name it `The Isle`
3. Copy the **Application ID** from General Information
4. Open `config.py` and paste it in:
   ```python
   DISCORD_APP_ID = "your_id_here"
   ```

### 3. Upload Image Assets

In your Discord application, go to **Rich Presence → Art Assets** and upload:

| Key name | Image |
|---|---|
| `isle` | Fallback image shown in menus |
| `allosaurus` | Allosaurus portrait |
| `austroraptor` | Austroraptor portrait |
| `baryonyx` | Baryonyx portrait |
| `carnotaurus` | Carnotaurus portrait |
| `ceratosaurus` | Ceratosaurus portrait |
| `deinosuchus` | Deinosuchus portrait |
| `diabloceratops` | Diabloceratops portrait |
| `dilophosaurus` | Dilophosaurus portrait |
| `dryosaurus` | Dryosaurus portrait |
| `gallimimus` | Gallimimus portrait |
| `herrerasaurus` | Herrerasaurus portrait |
| `hypsilophodon` | Hypsilophodon portrait |
| `kentrosaurus` | Kentrosaurus portrait |
| `maiasaura` | Maiasaura portrait |
| `omniraptor` | Omniraptor portrait |
| `oviraptor` | Oviraptor portrait |
| `pachycephalosaurus` | Pachycephalosaurus portrait |
| `pteranodon` | Pteranodon portrait |
| `pterodactylus` | Pterodactylus portrait |
| `stegosaurus` | Stegosaurus portrait |
| `tenontosaurus` | Tenontosaurus portrait |
| `triceratops` | Triceratops portrait |
| `troodon` | Troodon portrait |
| `tyrannosaurus` | Tyrannosaurus portrait |
| `morning` | Time of day icon — morning |
| `afternoon` | Time of day icon — afternoon |
| `evening` | Time of day icon — evening |
| `night` | Time of day icon — night |

### 4. Steam Launch Options (Auto-launch)

In Steam, right-click **The Isle → Properties → Launch Options** and paste:
```
"C:\The_Isle_presence\The_Isle_presence.exe" %command%
```

Update the path to wherever you installed the app.

### 5. Run

Double-click `The_Isle_presence.exe`. The app will appear in your system tray.

---

## Usage

Once running, the app lives silently in your system tray.

![System tray icon](images/tray_icon.png)

**Right-click the tray icon** for options:

| Option | Description |
|---|---|
| Show Console | Opens the log output window for debugging |
| Hide Console | Hides the console window again |
| Exit | Closes the app |

The presence updates automatically:
- **On spawn** — dino and server detected immediately
- **Every autosave** (~every 2 minutes) — growth, health, hunger, thirst updated
- **On safe-log** — final stats saved
- **Periodically** — time of day updated as in-game time progresses

---

## Presence Layout

```
[Dino portrait]   The Isle
      [🌙]        🥩 Troodon  ·  36% growth
                  ⏱ 1:46
                  👥 Petits Pieds EU
```

---

## Anti-Cheat

The Isle uses **EasyAntiCheat**. This app is safe because it:

- ✅ Only reads the game's log file — no process memory access
- ✅ Makes no game file modifications
- ✅ Does not inject code or DLLs into the game process
- ✅ Must not be installed inside the game's directory (installer enforces this)

---

## Troubleshooting

**Presence shows "In menus" even in-game**
- Make sure `Engine.ini` was patched and is locked read-only
- Check the console (right-click tray → Show Console) for errors

**Dino not detected**
- Make sure `LogPlayerController=VeryVerbose` is in your `Engine.ini`
- The dino is detected at spawn — if you joined mid-session before the app started, reconnect

**Growth not updating**
- Growth updates on autosave (roughly every 2 minutes) and on safe-log
- It won't show until the first autosave after you spawn

**Server name missing**
- Some servers may format their names differently — open an issue with your server name and we'll add support

**Steam isn't auto-launching the app**
- Verify the path in Steam launch options matches exactly where you installed the exe
- Make sure you're using the `--onedir` build, not the standalone `--onefile` exe

---

## Building from Source

```bash
git clone https://github.com/yourusername/the-isle-presence
cd the-isle-presence
pip install -r requirements.txt
python The_Isle_presence.py
```

To build the exe:
```bash
# Standalone (onefile)
pyinstaller --onefile --noconsole --name The_Isle_presence The_Isle_presence.py

# Steam auto-launch (onedir)
pyinstaller --onedir --noconsole --name The_Isle_presence The_Isle_presence.py
```

---

## Contributing

Pull requests welcome. If you find a new log pattern that exposes useful data, open an issue with a sample log snippet and I'll add support.

---

## License

MIT — do whatever you want with it.

---

*Not affiliated with Afterthought LLC or The Isle development team.*
