import aiohttp
import asyncio

path = "../crawler/util/top-1000-websites.txt"
full_links = open("../crawler/util/top1kFullLinks.txt", "a")

async def check_link(session, site):
    try:
        async with session.get(f"https://{site}") as response:
            print(response.status)
            full_links.write(f"https://{site}\n")
    except aiohttp.ClientError:
        try:
            async with session.get(f"http://{site}") as response:
                print(response.status)
                full_links.write(f"http://{site}\n")
                
        except aiohttp.ClientError:
            print(f"{site} site failed")

        except asyncio.exceptions.TimeoutError:
            print("Async operation timed out!")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [check_link(session, site) for site in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    with open(path, "r") as links:
        urls = [site.strip() for site in links.readlines()]

    asyncio.run(main())
    full_links.close()
