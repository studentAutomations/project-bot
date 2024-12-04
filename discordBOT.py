import os
from dhooks import Webhook, Embed, File

# Postavi URL za webhook
WEBHOOK_URL = [os.getenv('PROJECTBOT')]

# Putanja do slike
image2_path = 'sip-nova-obavestenja.png'

for url in WEBHOOK_URL:
    hook = Webhook(url)
    
    # Kreiraj embed
    embed = Embed(
        title="Evo najnovijih izmena:",
        description="- Ispravljeni su bagovi i greške.\n- Svaki predmet sada ima svog bota, koji dnevno posećuje sajt barem 50 puta.\n- Poruke bota imaju osvežen dizajn.\n- Rad botova je sada brži i efikasniji.\n- Notifikacije za mobilne aplikacije dobile su novi izgled.\n\nHvala na pažnji! 😊",
        color=0x7289DA  # Discord plava boja
    ) 
    
    # Dodaj stavke u embed
    #embed.add_field(name="", value="", inline=False)
    
    # Dodaj sliku na embed
    #embed.set_image(url="attachment://sip-nova-obavestenja.png")
    
    # Pošalji poruku sa slikom
    #file = File(image2_path, name="sip-nova-obavestenja.png")
    #hook.send("@everyone", embed=embed, file=file)
    hook.send("@everyone 📢 Ažuriranje bota", embed=embed)
