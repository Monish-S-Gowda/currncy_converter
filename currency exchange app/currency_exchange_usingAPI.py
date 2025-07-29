import requests
from country_currency_dict import search_country
from country_currency_dict import in_search_out_countrycode
from country_currency_dict import api_call_out
from country_currency_dict import code_to_country
from rich.prompt import Prompt
from rich.prompt import Confirm
from rich.console import Console
console = Console()
from rich import print
import json
import sys

console.clear()
def base_country_search():
    print("[green]country from : [/green]")
    name = in_search_out_countrycode()
    data = api_call_out(name, True)

    return data


def to_country_search():
    print("[red]country to : [/red]")
    name = in_search_out_countrycode()
    to_currency = name.upper()
    return to_currency

def main():
    data = base_country_search()
    to = to_country_search()
    specific_data = data
    try:
        inn = float(Prompt.ask("[yellow]enter the amount[/yellow]"))
    except:
        inn = 1
    print(f"[purple]{str(round(inn*specific_data[to],2))}[/purple] [green]{to}[/green] - [red]{code_to_country(to)}[/red]")

if __name__ == "__main__":
    while True:
        main()
        i = Confirm.ask("[red]do you want to exit[/red]")
        if i:
            console.clear()
            print("[red]exit...[/red]")
            break
        else:
            console.clear()
            print("[green]continue...[/green]")

    import time
    time.sleep(1)
    sys.exit()    

