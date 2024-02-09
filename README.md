# Discord_bot
A discord bot example to make it online 24/7 updated method after replit
### How to make it online?
1. Create a account on [render](https://render.com/).
2. Create new web service.
3. Add your github repository link ex. ``https://github.com/shiv09ds/Discord_bot``
4. Fill the necessary information for bot : (bot name)
5. Start command ``gunicorn main:app``
6. make sure you write your file name on left side of command ``gunicorn <your file name>:app``
7. create a variable on the bottom name it ``token`` and add your token in value place
9. choose the method for free and deploy
10. wait untill it shows ``your web service is live 🎉``
11. copy the link on left side of the shell it'll look like ``https://discord_bot-lop8.onrender.com``
12. Create an account on [Uptime robot](https://uptimerobot.com/)
13. create new monitor add your new copied http link and start monitor
### What is .env variable?
> the variable we created ``token`` while deploying our bot?
>  well it helps to hide our token into .env file.
> to access the token we use ``getenv`` function in python
### Discord token in public repositories
1. Discord is on high alert that your token must be safe.That's why whenever we upload it to public repositories discord changes your bot token.
2. use .env file to hide your token
