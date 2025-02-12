from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich.console import Console
from rich.panel import Panel
import os

# Initialize Rich console
console = Console()

# Define license options
LICENSE_OPTIONS = [
    Choice("MIT License", name="MIT License – Permissive, allows modification and distribution with attribution."),
    Choice("Apache License 2.0", name="Apache License 2.0 – Similar to MIT but includes patent protection."),
    Choice("GNU General Public License (GPL v3)", name="GNU General Public License (GPL v3) – Strong copyleft, modifications must remain open-source."),
    Choice("GNU Lesser General Public License (LGPL v3)", name="GNU Lesser General Public License (LGPL v3) – Weak copyleft, allows use in proprietary software."),
    Choice("Mozilla Public License 2.0 (MPL 2.0)", name="Mozilla Public License 2.0 (MPL 2.0) – Hybrid license, modified files must stay open-source."),
    Choice("Creative Commons Licenses (CC0, CC BY, etc.)", name="Creative Commons Licenses (CC0, CC BY, etc.) – For non-code assets like documentation."),
    Choice("Unlicense", name="Unlicense – Public domain dedication, no restrictions.")
]

def main():
    console.print(Panel("GitHub README.md Generator", style="bold blue"))

    # Prompt user for project details
    project_title = inquirer.text(message="Project Title:").execute()
    project_description = inquirer.text(message="Project Description:").execute()
    installation_instructions = inquirer.text(message="Installation Instructions:").execute()
    usage_instructions = inquirer.text(message="Usage Instructions:").execute()
    license_choice = inquirer.select(
        message="Select a License:",
        choices=LICENSE_OPTIONS,
        default="MIT License"
    ).execute()
    author_info = inquirer.text(message="Contact / Author Information:").execute()

    # Generate README.md content
    readme_content = f"""# {project_title}

## Description
{project_description}

## Installation
{installation_instructions}

## Usage
{usage_instructions}

## License
This project is licensed under the {license_choice}.

## Author
{author_info}
"""

    # Write to README.md file
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    # Provide feedback to the user
    console.print(Panel(f"[bold green]README.md successfully created![/bold green]", style="bold green"))

if __name__ == "__main__":
    main()