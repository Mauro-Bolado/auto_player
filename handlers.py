from hero import CwClient, events, TelegramClient
from telethon.tl.custom.message import Message
import asyncio
from datetime import datetime, timedelta, timezone
from random import randint, random, uniform
import re


async def me_ping_handler(event: Message):
    client = event.client  # type: CwClient
    delta_t = datetime.now(timezone.utc) - event.date
    await event.respond('/pong in ' + str(delta_t.total_seconds()) + ' secs')


async def go_and_pledge_handler(event: Message):
    client = event.client  # type: CwClient
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        await asyncio.sleep(randint(10, 50))
        await event.click(0)

    elif 'After a successful act of violence' in event.raw_text:
        await asyncio.sleep(randint(5, 50))
        await client.send_message('@chtwrsbot', '/pledge')


async def autoquest_restored_handler(event: Message):
    client = event.client  # type: CwClient
    if'Stamina restored.' in event.raw_text:
        for i in range(5):
            await asyncio.sleep(randint(2,3))
            await event.respond('🗺Quests')
            await asyncio.sleep(450,500)
            now = datetime.now(timezone.utc)
            if now.minute>10:
                if now.hour==14 or now.hour==6 or now.hour==22:
                    return
                continue


async def auto_click_quest_r_handler (event: Message):
    client = event.client  # type: CwClient
    if 'Many things can happen in the forest.' in event.raw_text:
        await asyncio.sleep(randint(4,5))
        await event.message.buttons[0][randint(0, len(event.buttons[0])-1)].click()


async def auto_click_foray_handler (event: Message):
    client = event.client  # type: CwClient
    if 'Many things can happen in the forest.' in event.raw_text:
        await asyncio.sleep(randint(4,5))
        await event.click(1, 0)



async def massive_spend_handler(event: Message):
    pattern = r'/spend (\d{1,2})'
    # pattern2= r'/stop'
    match=re.match(pattern, event.raw_text)
    for i in range(int(match.groups()[0])):
        # # if '/stop' in event.raw_text:
        # #     return
        # p=re.match(pattern2, event.raw_text)
        # if p is None:
        #     continue
        # else:
        #     return
        await event.client.send_message('@chtwrsbot','🗺Quests')
        await asyncio.sleep(randint(450,500))


async def mobs_to_group_handler(event: Message):
    client = event.client  # type: CwClient
    if 'You met some hostile creatures' in event.raw_text:
        await asyncio.sleep(2)
        await event.forward_to(-100486181604)

async def arena_handler(event: Message):
    client = event.client  # type: CwClient
    pattern=r'/arena'
    match=re.match(pattern, event.raw_text)
    if match:
        await asyncio.sleep(randint(3,1200))
        for i in range(5):
            await client.send_message('@chtwrsbot', '▶️Fast fight')
            await asyncio.sleep(randint(310, 400))


async def tactics_handler(event: Message):
    client = event.client  # type: CwClient
    if 'Prepare for the attack of' in event.raw_text:
        await asyncio.sleep(randint(1,3))
        await client.send_message('@chtwrsbot', '/tactics_wolfpack')


async def drugs(event: Message):
    client = event.client  # type: CwClient
    if '/rage' in event.raw_text:
        await asyncio.sleep(randint(1,600))
        await client.send_message('@chtwrsbot', '/use_p01')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p02')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p03')
    elif '/peace' in event.raw_text:
        await asyncio.sleep(randint(1,600))
        await client.send_message('@chtwrsbot', '/use_p04')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p05')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p06')
    elif '/morph' in event.raw_text:
        await asyncio.sleep(randint(1,600))
        await client.send_message('@chtwrsbot', '/use_p19')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p20')
        await asyncio.sleep(randint(2, 3))
        await client.send_message('@chtwrsbot', '/use_p21')
        
async def mobs_to_player(client:CwClient, event:Message):
    print('here')
    if 'You met some hostile creatures' in event.raw_text and not "Forbidden Champion" in event.raw_text:
        pattern = compile(r'(lvl.)(?P<mob_lvl>[\d]{2})')
        lvl_lits = re.match(pattern, event.raw_text)
        player_lvl = client.level
        if player_lvl >= max(lvl_lits) - 7 and player_lvl <= min(lvl_lits) + 10:
            await event.forward_to('chtwrsbot')
    elif "Forbidden Champion" in event.raw_text:
        pattern = compile(r'(lvl.)(?P<mob_lvl>[\d]{2})')
        lvl_lits = re.match(pattern, event.raw_text)
        if player_lvl < (max(lvl_lits) - 8) and player_lvl > (max(lvl_lits) - 10):
            await event.forward_to('chtwrsbot')
        

async def go_and_trader(resource: str, event: Message):
    client = event.client # type: CwClient
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        await asyncio.sleep(randint(20, 50))
        await event.click(0)
    elif 'You defended villagers well' in event.raw_text:
        cantidad=re.findall(r'\d{3}', event.raw_text)[0]
        await asyncio.sleep(randint(15, 50))
        await event.respond(f'/sc {resource} {cantidad}')