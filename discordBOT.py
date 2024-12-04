import os
from dhooks import Webhook, Embed

# Postavi URL za webhook
WEBHOOK_URL = [os.getenv('PROJECTBOT')]

for url in WEBHOOK_URL:
    hook = Webhook(url)
    
    # Kreiraj embed
    embed = Embed(
        title="📢 Ažuriranje bota",
        description="Evo najnovijih promena:",
        color=0x7289DA  # Discord plava boja
    )
    
    # Dodaj stavke u embed
    embed.add_field(name="✅", value="Popravljeni su bagovi i greške.", inline=False)
    embed.add_field(name="🤖", value="Dodati su novi botovi.", inline=False)
    embed.add_field(name="✨", value="Poruke bota imaju novi dizajn.", inline=False)
    embed.add_field(name="⏱️", value="Smanjeno je vreme obrade operacija.", inline=False)
    embed.add_field(name="📱", value="Notifikacije za mobilne aplikacije sada imaju novi izgled.", inline=False)
    
    # Pošalji embed
    hook.send("@everyone", embed=embed)
