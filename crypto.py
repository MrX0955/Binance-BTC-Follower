import asyncio, websockets, json, os, platform
from colorama   import Fore
from pystyle    import Colors, Colorate


def clear(): os.system('cls' if platform.system() == 'Windows' else 'clear')


def banner():
    print(Colorate.Horizontal(Colors.purple_to_red, """
                           .d8888b.  8888888b.  Y88b   d88P 8888888b.  88888888888  .d88888b.  
                          d88P  Y88b 888   Y88b  Y88b d88P  888   Y88b     888     d88P" "Y88b 
                          888    888 888    888   Y88o88P   888    888     888     888     888 
                          888        888   d88P    Y888P    888   d88P     888     888     888 
                          888        8888888P"      888     8888888P"      888     888     888 
                          888    888 888 T88b       888     888            888     888     888 
                          Y88b  d88P 888  T88b      888     888            888     Y88b. .d88P 
                           "Y8888P"  888   T88b     888     888            888      "Y88888P"  """, 1))
    print("\n")


async def BTC():
    try:
        clear()
        banner()
        mrx = int(input(
            Colorate.Diagonal(Colors.blue_to_purple, "How many times do you want to repeat? ['0' For Infinity]: ", 2)))
        if "-" in str(mrx): exit("You can't use '-' in the number")
        clear()
        banner()
    except ValueError:
        exit("[!] - Access Denied! - [!]")

    async with websockets.connect('wss://stream.binance.com/stream') as websocket:
        if mrx == 0:
            while True:
                await websocket.send("{\"method\":\"SUBSCRIBE\",\"params\":[\"btctry@kline_1d\"],\"id\":200}")
                await websocket.recv()
                responsee = await websocket.recv()

                print(f" {Fore.YELLOW}> {Fore.RESET}{Fore.LIGHTRED_EX}" + json.loads(responsee)["data"]["k"][
                    "s"] + " -> " + json.loads(responsee)["data"]["k"]["c"])
                await asyncio.sleep(1)

        if mrx != 0:
            for i in range(mrx):
                await websocket.send("{\"method\":\"SUBSCRIBE\",\"params\":[\"btctry@kline_1d\"],\"id\":200}")
                await websocket.recv()
                responsee = await websocket.recv()

                print(f" {Fore.YELLOW}> {Fore.RESET}{Fore.LIGHTRED_EX}" + json.loads(responsee)["data"]["k"][
                    "s"] + " -> " + json.loads(responsee)["data"]["k"]["c"])
                await asyncio.sleep(1)


asyncio.get_event_loop().run_until_complete(BTC())
