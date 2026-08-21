#!/usr/bin/env python3

import os
import json
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich import box


console = Console()


DB_FOLDER = "database"



def clear():
    os.system("clear")



def banner():

    clear()

    console.print(
        Panel.fit(
            "[bold cyan]JSON SEARCH TOOL[/bold cyan]\n"
            "[yellow]Professional Demo Edition[/yellow]",
            border_style="cyan"
        )
    )



def loading(text):

    with Progress() as progress:

        task = progress.add_task(
            f"[cyan]{text}",
            total=100
        )

        while not progress.finished:

            progress.update(
                task,
                advance=20
            )

            time.sleep(0.1)



def databases():

    if not os.path.exists(DB_FOLDER):

        os.mkdir(DB_FOLDER)


    files=[]


    for f in os.listdir(DB_FOLDER):

        if f.endswith(".json"):

            files.append(f)


    return files



def load_json(file):

    path=os.path.join(
        DB_FOLDER,
        file
    )


    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            data=json.load(f)


            if isinstance(data,list):

                return data


            else:

                return [data]


    except Exception as e:

        console.print(
            f"[red]JSON Error {file}: {e}[/red]"
        )

        return []



def get_fields():

    fields=[]


    for file in databases():

        data=load_json(file)


        for item in data[:10]:

            for key in item.keys():

                if key not in fields:

                    fields.append(key)


    return fields



def search_all(field,value):


    total=0


    console.print(
        "\n[bold yellow]Searching Database...[/bold yellow]\n"
    )


    for file in databases():


        loading(
            f"Checking {file}"
        )


        data=load_json(file)


        result=[]


        for item in data:


            if str(
                item.get(field,"")
            ).lower() == value.lower():

                result.append(item)



        if result:


            table=Table(
                title=f"📁 {file}",
                box=box.ROUNDED
            )


            table.add_column(
                "Field",
                style="cyan"
            )

            table.add_column(
                "Value",
                style="green"
            )


            for item in result:


                for k,v in item.items():

                    table.add_row(
                        k,
                        str(v)
                    )


                table.add_row(
                    "",
                    ""
                )


            console.print(table)


            total += len(result)



    console.print(
        Panel(
            f"[bold green]Total Match Found : {total}[/bold green]"
            if total
            else
            "[bold red]NOT RESULT FOUND[/bold red]",
            border_style="green"
        )
    )


    input("\nPress Enter...")



def menu():


    while True:


        banner()


        console.print("""
[green][1][/green] Search All Database
[yellow][2][/yellow] Database Information
[red][0][/red] Exit
""")


        choice=input(
            "Select: "
        )



        if choice=="1":


            fields=get_fields()


            console.print(
                "\nAvailable Fields:\n"
            )


            for i,f in enumerate(fields,1):

                console.print(
                    f"[cyan]{i}[/cyan] {f}"
                )


            select=input(
                "\nSelect Field: "
            )


            try:

                field=fields[
                    int(select)-1
                ]


            except:

                continue



            value=input(
                f"Enter {field}: "
            )


            search_all(
                field,
                value
            )



        elif choice=="2":


            banner()


            for f in databases():

                data=load_json(f)


                console.print(
                    f"[cyan]{f}[/cyan] "
                    f"Records: [green]{len(data)}[/green]"
                )


            input(
                "\nPress Enter..."
            )



        elif choice=="0":

            break





if __name__=="__main__":

    menu()
