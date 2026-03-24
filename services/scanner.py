import discord

async def scanner(channel, date_debut, date_fin):

    salon = channel.history()
    image = 0
    async for x_message in salon:
        if x_message.created_at > date_fin:
            continue

        elif date_debut <= x_message.created_at <= date_fin:
                if x_message.attachments > 0:
                    image+=1
                print(image)

        else:
            break


