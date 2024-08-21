import asyncio
import httpx
import time

async def get_pokemon(client, url):
    print(f'{time.ctime()} - get {url}')
    resp = await client.get(url)
    pokemon = resp.json()
    Pokemon_list = []
    for o in pokemon["pokemon"] :
        print(o['pokemon']['name'])
    print(Pokemon_list)
    return pokemon

async def get_pokemons(n):
    async with httpx.AsyncClient() as client:
        tasks = []
        # rand_list = []
        # for i in range(5):
        #     rand_list.append(random.randint(1,151))
        for i in n:
            url = f'https://pokeapi.co/api/v2/ability/{i}'
            tasks.append(asyncio.create_task(get_pokemon(client,url)))
        pokemons = await asyncio.gather(*tasks)
        return pokemons
    
async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons(['battle-armor','speed-boost'])
    # print(pokemons)
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
   asyncio.run(index())