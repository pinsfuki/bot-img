import discord

async def scanner(channel, date_debut, date_fin):

    salon = channel.history()
    async for x_date in salon:
        if x_date.created_at > date_fin:
            continue

        elif date_debut <= x_date.created_at <= date_fin:
            print('ok')

        else:
            break


