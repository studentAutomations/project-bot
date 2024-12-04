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
        title="Ažuriranje sistema bota donosi sledeće izmene:",
        description = "- Ispravljeni su bagovi i greške.\n- Svaki predmet sada ima svog bota, koji dnevno posećuje sajt barem 50 puta. [znam da je preterano ali github ovako funkcionise i nema sanse da propustimo nove objave]\n- Poruke botova sada imaju novi dizajn.\n- Botovi rade efikasnije.\n- Notifikacije za mobilne aplikacije sada imaju nov izgled.\n\nHvala na pažnji! 😊",
        color=0x7289DA  # Discord plava boja
    ) 
    
    # Dodaj stavke u embed
    #embed.add_field(name="", value="", inline=False)
    
    # Dodaj sliku na embed
    #embed.set_image(url="attachment://sip-nova-obavestenja.png")
    
    # Pošalji poruku sa slikom
    #file = File(image2_path, name="sip-nova-obavestenja.png")
    #hook.send("@everyone", embed=embed, file=file)
    hook.send("@everyone 📢 Ažuriranje botova", embed=embed)
