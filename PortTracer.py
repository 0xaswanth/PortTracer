import socket
import threading
import time
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich import print
from rich.text import Text

# Initialize console for rich animations
console = Console()

def show_intro():
    """Display a welcome banner with developer details."""
    console.print(
        Panel.fit(
            "[bold cyan]PortTracer[/bold cyan]\n"
            "[yellow]Developed by: Aswanth KP[/yellow]\n"
            "[green]GitHub: [link=https://github.com/0xaswanth]0xaswanth[/link][/green]",
            title="Welcome!",
            border_style="bright_magenta"
        )
    )
    console.print("\n[bold green]Scanning made simple and efficient![/bold green]\n")
    time.sleep(2)

def animate_scan(description):
    """Display a progress bar animation with a description."""
    for step in track(range(100), description=f"[cyan]{description}"):
        time.sleep(0.02)

def scan_port(target, port, results):
    """Scan a single port on the target."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                results.append(port)
    except Exception:
        pass

def port_scanner(target, start_port, end_port):
    """Scan the specified range of ports on the target."""
    results = []
    threads = []
    console.print(f"\n[bold yellow]Scanning {target} from port {start_port} to {end_port}...[/bold yellow]")

    # Create threads for scanning ports
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, results))
        threads.append(thread)
        thread.start()

    # Show progress animation while scanning
    for _ in track(range(len(threads)), description="[green]Scanning ports..."):
        time.sleep(0.01)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Display results
    if results:
        console.print(f"\n[bold green]Open ports detected:[/bold green] [cyan]{', '.join(map(str, results))}[/cyan]")
    else:
        console.print("\n[bold red]No open ports found.[/bold red]")

def main():
    """Main function to run the tool."""
    # Display introduction
    show_intro()

    # User inputs
    target = console.input("[bold yellow]Enter target IP: [/bold yellow]").strip()
    start_port = int(console.input("[bold yellow]Enter starting port: [/bold yellow]").strip())
    end_port = int(console.input("[bold yellow]Enter ending port: [/bold yellow]").strip())

    # Animate preparation
    animate_scan("Preparing to scan ports...")

    # Perform port scanning
    port_scanner(target, start_port, end_port)

    # Goodbye message
    console.print(
        "\n[bold cyan]Thank you for using the Port Scanner Tool![/bold cyan]\n"
        "[bold green]Happy Scanning![/bold green]\n"
    )

if __name__ == "__main__":
    main()
