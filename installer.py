
from __future__ import annotations
import os, sys, re, shutil, winreg
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


BG      = "#1a1a1a"
PANEL   = "#242424"
CARD    = "#2c2c2c"
BTN     = "#383838"
BTN_H   = "#464646"
ACC     = "#4e9040"
ACC_H   = "#5cb34a"
TEXT    = "#e8e8e8"
DIM     = "#7a7a7a"
ERR     = "#c0392b"
OK_C    = "#27ae60"
WARN    = "#e67e22"

FT      = ("Segoe UI", 10)
FT_B    = ("Segoe UI", 10, "bold")
FT_H    = ("Segoe UI", 14, "bold")
FT_SH   = ("Segoe UI",  9)
FT_MONO = ("Consolas",  9)


ISLE_APP_ID = "376210"

ENGINE_INI_PATH = (
    Path(os.environ.get("LOCALAPPDATA", "")) /
    "TheIsle" / "Saved" / "Config" / "WindowsClient" / "Engine.ini"
)

ENGINE_INI = """\
;;METADATA=(Diff=true, UseCommands=true)

[GameNetDriver StatelessConnectHandlerComponent]
CachedClientID=462

[Core.Log]
LogAPICall=VeryVerbose
LogAction=VeryVerbose
LogActivelyUploadedMessage=VeryVerbose
LogAffine=VeryVerbose
LogAffineTransform=VeryVerbose
LogAffineTransformImpl=VeryVerbose
LogAndRtpDumps=VeryVerbose
LogAqEAsaqwp6S9rUChZTEirLQc=VeryVerbose
LogArbitraryPolicyPerDownload=VeryVerbose
LogArrow=VeryVerbose
LogAudioPowerLevel=VeryVerbose
LogBKIXsm20XyV=VeryVerbose
LogBackgroundServiceEvent=VeryVerbose
LogBackgroundServiceEventOnCoreThread=VeryVerbose
LogBase=VeryVerbose
LogBuffer=VeryVerbose
LogBwBiasFactor=VeryVerbose
LogCallback=VeryVerbose
LogCameraTransform=VeryVerbose
LogCameraTransformImpl=VeryVerbose
LogCapsule=VeryVerbose
LogCapturePipeline=VeryVerbose
LogCategory=VeryVerbose
LogCategoryListRow=VeryVerbose
LogCircle=VeryVerbose
LogClose=VeryVerbose
LogCode=VeryVerbose
LogCollapseAll=VeryVerbose
LogCollectionAllowed=VeryVerbose
LogCone=VeryVerbose
LogConfigB=VeryVerbose
LogConsoleResponse=VeryVerbose
LogContextANGLE=VeryVerbose
LogContinue=VeryVerbose
LogCountColumn=VeryVerbose
LogCountFormat=VeryVerbose
LogCylinder=VeryVerbose
LogDataDescriptions=VeryVerbose
LogDataFmt=VeryVerbose
LogDataflowNode=VeryVerbose
LogDecode=VeryVerbose
LogDuration=VeryVerbose
LogEXTContextANGLE=VeryVerbose
LogEe0y8tqxGYry=VeryVerbose
LogEncode=VeryVerbose
LogEndAndStart=VeryVerbose
LogEntries=VeryVerbose
LogEntry=VeryVerbose
LogErrors=VeryVerbose
LogEscalate=VeryVerbose
LogEvent=VeryVerbose
LogEventsAsync=VeryVerbose
LogExpandAll=VeryVerbose
LogExportHistory=VeryVerbose
LogExporter=VeryVerbose
LogFactory=VeryVerbose
LogFactoryManager=VeryVerbose
LogFailedUploadTimeFormat=VeryVerbose
LogFeatureStatus=VeryVerbose
LogField=VeryVerbose
LogFieldName=VeryVerbose
LogFileMessage=VeryVerbose
LogFileUse=VeryVerbose
LogFilename=VeryVerbose
LogFiles=VeryVerbose
LogFilesForAllProfiles=VeryVerbose
LogFilm=VeryVerbose
LogFlocComputedEvent=VeryVerbose
LogFragment=VeryVerbose
LogFrequency=VeryVerbose
LogFrequencyClamped=VeryVerbose
LogFrequencyScaling=VeryVerbose
LogFrequencyValue=VeryVerbose
LogFwdOpCPU=VeryVerbose
LogGLDebugMessage=VeryVerbose
LogGameRoundEnd=VeryVerbose
LogGameRoundStart=VeryVerbose
LogGzipped=VeryVerbose
LogHeaderFormat=VeryVerbose
LogHistoryTabHeading=VeryVerbose
LogIC3lsY8vziRTNYCvOqlQMiM056sUsrEv8bLPLL605S=VeryVerbose
LogINTEL=VeryVerbose
LogInDirectory=VeryVerbose
LogInfoChanged=VeryVerbose
LogInformation=VeryVerbose
LogInterfaceUsage=VeryVerbose
LogInterval=VeryVerbose
LogIsEmpty=VeryVerbose
LogJCbaqckh0CR=VeryVerbose
LogJsConsoleMessages=VeryVerbose
LogKHRContextANGLE=VeryVerbose
LogKillSwitch=VeryVerbose
LogL16Decode=VeryVerbose
LogL16Encode=VeryVerbose
LogL16InitState=VeryVerbose
LogLength=VeryVerbose
LogLevel=VeryVerbose
LogLevelAll=VeryVerbose
LogLevelAudio=VeryVerbose
LogLevelCore=VeryVerbose
LogLevelMediaService=VeryVerbose
LogLevelRTCP=VeryVerbose
LogLevelVideo=VeryVerbose
LogLevelVideoCodec=VeryVerbose
LogLevelWebRTC=VeryVerbose
LogLikelihoodLoss=VeryVerbose
LogLimitInstant=VeryVerbose
LogLimitSustained=VeryVerbose
LogListing=VeryVerbose
LogListingComboButton=VeryVerbose
LogListingModel=VeryVerbose
LogListingPtr=VeryVerbose
LogListingViewModel=VeryVerbose
LogLocalFileLabelFormat=VeryVerbose
LogLocalLogIdFormat=VeryVerbose
LogLocation=VeryVerbose
LogLuvDecode24=VeryVerbose
LogLuvDecode32=VeryVerbose
LogLuvEncode24=VeryVerbose
LogLuvEncode32=VeryVerbose
LogLuvInitState=VeryVerbose
LogLuvSetupDecode=VeryVerbose
LogLuvSetupEncode=VeryVerbose
LogLuvVSetField=VeryVerbose
LogManager=VeryVerbose
LogManagerKeyedService=VeryVerbose
LogMappingContextRedirects=VeryVerbose
LogMessage=VeryVerbose
LogMessageBody=VeryVerbose
LogMessageListRow=VeryVerbose
LogMessageR=VeryVerbose
LogMessages=VeryVerbose
LogMetadataMetrics=VeryVerbose
LogModel=VeryVerbose
LogModule=VeryVerbose
LogMoreActionsLabel=VeryVerbose
LogMraaA5sUEwCzMDrmSo=VeryVerbose
LogMtvrKerSQ0C7KHoukkYzYPsBI0=VeryVerbose
LogName=VeryVerbose
LogNameColumn=VeryVerbose
LogNewFormat=VeryVerbose
LogNode=VeryVerbose
LogNotUploadedMessage=VeryVerbose
LogNotification=VeryVerbose
LogOJ6g4LCQnuijyJhym663eK1cp3SU7KjyYb6PDKImwWaOnMDwkdi=VeryVerbose
LogObject=VeryVerbose
LogObserver=VeryVerbose
LogOnAnonymous=VeryVerbose
LogOnly=VeryVerbose
LogOpCPU=VeryVerbose
LogOpData=VeryVerbose
LogOrientedBox=VeryVerbose
LogOutAllAccounts=VeryVerbose
LogOutFailure=VeryVerbose
LogOutFromCookieCompleted=VeryVerbose
LogOutSuccess=VeryVerbose
LogOwner=VeryVerbose
LogPageHeading=VeryVerbose
LogParams=VeryVerbose
LogParamsElt=VeryVerbose
LogPasswordCaptureTimer=VeryVerbose
LogPath=VeryVerbose
LogPathVariable=VeryVerbose
LogPendingMessage=VeryVerbose
LogPerPolicyApplied=VeryVerbose
LogPerformanceSnapshot=VeryVerbose
LogPlayerDespawn=VeryVerbose
LogPlayerRevive=VeryVerbose
LogPlayerSpawn=VeryVerbose
LogPlayerTakeDamage=VeryVerbose
LogPlayerTick=VeryVerbose
LogPlayerUseAbility=VeryVerbose
LogPlayerUseWeapon=VeryVerbose
LogPortUnreach=VeryVerbose
LogPostEncode=VeryVerbose
LogPreDecode=VeryVerbose
LogPreEncode=VeryVerbose
LogPrefix=VeryVerbose
LogPriority=VeryVerbose
LogPriorityR=VeryVerbose
LogPrivate=VeryVerbose
LogPrivateAPI=VeryVerbose
LogProtocolMessage=VeryVerbose
LogProxySink=VeryVerbose
LogProxySource=VeryVerbose
LogRTLookupRequest=VeryVerbose
LogRTLookupResponse=VeryVerbose
LogRecall=VeryVerbose
LogRecallProtobufs=VeryVerbose
LogRecord=VeryVerbose
LogRecordLocked=VeryVerbose
LogRecordingOnStart=VeryVerbose
LogRecordings=VeryVerbose
LogRecordingsEnabled=VeryVerbose
LogRecordingsFileSelectionCancelled=VeryVerbose
LogRecordingsToggleability=VeryVerbose
LogRecords=VeryVerbose
LogRenderer=VeryVerbose
LogRendererSSE=VeryVerbose
LogReportIdFormat=VeryVerbose
LogRequestTime=VeryVerbose
LogRevOpCPU=VeryVerbose
LogReverse=VeryVerbose
LogSearchLabel=VeryVerbose
LogSegment=VeryVerbose
LogSetupDecode=VeryVerbose
LogSetupEncode=VeryVerbose
LogShapeLibraries=VeryVerbose
LogSideOffset=VeryVerbose
LogSideSlope=VeryVerbose
LogSingleton=VeryVerbose
LogSink=VeryVerbose
LogSize=VeryVerbose
LogSizeBytes=VeryVerbose
LogSoftmax=VeryVerbose
LogSource=VeryVerbose
LogSourceParams=VeryVerbose
LogSourceResult=VeryVerbose
LogSpawnLocations=VeryVerbose
LogSphere=VeryVerbose
LogStart=VeryVerbose
LogStats=VeryVerbose
LogStatsBuffer=VeryVerbose
LogStreamTabHeading=VeryVerbose
LogString=VeryVerbose
LogStringDataflowNode=VeryVerbose
LogSubscribe=VeryVerbose
LogSumExp=VeryVerbose
LogSuppressionInterface=VeryVerbose
LogSync=VeryVerbose
LogText=VeryVerbose
LogTimeColumn=VeryVerbose
LogTimes=VeryVerbose
LogToConsole=VeryVerbose
LogToLin=VeryVerbose
LogToURL=VeryVerbose
LogTransform=VeryVerbose
LogTransformImpl=VeryVerbose
LogTypeColumn=VeryVerbose
LogUnexpectedIPCPostedToBackForwardCachedDocuments=VeryVerbose
LogUnsubscribe=VeryVerbose
LogUpload=VeryVerbose
LogUploadEnabled=VeryVerbose
LogUploadInterval=VeryVerbose
LogUploadTimeFormat=VeryVerbose
LogUploaderImpl=VeryVerbose
LogUraS2sp8a0J7abtCU0GDSmsyIyZ7BJGpWwzqPpMqavKzCDtBG0P=VeryVerbose
LogUserIntoLocalPlatformNode=VeryVerbose
LogV3SwnsDkmgqZgqZgsNSxGrYGuJKluqdGZjK6wqDwrtSnwKiKowq=VeryVerbose
LogVSetField=VeryVerbose
LogVariabilityMaskEy4int2ffS3=VeryVerbose
LogVcqwCHqgmE6pwqwIwuCxKK5qoIq3crtGnfCxZrZAogqElq8wVlq=VeryVerbose
LogVerbosity=VeryVerbose
LogVerifier=VeryVerbose
LogVideoSendStreamConfig=VeryVerbose
LogViewModel=VeryVerbose
LogWAbSINsss0DnbMSi16ik8KwsyJTIBsia4hCZKsbSxBrMHNEMynL=VeryVerbose
LogWarningOnDroppedConnection=VeryVerbose
LogWasmCodes=VeryVerbose
LogWhenMaxObjectLimitExceeded=VeryVerbose
LogWidgetClass=VeryVerbose
LogWireframeOptional=VeryVerbose
LogWithSource=VeryVerbose
LogWrapper=VeryVerbose
LogWrite=VeryVerbose
LogWriteInternal=VeryVerbose
LogWriter=VeryVerbose
LogXNode=VeryVerbose
LogTemp=VeryVerbose
LogGameMode=VeryVerbose
LogSpawn=VeryVerbose
LogPlayerController=VeryVerbose
LogPawn=VeryVerbose
LogActor=VeryVerbose

"""


def res(name: str) -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return base / name



def find_steam_path() -> Path | None:
    candidates = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam", "InstallPath"),
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam",             "InstallPath"),
        (winreg.HKEY_CURRENT_USER,  r"Software\Valve\Steam",             "SteamPath"),
    ]
    for hive, sub, val in candidates:
        try:
            with winreg.OpenKey(hive, sub) as k:
                p = Path(winreg.QueryValueEx(k, val)[0])
                if p.exists():
                    return p
        except Exception:
            pass
    return None


def find_isle_path(steam: Path) -> Path | None:
    libs = [steam]
    vdf = steam / "steamapps" / "libraryfolders.vdf"
    if vdf.exists():
        for m in re.finditer(r'"path"\s+"([^"]+)"',
                             vdf.read_text(encoding="utf-8", errors="ignore")):
            p = Path(m.group(1).replace("\\\\", "\\"))
            if p.exists():
                libs.append(p)
    for lib in libs:
        acf = lib / "steamapps" / f"appmanifest_{ISLE_APP_ID}.acf"
        if acf.exists():
            m = re.search(r'"installdir"\s+"([^"]+)"',
                          acf.read_text(encoding="utf-8", errors="ignore"))
            if m:
                return lib / "steamapps" / "common" / m.group(1)
    return None


def steam_is_running() -> bool:
    try:
        import psutil
        return any(p.name().lower() == "steam.exe"
                   for p in psutil.process_iter(["name"]))
    except Exception:
        return False


def find_localconfigs(steam: Path) -> list[Path]:
    ud = steam / "userdata"
    if not ud.exists():
        return []
    configs = list(ud.glob("*/config/localconfig.vdf"))
    configs.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return configs


def set_launch_options(text: str, app_id: str, opts: str) -> str:
    """Find the app_id block in localconfig.vdf and set/add LaunchOptions."""
    m = re.search(rf'"{re.escape(app_id)}"\s*\n\s*\{{', text)
    if not m:
        raise ValueError(
            f"App {app_id} not found in localconfig.vdf.\n"
            "Launch The Isle at least once through Steam, then retry."
        )
    start = m.end()
    depth, i = 1, start
    while i < len(text) and depth:
        if   text[i] == '{': depth += 1
        elif text[i] == '}': depth -= 1
        i += 1
    section = text[start : i - 1]
    after   = text[i - 1:]

    safe_opts = opts.replace("\\", "\\\\").replace('"', '\\"'  )
    new_line  = f'\t\t\t\t\t\t"LaunchOptions"\t\t"{safe_opts}"'

    lo_pat    = re.compile(r'\s*"LaunchOptions"\s+"(?:[^"\\\\]|\\\\.)*"')

    if lo_pat.search(section):

        replacement = "\n" + new_line
        section = lo_pat.sub(lambda _: replacement, section, count=1)
    else:
        section = section.rstrip() + "\n" + new_line + "\n\t\t\t\t\t"

    return text[:start] + section + after



def ini_is_patched() -> bool:
    try:
        return (ENGINE_INI_PATH.exists() and
                "LogPlayerController=VeryVerbose" in
                ENGINE_INI_PATH.read_text(errors="ignore"))
    except Exception:
        return False


def patch_ini() -> tuple[bool, str]:
    try:
        ENGINE_INI_PATH.parent.mkdir(parents=True, exist_ok=True)
        if ENGINE_INI_PATH.exists():
            ENGINE_INI_PATH.chmod(0o666)
        ENGINE_INI_PATH.write_text(ENGINE_INI, encoding="utf-8")
        ENGINE_INI_PATH.chmod(0o444)
        return True, "Engine.ini written and locked read-only."
    except Exception as e:
        return False, str(e)



def install_onefile(dest: Path) -> tuple[bool, str]:
    try:
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(res("The_Isle_presence.exe"), dest / "The_Isle_presence.exe")
        return True, f"Installed to {dest}"
    except Exception as e:
        return False, str(e)


def install_onedir(dest: Path) -> tuple[bool, str]:
    try:
        dest.mkdir(parents=True, exist_ok=True)
        out = dest / "The_Isle_presence"
        if out.exists():
            shutil.rmtree(out)
        shutil.copytree(res("The_Isle_presence"), out)
        return True, f"Installed to {out}"
    except Exception as e:
        return False, str(e)



def mkbtn(parent, text, cmd, accent=False, **kw):
    return tk.Button(
        parent, text=text, command=cmd,
        bg=ACC if accent else BTN,
        fg=TEXT,
        activebackground=ACC_H if accent else BTN_H,
        activeforeground=TEXT,
        relief=tk.FLAT, cursor="hand2",
        font=FT_B, padx=14, pady=7, borderwidth=0, **kw
    )


def mklbl(parent, text, font=None, color=None, wrap=560, **kw):
    return tk.Label(
        parent, text=text,
        font=font or FT, bg=BG,
        fg=color or TEXT,
        wraplength=wrap, justify=tk.LEFT, **kw
    )


def mksep(parent):
    tk.Frame(parent, bg=PANEL, height=1).pack(fill=tk.X, pady=10)



class Installer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Isle Presence — Installer")
        self.geometry("640x500")
        self.resizable(False, False)
        self.configure(bg=BG)


        self.build_type  = tk.StringVar(value="onedir")
        self.install_dir = tk.StringVar()
        self.steam_path  = find_steam_path()
        self.isle_path   = (find_isle_path(self.steam_path)
                            if self.steam_path else None)
        self._history: list[type] = []

        self._build_chrome()
        self.show(WelcomePage)

    def _build_chrome(self):

        hdr = tk.Frame(self, bg=PANEL, height=56)
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)
        tk.Label(hdr, text="THE ISLE", font=("Segoe UI", 15, "bold"),
                 bg=PANEL, fg=ACC).pack(side=tk.LEFT, padx=(20, 4), pady=14)
        tk.Label(hdr, text="PRESENCE INSTALLER", font=("Segoe UI", 15),
                 bg=PANEL, fg=TEXT).pack(side=tk.LEFT, pady=14)
        self._step_lbl = tk.Label(hdr, text="", font=FT_SH, bg=PANEL, fg=DIM)
        self._step_lbl.pack(side=tk.RIGHT, padx=20)

        tk.Frame(self, bg=ACC, height=2).pack(fill=tk.X)


        self._content = tk.Frame(self, bg=BG)
        self._content.pack(fill=tk.BOTH, expand=True, padx=32, pady=20)


        tk.Frame(self, bg=PANEL, height=1).pack(fill=tk.X)
        nav = tk.Frame(self, bg=PANEL, height=58)
        nav.pack(fill=tk.X)
        nav.pack_propagate(False)
        self._btn_back = mkbtn(nav, "← Back", self._go_back)
        self._btn_back.pack(side=tk.LEFT, padx=14, pady=10)
        self._btn_next = mkbtn(nav, "Next →", self._go_next, accent=True)
        self._btn_next.pack(side=tk.RIGHT, padx=14, pady=10)

    def show(self, page_cls, replace=False):
        for w in self._content.winfo_children():
            w.destroy()
        if not replace:
            self._history.append(page_cls)
        self._page = page_cls(self._content, self)
        self._page.pack(fill=tk.BOTH, expand=True)
        self._btn_back.config(
            state=tk.NORMAL if len(self._history) > 1 else tk.DISABLED
        )

    def set_step(self, text):
        self._step_lbl.config(text=text)

    def set_next(self, text="Next →"):
        self._btn_next.config(text=text)

    def _go_next(self):
        self._page.on_next()

    def _go_back(self):
        if len(self._history) > 1:
            self._history.pop()
            self.show(self._history.pop(), replace=True)



class Page(tk.Frame):
    def __init__(self, parent, app: Installer):
        super().__init__(parent, bg=BG)
        self.app = app
        self.build()

    def build(self): pass
    def on_next(self): pass

    def heading(self, title, sub=""):
        mklbl(self, title, font=FT_H).pack(anchor=tk.W)
        mklbl(self, sub, font=FT_SH, color=DIM).pack(anchor=tk.W, pady=(2, 14))

    def body(self, text, color=None):
        mklbl(self, text, color=color).pack(anchor=tk.W, pady=3)

    def status(self):
        sv = tk.StringVar()
        lw = tk.Label(self, textvariable=sv, font=FT_SH,
                      bg=BG, fg=DIM, wraplength=560, justify=tk.LEFT)
        lw.pack(anchor=tk.W, pady=4)
        return sv, lw

    def set_status(self, sv, lw, text, color=TEXT):
        sv.set(text)
        lw.config(fg=color)
        self.update_idletasks()


class WelcomePage(Page):
    def build(self):
        self.app.set_step("Step 1 of 5")
        self.app.set_next("Next →")
        self.heading("Welcome", "Discord Rich Presence for The Isle — EVRIMA")
        self.body(
            "This installer sets up the Isle Presence companion app, which shows your "
            "current dinosaur, server, growth percentage, and time of day in your "
            "Discord profile — automatically and with no anti-cheat risk."
        )
        mksep(self)
        mklbl(self, "The installer will:", color=DIM).pack(anchor=tk.W)
        for step in [
            "  1.  Patch Engine.ini to enable the logging the app reads from",
            "  2.  Install the companion app (standalone or Steam-integrated)",
            "  3.  Configure Steam to launch the app automatically with the game",
        ]:
            mklbl(self, step).pack(anchor=tk.W, pady=1)
        mksep(self)
        if self.app.isle_path:
            mklbl(self, f"✓  The Isle detected at:  {self.app.isle_path}",
                  font=FT_SH, color=OK_C).pack(anchor=tk.W)
        else:
            mklbl(self, "⚠  Could not auto-detect The Isle install location — "
                        "you will be asked to browse for it.",
                  font=FT_SH, color=WARN).pack(anchor=tk.W)

    def on_next(self):
        self.app.show(PatchPage)


class PatchPage(Page):
    def build(self):
        self.app.set_step("Step 2 of 5")
        self.app.set_next("Next →")
        self.heading("Game Logging Setup",
                     "Patches Engine.ini to enable the verbose logging the app depends on")
        self.body(
            "Isle Presence reads your dino, server, growth and time of day from "
            "The Isle's log file. Unreal Engine only writes this data when specific "
            "log categories are set to VeryVerbose."
        )
        mklbl(self, f"Location:  {ENGINE_INI_PATH}",
              font=FT_SH, color=DIM).pack(anchor=tk.W, pady=(0, 10))
        mksep(self)

        self._sv, self._lw = self.status()
        self._refresh_status()
        self._pbtn = mkbtn(self, "Patch Engine.ini", self._patch)
        self._pbtn.pack(anchor=tk.W, pady=6)
        mklbl(self,
              "The file will be locked read-only so the game cannot reset it on exit.",
              font=FT_SH, color=DIM).pack(anchor=tk.W)

    def _refresh_status(self):
        if ini_is_patched():
            self.set_status(self._sv, self._lw, "✓  Already patched.", OK_C)
        else:
            self.set_status(self._sv, self._lw, "✗  Not yet patched.", ERR)

    def _patch(self):
        self.set_status(self._sv, self._lw, "Patching…", DIM)
        self._pbtn.config(state=tk.DISABLED)
        ok, msg = patch_ini()
        if ok:
            self.set_status(self._sv, self._lw, f"✓  {msg}", OK_C)
        else:
            self.set_status(self._sv, self._lw, f"✗  {msg}", ERR)
            self._pbtn.config(state=tk.NORMAL)

    def on_next(self):
        if not ini_is_patched():
            self.set_status(self._sv, self._lw,
                            "Please patch Engine.ini before continuing.", WARN)
            return
        self.app.show(BuildPage)


class BuildPage(Page):
    def build(self):
        self.app.set_step("Step 3 of 5")
        self.app.set_next("Next →")
        self.heading("Installation Type",
                     "Choose how you want to run the companion app")

        opts = [
            ("onedir",
             "Steam Auto-Launch  (Recommended)",
             "Launches automatically whenever you start The Isle through Steam.\n"
             "Installs as a folder — Steam's launch options will point at the exe inside."),
            ("onefile",
             "Standalone",
             "A single portable exe you launch manually before playing.\n"
             "Simpler — no Steam configuration needed."),
        ]
        for val, label, desc in opts:
            f = tk.Frame(self, bg=CARD, padx=16, pady=12)
            f.pack(fill=tk.X, pady=6)
            tk.Radiobutton(f, text=label, variable=self.app.build_type,
                           value=val, font=FT_B, bg=CARD, fg=TEXT,
                           activebackground=CARD, activeforeground=TEXT,
                           selectcolor=BG).pack(anchor=tk.W)
            tk.Label(f, text=desc, font=FT_SH, bg=CARD, fg=DIM,
                     justify=tk.LEFT).pack(anchor=tk.W, padx=22, pady=(2, 0))

    def on_next(self):
        self.app.show(LocationPage)


class LocationPage(Page):
    def build(self):
        self.app.set_step("Step 4 of 5")
        self.app.set_next("Install")
        btype = self.app.build_type.get()


        system_drive = Path(os.environ.get("SystemDrive", "C:") + "\\")
        default = str(system_drive)
        self.app.install_dir.set(default)

        self.heading("Install Location",
                     "Where should the app be installed?")
        if btype == "onedir":
            self.body(
                "The The_Isle_presence/ folder will be created inside your chosen directory."
            )

            f = tk.Frame(self, bg="#2a1f0e", padx=12, pady=10)
            f.pack(fill=tk.X, pady=(0, 6))
            tk.Label(f, text="⚠  Do not install inside The Isle's game folder.",
                     font=FT_B, bg="#2a1f0e", fg=WARN, justify=tk.LEFT).pack(anchor=tk.W)
            tk.Label(f,
                     text="EasyAntiCheat scans the game directory tree and will flag the app's "
                          "DLLs as untrusted, blocking you from joining servers. "
                          "Install anywhere outside the game folder — the default below is fine.",
                     font=FT_SH, bg="#2a1f0e", fg=TEXT,
                     wraplength=530, justify=tk.LEFT).pack(anchor=tk.W, pady=(4, 0))
        else:
            self.body("The_Isle_presence.exe will be placed in your chosen directory.")


        row = tk.Frame(self, bg=BG)
        row.pack(fill=tk.X, pady=10)
        self._entry = tk.Entry(row, textvariable=self.app.install_dir, font=FT_MONO,
                 bg=CARD, fg=TEXT, insertbackground=TEXT,
                 relief=tk.FLAT, width=50)
        self._entry.pack(side=tk.LEFT, ipady=6, padx=(0, 8))
        mkbtn(row, "Browse…", self._browse).pack(side=tk.LEFT)

        mksep(self)
        self._sv, self._lw = self.status()

    def _browse(self):
        d = filedialog.askdirectory(initialdir=self.app.install_dir.get())
        if d:
            self.app.install_dir.set(d)

    def on_next(self):
        dest  = Path(self.app.install_dir.get())
        btype = self.app.build_type.get()


        if btype == "onedir" and self.app.isle_path:
            try:
                dest.resolve().relative_to(self.app.isle_path.resolve())
                self.set_status(
                    self._sv, self._lw,
                    "⚠  That path is inside The Isle's game folder. "
                    "EAC will flag the app's DLLs as untrusted — please choose a different location.",
                    WARN
                )
                return
            except ValueError:
                pass  

        self.set_status(self._sv, self._lw, "Installing…", DIM)
        self.update_idletasks()

        ok, msg = (install_onedir(dest) if btype == "onedir"
                   else install_onefile(dest))
        if not ok:
            self.set_status(self._sv, self._lw, f"✗  {msg}", ERR)
            return

        self.set_status(self._sv, self._lw, f"✓  {msg}", OK_C)
        self.after(400, lambda: self.app.show(
            LaunchPage if btype == "onedir" else CompletePage
        ))


class LaunchPage(Page):
    def build(self):
        self.app.set_step("Step 5 of 5")
        self.app.set_next("Finish")
        self.app._btn_next.config(state=tk.DISABLED)
        self._action_taken = False

        dest = Path(self.app.install_dir.get())
        exe  = dest / "The_Isle_presence" / "The_Isle_presence.exe"
        self._opts = f'"{exe}" %command%'

        self.heading("Steam Integration",
                     "Point Steam at the app so it launches with the game")
        self.body(
            "Let the installer configure Steam automatically, or copy the launch "
            "options and paste them in manually."
        )

        mkbtn(self, "Auto-configure Steam", self._auto, accent=True).pack(anchor=tk.W, pady=(4, 6))

        mksep(self)
        mklbl(self, "Or paste manually:  Steam  →  Right-click The Isle  →  Properties  →  Launch Options",
              color=DIM).pack(anchor=tk.W)
        mkbtn(self, "Copy to Clipboard", self._copy).pack(anchor=tk.W, pady=6)
        f = tk.Frame(self, bg=CARD, padx=12, pady=10)
        f.pack(fill=tk.X, pady=(0, 4))
        e = tk.Entry(f, font=FT_MONO, bg=CARD, fg=ACC,
                     relief=tk.FLAT, state="normal", width=62)
        e.insert(0, self._opts)
        e.config(state="readonly")
        e.pack(fill=tk.X, ipady=4)

        self._sv, self._lw = self.status()

    def _unlock_finish(self):
        if not self._action_taken:
            self._action_taken = True
            self.app._btn_next.config(state=tk.NORMAL)

    def _copy(self):
        self.clipboard_clear()
        self.clipboard_append(self._opts)
        self.set_status(self._sv, self._lw, "✓  Copied to clipboard.", OK_C)
        self._unlock_finish()

    def _auto(self):
        if not self.app.steam_path:
            self.set_status(self._sv, self._lw, "✗  Steam not found.", ERR)
            return
        if steam_is_running():
            self.set_status(self._sv, self._lw,
                            "⚠  Steam is running. Close it completely, then try again.", WARN)
            return

        configs = find_localconfigs(self.app.steam_path)
        if not configs:
            self.set_status(self._sv, self._lw,
                            "✗  No localconfig.vdf found.", ERR)
            return

        patched, errors = 0, []
        for cfg in configs:
            try:
                new = set_launch_options(
                    cfg.read_text(encoding="utf-8", errors="ignore"),
                    ISLE_APP_ID, self._opts
                )
                cfg.write_text(new, encoding="utf-8")
                patched += 1
            except Exception as e:
                errors.append(str(e))

        if patched:
            self.set_status(self._sv, self._lw,
                            f"✓  Patched {patched} Steam account(s). "
                            "Launch Steam and The Isle to verify.", OK_C)
            self._unlock_finish()
        else:
            self.set_status(self._sv, self._lw,
                            f"✗  {errors[0] if errors else 'Unknown error.'}", ERR)

    def on_next(self):
        self.app.show(CompletePage)


class CompletePage(Page):
    def build(self):
        self.app.set_step("Done")
        self.app.set_next("Finish")
        self.app._btn_back.config(state=tk.DISABLED)

        self.heading("Installation Complete! 🦕",
                     "Isle Presence is ready to use.")
        mksep(self)

        lines = [
            "✓  Engine.ini patched and locked",
            f"✓  App installed to  {self.app.install_dir.get()}",
        ]
        if self.app.build_type.get() == "onedir":
            lines.append("✓  Steam launch options configured")
        for line in lines:
            mklbl(self, line, color=OK_C).pack(anchor=tk.W, pady=2)

        mksep(self)
        if self.app.build_type.get() == "onedir":
            self.body(
                "Launch The Isle through Steam — the companion app will start silently "
                "in your system tray. Your Discord status updates once you join a server "
                "and spawn as a dinosaur."
            )
        else:
            self.body(
                "Run The_Isle_presence.exe before launching The Isle. "
                "Your Discord status will update once you join a server and spawn."
            )

    def on_next(self):
        self.app.destroy()



if __name__ == "__main__":
    app = Installer()
    app.mainloop()