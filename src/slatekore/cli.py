"""Slatekore CLI - Initialize Obsidian vaults as AI research second brains."""

import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from . import __version__
from .init import initialize_vault
from .check import check_prerequisites

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="slatekore")
def main():
    """🧠 Slatekore - AI Research Second Brain for Obsidian + Gemini CLI.
    
    Initialize your Obsidian vault as a powerful AI-powered research second brain.
    """
    pass


@main.command()
@click.argument("path", type=click.Path(), default=".")
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files")
def init(path: str, force: bool):
    """Initialize an Obsidian vault with Slatekore.
    
    PATH is the target directory (defaults to current directory).
    
    Examples:
    
        slatekore init                  # Initialize current directory
        
        slatekore init ./my-vault       # Initialize specific directory
        
        slatekore init . --force        # Overwrite existing config
    """
    target = Path(path).resolve()
    
    console.print(Panel.fit(
        f"[bold blue]🧠 Slatekore v{__version__}[/bold blue]\n"
        f"Initializing vault at: [cyan]{target}[/cyan]",
        border_style="blue"
    ))
    
    try:
        result = initialize_vault(target, force=force)
        
        console.print()
        console.print("[bold green]✅ Vault initialized successfully![/bold green]")
        console.print()
        
        # Show what was created
        console.print("[bold]Created:[/bold]")
        for item in result["created"]:
            console.print(f"  [green]•[/green] {item}")
        
        if result.get("skipped"):
            console.print()
            console.print("[bold yellow]Skipped (already exists):[/bold yellow]")
            for item in result["skipped"]:
                console.print(f"  [yellow]•[/yellow] {item}")
        
        console.print()
        console.print(Panel(
            "[bold]Next steps:[/bold]\n\n"
            "1. Open the vault in Obsidian\n"
            "2. Install required plugins: [cyan]terminal[/cyan], [cyan]calendar[/cyan], [cyan]card-board[/cyan]\n"
            "3. Open terminal and run: [cyan]gemini[/cyan]\n"
            "4. Start with: [cyan]/daily-setup[/cyan] or [cyan]/capture <url>[/cyan]",
            title="🚀 Getting Started",
            border_style="green"
        ))
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise SystemExit(1)


@main.command()
def check():
    """Check if prerequisites are installed.
    
    Verifies:
    - Gemini CLI is installed and accessible
    - Obsidian plugins are recommended
    """
    console.print("[bold]Checking prerequisites...[/bold]")
    console.print()
    
    results = check_prerequisites()
    
    all_good = True
    for name, status in results.items():
        if status["ok"]:
            console.print(f"[green]✓[/green] {name}: {status['message']}")
        else:
            console.print(f"[red]✗[/red] {name}: {status['message']}")
            if status.get("help"):
                console.print(f"  [dim]→ {status['help']}[/dim]")
            all_good = False
    
    console.print()
    if all_good:
        console.print("[bold green]All prerequisites met! Ready to use slatekore.[/bold green]")
    else:
        console.print("[bold yellow]Some prerequisites missing. See above for details.[/bold yellow]")


@main.command()
def upgrade():
    """Upgrade templates to the latest version.
    
    Updates templates and workflows while preserving your notes.
    """
    console.print("[yellow]Upgrade command coming soon![/yellow]")
    console.print("For now, re-run [cyan]slatekore init --force[/cyan] to update templates.")


if __name__ == "__main__":
    main()
