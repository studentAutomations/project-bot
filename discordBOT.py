import os
from dhooks import Webhook, Embed, File


WEBHOOK_URL = [os.getenv('PROJECTBOT')]


image2_path = 'sip-nova-obavestenja.png'

for url in WEBHOOK_URL:
    hook = Webhook(url)
    
    
    embed = Embed(
        description="**Evo najnovijih izmena:\n\n- svi botovi sadaimaju built in link koji vas vodi direktno na forum sa novostima\n\nHvala na pažnji! 😊**",
        color=0x7289DA  
    ) 
    
    hook.send("@everyone 📢 Ažuriranje botova", embed=embed)
