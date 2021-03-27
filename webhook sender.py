from discord_webhook import DiscordEmbed,DiscordWebhook
import csv
try:
    def hello():
        print("Choose options:")
        print("[1] Send message via webhook")
        print("[2] Send embed via webhook")
        print("[3] Add a new webhook")
        print("[4] Send message to test-webhook")
        print("[5] Send embed to test-webhook")
        print("[6] Exit")
        choice = int(input("Input: "))

        if choice == 1:
            sendmessage()
        elif choice == 2:
            sendembed()
        elif choice == 3:
            addwebhook()
        elif choice == 4:
            sendtestmessage()
        elif choice == 5:
            sendtestembed()
        elif choice == 6:
            exit()
        else:
            print("Wrong input!")
            hello()
except Exception as e:
    print("Error: "+ e +"! Something broke... Restarting...")
    hello()


try:
    def sendmessage():
        with open("webhooksettings.csv",newline="") as webhooksettings:
            customer = csv.DictReader(webhooksettings)
            with open("message.txt") as message:
                contentm = message.read()
                for data in customer:
                    webhook = DiscordWebhook(url=data["webhook_url"],content= contentm, avatar_url = data["avatar_url"])
                    response = webhook.execute()
                    if "200" in str(response):
                        print("Success!")
            hello()
except Exception as e:
    print("Error: "+ e +"! Something broke... Restarting...")
    hello()

try:
    def sendtestmessage():
        with open("webhooktestsettings.csv",newline="") as webhooksettings:
            customer = csv.DictReader(webhooksettings)
            with open("message.txt") as message:
                contentm = message.read()
                for data in customer:
                    webhook = DiscordWebhook(url=data["webhook_url"],content= contentm, avatar_url = data["avatar_url"])
                    response = webhook.execute()
                    if "200" in str(response):
                        print("Success!")
            hello()
except Exception as e:
    print("Error: "+ e +"! Something broke... Restarting...")
    hello()


try:
    def sendembed():
        with open("webhooksettings.csv") as webhooksettings:
            customer = csv.DictReader(webhooksettings)
            with open("image URL.txt") as image:
                image_url = image.read()
                with open("message.txt") as message:
                    message_text = message.read()
                    with open("title.txt") as title:
                        title_text = title.read()

                        for data in customer:
                            webhook = DiscordWebhook(url = data["webhook_url"],username =data["username"], avatar_url = data["avatar_url"] )
                            embed = DiscordEmbed(title = title_text , description = message_text,color=int("0x"+data["color"],16))
                            embed.set_author(name=data["author_name"],icon_url= data["author_icon_url"])
                            embed.set_image(url=image_url)
                            embed.set_footer(text=data["footer_text"],icon_url=data["footer_icon_url"])
                            if data["thumbnail_isActive"]=="Yes":
                                embed.set_thumbnail(url=data["thumbnail_url"])
                            if data["timestamp_isActive"]=="No":
                                embed.set_timestamp()
                            webhook.add_embed(embed)
                            response = webhook.execute()
                            if "200" in str(response):
                                print("Success! Embed sent!")
        hello()
except Exception as e:
    print("Error: "+ e +"! Something broke... Restarting...")
    hello()

try:
    def sendtestembed():
        with open("webhooktestsettings.csv") as webhooksettings:
            customer = csv.DictReader(webhooksettings)
            with open("image URL.txt") as image:
                image_url = image.read()
                with open("message.txt") as message:
                    message_text = message.read()
                with open("title.txt") as title:
                    title_text = title.read()

                    for data in customer:
                        webhook = DiscordWebhook(url = data["webhook_url"],username =data["username"], avatar_url = data["avatar_url"] )
                        embed = DiscordEmbed(title = title_text , description = message_text,color = int("0x"+data["color"],16))
                        embed.set_author(name=data["author_name"],icon_url= data["author_icon_url"])
                        embed.set_image(url=image_url)
                        embed.set_footer(text=data["footer_text"],icon_url=data["footer_icon_url"])
                        if data["thumbnail_isActive"]=="Yes":
                            embed.set_thumbnail(url=data["thumbnail_url"])
                        if data["timestamp_isActive"]=="No":
                            embed.set_timestamp()
                        webhook.add_embed(embed)
                        response = webhook.execute()
                        if "200" in str(response):
                            print("Success! Embed sent!")

except Exception as e:
    print("Error: "+ e +"! Something broke... Restarting...")
    hello()


try:
    def addwebhook():
        webhook = []
        print("Input webhook:")
        webhook.append(input("URL:"))
        print("Input username:")
        webhook.append(input("Username:"))
        print("Input avatar URL:")
        webhook.append(input("URL:"))
        print("Input Color (HEX Code):")
        webhook.append(input("Hex: "))
        print("Input Author's Name:")
        webhook.append(input("Name:"))
        print("Input Author's icon URL")
        webhook.append(input("URL:"))
        print("Input footer text:")
        webhook.append(input("Footer text:"))
        print("Input footer icon URL:")
        webhook.append(input("URL:"))
        print("Use Thumbnail? [Y/N]")
        thumbnail = input()
        if thumbnail == "Y":
            print("Input Thumbnail URL:")
            webhook.append(input("URL:"))
            webhook.append("Yes")

            print("Add Timestamp? [Y/N]")
            stamp = input()
            if stamp == "Y":
                webhook.append("Yes")
                with open("webhooksettings.csv","a",newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(webhook)
                    print("Congratulations! Webhook has been added")
            else:
                webhook.append("No")
                with open("webhooksettings.csv","a",newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(webhook)
                    print("Congratulations! Webhook has been added")
        else:
            webhook.append("")
            webhook.append("No")
            print("Add Timestamp? [Y/N]")
            stamp = input()
            if stamp == "Y":
                webhook.append("Yes")
                with open("webhooksettings.csv","a",newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(webhook)
                    print("Congratulations! Webhook has been added")

            else:
                webhook.append("No")
                with open("webhooksettings.csv","a",newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(webhook)
                    print("Congratulations! Webhook has been added")
    hello()

except Exception as e:
    print("Error: "+ str(e) +"! Something broke... Restarting...")
    hello()




hello()