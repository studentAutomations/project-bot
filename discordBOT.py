import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('PROJECTBOT')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone**/n/n**📢 Ažuriranje bota**/n Evo najnovijih promena:/n- Popravljeni su bagovi i greške./n- Dodati su novi botovi./n- Poruke bota imaju novi dizajn./n- Smanjeno je vreme obrade operacija./n- Notifikacije za mobilne aplikacije sada imaju novi izgled./nHvala na pažnji! 😊')
