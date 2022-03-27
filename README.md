# **AUTO DELETE BOT**
Delete group messages after a specific time `INCLUDING MESSAGES FROM BOTS`

## Variables
1. `API_ID` : Get from [my.telegram.org](https://my.telegram.org/)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org)
3. `BOT_TOKEN` : Your telegram **BOT** token from [@BotFather](https://t.me/BotFather)
4. `SESSION` : Generate from here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@HithaishiDesai/STRING-SESSION)
5. `GROUPS` : ID of Groups (seperate by spaces) **EXAMPLE** : -1001274443179
6. `ADMINS` : ID of Admins, messages from admins will not be deleted (seperate by space if multiple ADMINS)
7. `TIME` : Time in **Seconds**

### Make sure:
- **Bot** is <b> ADMIN <b> in Groups with <b>Delete </b> permission
- Account used to create SESSION is <b> ADMIN </b> in Groups

## Deploy in Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HithaishiDesai/Auto-Delete-Bot/tree/MODIFIED)

## Deploy in your VPS

```sh
git clone https://github.com/HithaishiDesai/Auto-Delete-Bot/tree/MODIFIED
cd AutoDelete-V2
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 bot.py
```

### Credits
- [😎 𝗛𝗜𝗧𝗛𝗔𝗜𝗦𝗛𝗜 𝗗𝗘𝗦𝗔𝗜 😎](https://t.me/Hithaishi_Desai)
