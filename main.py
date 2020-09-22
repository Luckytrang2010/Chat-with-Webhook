from discord_webhook import DiscordWebhook, DiscordEmbed
talktime = False
webhook = open("webhook.txt","r+")
if webhook.read() != "":
    op = input("[?] Read file? [Y/N]: ")
    if op.lower() == "y":
        try:
            talktime = True
            while talktime == True:
                msg = input("Enter the message here: ")
                ok = DiscordWebhook(url=webhook,content=msg)
                runtime = ok.execute()
        except Exception as e:
            print(f"Error occured, try again.\nError info: {e}")
    elif op.lower() == "n":
        try:
            wb = input("Enter discord webhook's URL here: ")
            talktime = True
            while talktime == True:
                msg = input("Enter the message here: ")
                ok = DiscordWebhook(url=wb,content=msg)
                runtime = ok.execute()
        except Exception as e:
            print(f"Error occured, try again.\nError info: {e}")
else:
    try:
        wb = input("Enter discord webhook's URL here: ")
        webhook.write(wb)
        talktime = True
        while talktime == True:
            msg = input("Enter the message here: ")
            ok = DiscordWebhook(url=wb,content=msg)
            runtime = ok.execute()
    except Exception as e:
        print(f"Error occured, try again.\nError info: {e}")