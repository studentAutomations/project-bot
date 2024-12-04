import os
from dhooks import Webhook, Embed, File


WEBHOOK_URL = [os.getenv('PROJECTBOT')]


image2_path = 'sip-nova-obavestenja.png'

for url in WEBHOOK_URL:
    hook = Webhook(url)
    
    
    embed = Embed(
        description="**[SIP link](https://sip.elfak.ni.ac.rs/)**",
        color=0x7289DA  
    ) 
    
    
    embed.set_image(url="attachment://sip-nova-obavestenja.png")
    
    
    file = File(image2_path, name="sip-nova-obavestenja.png")
    
    hook.send("**@everyone 📢 SIP**", embed=embed, file=file)
