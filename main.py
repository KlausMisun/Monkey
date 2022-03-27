import random
import asyncio
from datetime import datetime

CHARACTERS = "ACT I\nSEN.lsinorepatfmbhcFROBDW'?y,w:duLgvk!HY;qMUGx-PQjzJKV[]Z&"
CHARACTERS_COUNT = len(CHARACTERS)

f = open("hamlot.txt", "r")
hamlot = f.read()
hamlotSize = len(hamlot)

random.seed(datetime.now().second)


async def monkeyWrite(monkeyNumber: int):
    position = 0
    highestPosition = 0

    generatedText = ''

    while hamlotSize > position:
        randomCharacterIndex = random.randint(0, len(CHARACTERS) - 1)
        randomCharacter = CHARACTERS[randomCharacterIndex]

        if (hamlot[position] == randomCharacter):
            generatedText += randomCharacter
            position += 1
            continue

        if (position > highestPosition):
            highestPosition = position
            print(
                "New HighScore reached: {position} characters by Monkey #{name} \n"
                .format(position=position, name=monkeyNumber))

        position = 0
        text = ''

    print("MONKEY DID IT")


async def main():
    tasks = [monkeyWrite(num) for num in range(3)]
    await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
coroutine = main()
loop.run_until_complete(coroutine)
