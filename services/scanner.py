import discord

async def scanner(channel, date_debut, date_fin):
    salon = channel.history(limit=None)
    compteur_image = 0

    print(f"[DEBUG] date_debut = {date_debut}")
    print(f"[DEBUG] date_fin   = {date_fin}")

    async for x_message in salon:
        print(f"\n[DEBUG] message lu -> {x_message.created_at} | contenu = {x_message.content[:50]}")

        if x_message.created_at > date_fin:
            print("[DEBUG] trop récent -> continue")
            continue

        elif date_debut <= x_message.created_at <= date_fin:
            print("[DEBUG] message dans la plage")
            print(f"[DEBUG] nombre d'attachments = {len(x_message.attachments)}")

            for x_image in x_message.attachments:
                print(f"[DEBUG] fichier trouvé = {x_image.filename}")

                if x_image.filename.lower().endswith(('.heic', '.png', '.jpeg', '.webp', '.jpg')):
                    print("[DEBUG] -> image valide")
                    compteur_image += 1
                else:
                    print("[DEBUG] -> pas une image prise en compte")

        else:
            print("[DEBUG] trop ancien -> break")
            break

    print(f"\n[DEBUG] total images = {compteur_image}")