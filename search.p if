#!/usr/bin/env python3

import os
import json
import time

# Colors
G = "\033[92m"
C = "\033[96m"
Y = "\033[93m"
R = "\033[91m"
W = "\033[0m"

DB_FOLDER = "database"


def banner():
    os.system("clear")
    print(f"""
{C}╔════════════════════════════╗
║     JSON SEARCH TOOL        ║
║        DEMO EDITION         ║
╚════════════════════════════╝{W}
""")


def load_databases():

    if not os.path.exists(DB_FOLDER):
        os.mkdir(DB_FOLDER)

    files = []

    for f in os.listdir(DB_FOLDER):
        if f.endswith(".json"):
            files.append(f)

    return files


def load_json(file):

    path = os.path.join(DB_FOLDER, file)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def show_databases():

    while True:

        banner()

        files = load_databases()

        print(f"{Y}Available Database:{W}\n")

        for i, f in enumerate(files, 1):
            try:
                data = load_json(f)
                print(
                    f"{G}[{i}] {f}  "
                    f"(Records: {len(data)}){W}"
                )

            except:
                print(f"{R}[{i}] {f}{W}")

        print("\n[0] Exit")

        choice = input("\nSelect Database: ")

        if choice == "0":
            break

        try:
            selected = files[int(choice)-1]
            search_menu(selected)

        except:
            print(R+"Invalid Selection"+W)
            time.sleep(1)



def detect_fields(data):

    fields=set()

    for item in data[:5]:
        for k in item.keys():
            fields.add(k)

    return list(fields)



def search_menu(filename):

    data = load_json(filename)

    while True:

        banner()

        fields = detect_fields(data)

        print(f"""
{G}Database:{W} {filename}

{C}Total Records:{W} {len(data)}

Available Search Fields:
""")

        for i,f in enumerate(fields,1):
            print(f"{Y}[{i}] Search {f}{W}")

        print("[0] Back")


        choice=input("\nSelect: ")


        if choice=="0":
            break


        try:

            field=fields[int(choice)-1]

            value=input(
                f"\nEnter {field}: "
            )

            results=[]


            for item in data:

                if str(item.get(field,"")).lower()==value.lower():
                    results.append(item)


            show_result(results)


        except:
            print(R+"Invalid Option"+W)

            time.sleep(1)



def show_result(results):

    if not results:

        print(
            f"\n{R}❌ NOT RESULT FOUND{W}"
        )

        input("\nPress Enter...")

        return


    print(
        f"\n{G}✅ {len(results)} RESULT FOUND{W}"
    )


    for item in results:

        print("\n"+"="*35)

        for k,v in item.items():

            print(
                f"{C}{k}{W} : {v}"
            )

        print("="*35)


    input("\nPress Enter...")



if __name__=="__main__":

    show_databases()
