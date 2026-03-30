import discord

async def scanner(channel, date_debut, date_fin):

    salon = channel.history(limit=None)

    compteur_image = 0
    async for x_message in salon:
        if x_message.created_at > date_fin:
            continue

        elif date_debut <= x_message.created_at <= date_fin:
            for x_image in x_message.attachments:
                if x_image.filename.endswith(('.heic','.png', '.jpeg','.webp', '.jpg' )):
                    compteur_image+=1

        else:
            break
    return compteur_image
