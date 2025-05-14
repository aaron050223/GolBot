<a href="https://github.com/aaron050223/GolBot/blob/main/CONTRIBUTING.md">
<img src="https://img.shields.io/badge/CONTRIBUTING-8A2BE2">
</a>

# GolBot

## **1. What do you need?**

Before running the bot, make sure you meet the following requirements:

### 1.1. **Do you have Python installed?**

Python es necesario para ejecutar este programa. Para verificar si lo tienes:

1. Open the terminal:
    - Windows: Press `Win + R`, write `cmd` and press Enter.
    - macOS/Linux: Search "Terminal" in your sistem and open it.
2. Type the following command and press Enter:
    
    ```
    python --version
    ```
    
   If it does not work:
    
    ```
    python3 --version
    ```
    
    - If you see something like `Python 3.x.x`, it is already installed.
    - If it does not appear, download it from [python.org](https://www.python.org/downloads/) and install it. **Important:** Check the **Add Python to PATH** option during the installation.

### 1.2. **Do you have the bot file?**

The bot file is called `GolBot.py`. Make sure you have it on your computer and know in which folder it is located.

---

## **2. How to run the bot?**

### 2.1. **Open the terminal**

- Windows: Open `cmd` or PowerShell (`Win + R`, type `cmd` and press Enter)..
- macOS/Linux: Open the “Terminal” application.

### 2.2. **Move to the file folder**

To run the bot, you first need to be in the folder where you saved `GolBot.py`. Use the `cd` command to move around:

- If you saved the file to your Documents folder:
    - In macOS/Linux:
        
        ```
        cd ~/Documents
        ```
        
    - In Windows:
        
        ```
        cd C:\User\YourUser\Documents
        ```
        

To make sure the file is in that folder, type:

```
ls  # macOS/Linux
dir # Windows
```

You should see `GolBot.py` in the list of files.

### 2.3. **Execute the bot**

The bot is run with Python. To start the bot, use one of the following commands, depending on how your system is configured:

- If your sistem uses `python`:
    
    ```
    python GolBot.py
    ```
    
- If your sistem uses `python3`:
    
    ```
    python3 GolBot.py
    ```
    

The bot will start working and you will be able to interact with it through Telegram.

---

## **3. How to use the bot**

### 3.1. **Command `/start`**

The `/start` command welcomes the user and displays the available options:

- It offers commands to view today's matches, the complete matchday, the standings and the top scorers. para consultar.
- Ofrece comandos para ver los partidos de hoy, la jornada completa, la clasificación y los máximos goleadores.

### 3.2. **Command `/partidos`**

The `/partidos` command allows the user to obtain information about the matches of a league on a specific date. You must use the command as follows:

- Matchs of today:
    
    ```
    /partidos <league> hoy
    ```
    
- Matchs of the matchday:
    
    ```
    /partidos <league> jornada
    ```
    

If you do not specify the league or mode correctly (today/day), the bot will prompt you to do it correctly.

### 3.3. **Command `/clasificacion`**

The `/clasificacion` command allows you to look up the current standings of a league. You must use the command as follows:

```
/clasificacion <league>
```

This command returns a list of ranked teams and their points.

### 3.4. **Command `/maximos`**

The `/maximos` command displays the top scorers of a league. You must use the command as follows:

```
/maximos <league>
```

This command returns a list of the players with the most goals in the selected league.

### 3.5. **Common errors**

- If the league or the parameter (hoy/jornada) is omitted in the commands, the bot will prompt you to include it.
- If the league is not valid, the bot will report that the selected league does not exist.
- If the bot cannot get the data from the Football-Data.org API, it will show you an error message.

---

## **4. Explanation of the code**

### 4.1. **Modules used**

- `requests`: Used to make HTTP requests to the Football-Data.org API.
- `telebot`: Library to interact with the Telegram API and create the bot.
- datetime` and `pytz`: To handle dates and times, setting the time zone to Madrid (Europe/Madrid).

### 4.2. **Funciones principales**

- **`start()`**: Sends a welcome message with the bot options when it starts.
- **`obtener_partidos()`**: Gets the matches of the specified league (today or matchday).
- **`obtener_clasificacion()`**: Gets the rankings of the selected league.
- **`obtener_maximos()`**: Shows the top scorers of the selected league.
- **`formatear_partido()`**: Formats the information of each match to present it clearly.


### 4.3. **Usage considerations**

This bot uses the Football-Data.org API, which has a request limit. Make sure not to make too many requests in a short period of time to avoid crashes. Also, the API may be temporarily unavailable, in which case the bot will not be able to get the data.

> ⚠️ **¡Important!** The bot only works **running the python file**, if you don't run the bot **doesn't** work.

# Examples

### /start

When using `/start` the following message will be displayed:

![/start](imagenes_de_ejemplos/start.png)

### /partidos

When using `/partidos`, followed by the desired league and `hoy` (today) or `jornada` (matchday) the following message will be displayed (taking into account that if the match has already finished it will show the result and if it is in game it will show `🟢 En juego` (In game)):


![/partidos](imagenes_de_ejemplos/partidosJornada.png)

### /maximos

When using `/maximos` the following message will be displayed with the top scorers of the selected league:

![/goleadores](imagenes_de_ejemplos/goleadores.png)

### /clasificacion

When using `/clasificacion` the following message will be displayed with the classification of the selected league:

![/clasificaion](imagenes_de_ejemplos/clasificacion.png)

# 🧾 How to get your own tokens?

## 🤖 Telegram token.
- Open Telegram and search for *@BotFather*.
- Start a conversation and use the command:
```
/newbot
```

- Choose a name for your bot (it can be anything).
- Then choose a unique username for the bot (it must end in bot, for example: GolazoBot).
- BotFather will give you an access token like this:
```
123456789:ABCdefGhIjKlmNoPQRstuVWxyZ
```
- Copy that token and paste it into your code as above.
> ⚠️ Keep your token private! Anyone with access to it can control your bot.

## ⚽ football-data.org token.
- Go to https://www.football-data.org/.
- Click on “Get your free API key” or “Sign Up” at the top.
- Sign up with your email address.
- Once registered, go to the Dashboard.
- There you will see your X-Auth-Token, which you will need to include in the code as API_KEY.
