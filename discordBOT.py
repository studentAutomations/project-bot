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
    embed.add_field(name="✅", value="Popravljeni su bagovi i greške.")
    embed.add_field(name="🤖", value="Dodati su novi botovi.")
    embed.add_field(name="✨", value="Poruke bota imaju novi dizajn.")
    embed.add_field(name="⏱️", value="Smanjeno je vreme obrade operacija.")
    embed.add_field(name="📱", value="Notifikacije za mobilne aplikacije sada imaju novi izgled.")
    
    # Pošalji embed
    hook.send("@everyone", embed=embed)
