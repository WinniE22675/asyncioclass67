import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = 'asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = 'asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:

        async with aiofiles.open(path,mode='r') as f:
            contents = await f.read()
        
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]
        print(moves)

        async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt',mode='w')as f:
            await f.write('\n'.join(moves))

asyncio.run(main())
