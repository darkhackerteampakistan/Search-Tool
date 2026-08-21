#!/usr/bin/env python3

import os
import json
import time


# Colors
GREEN="\033[92m"
CYAN="\033[96m"
YELLOW="\033[93m"
RED="\033[91m"
RESET="\033[0m"


DB_FOLDER="database"



def clear():
    os.system("clear")



def banner():

    clear()

    print(f"""
{CYAN}
╔══════════════════════════════╗
║       JSON SEARCH TOOL       ║
║          DEMO VERSION        ║
╚══════════════════════════════╝
{RESET}
""")



def get_databases():

    if not os.path.exists(DB_FOLDER):
        os.mkdir(DB_FOLDER)

    files=[]

    for file in os.listdir(DB_FOLDER):

        if file.endswith(".json"):
            files.append(file)

    return files



def load_json(file):

    path=os.path.join(DB_FOLDER,file)

    try:

        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)

    except:

        return []



def get_fields(data):

    fields=[]

    for item in data[:10]:

        for key in item.keys():

            if key not in fields:
                fields.append(key)


    return fields



def search_data(data,field,value):

    result=[]

    for item in data:

        if str(item.get(field,"")).lower()==value.lower():

            result.append(item)


    return result



def show_results(results,db):


    print("\n")
    print("="*45)

    print(
        f"{GREEN}DATABASE : {db}{RESET}"
    )

    print("="*45)


    for item in results:

        for key,value in item.items():

            print(
                f"{CYAN}{key}{RESET} : {value}"
            )

        print("-"*30)





def all_database_search():


    files=get_databases()


    if not files:

        print("No Database Found")
        return



    # collect fields

    fields=[]


    for file in files:

        data=load_json(file)

        for f in get_fields(data):

            if f not in fields:
                fields.append(f)



    print("\nAvailable Search Fields:\n")


    for i,f in enumerate(fields,1):

        print(
            f"{YELLOW}[{i}] {f}{RESET}"
        )


    print("[0] Back")


    choice=input("\nSelect Field: ")



    if choice=="0":
        return



    try:

        field=fields[int(choice)-1]

    except:

        return



    value=input(
        f"\nEnter {field}: "
    )



    total=0



    print("\nSearching All Database...\n")


    for file in files:


        data=load_json(file)


        result=search_data(
            data,
            field,
            value
        )


        if result:

            show_results(
                result,
                file
            )


            total+=len(result)



    if total==0:

        print(
            f"\n{RED}❌ NOT RESULT FOUND IN ANY DATABASE{RESET}"
        )

    else:

        print(
            f"\n{GREEN}TOTAL MATCH : {total}{RESET}"
        )



    input("\nPress Enter...")




def single_database():

    files=get_databases()


    for i,f in enumerate(files,1):

        data=load_json(f)

        print(
            f"{YELLOW}[{i}] {f} "
            f"(Records: {len(data)}){RESET}"
        )


    print("[0] Back")


    choice=input("\nSelect Database: ")



    if choice=="0":
        return


    try:

        file=files[int(choice)-1]


    except:

        return



    data=load_json(file)


    fields=get_fields(data)


    print("\nFields:\n")


    for i,f in enumerate(fields,1):

        print(
            f"[{i}] {f}"
        )



    choice=input("\nSelect Field: ")



    try:

        field=fields[int(choice)-1]

    except:

        return



    value=input(
        f"Enter {field}: "
    )



    result=search_data(
        data,
        field,
        value
    )


    if result:

        show_results(
            result,
            file
        )

    else:

        print(
            f"\n{RED}❌ NOT RESULT FOUND{RESET}"
        )


    input("\nPress Enter...")





def main():


    while True:


        banner()


        print("""
[1] Search All Database
[2] Search Single Database
[0] Exit
""")


        choice=input("Select: ")



        if choice=="1":

            all_database_search()


        elif choice=="2":

            single_database()


        elif choice=="0":

            break


        else:

            time.sleep(1)




if __name__=="__main__":

    main()
