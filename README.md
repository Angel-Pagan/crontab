# crontab
 
Crontab Schedule expressions: 
""" Once a day: 0 0 * * * /usr/bin/python3/home/AngelPagan/crontab/app.py > /usr/bin/python3/home/AngelPagan/crontab/log.txt 2>&1 &
On sunday at 10pm: 0 22 * * SUN /usr/bin/python3/home/AngelPagan/crontab/app.py > /usr/bin/python3/home/AngelPagan/crontab/log.txt 2>&1 &
Once at the end of every quarter: 0 0 1 */3 * /usr/bin/python3/home/AngelPagan/crontab/app.py > /usr/bin/python3/home/AngelPagan/crontab/log.txt 2>&1 &"""

For examples of Crontab expressions please visit https://crontab.guru/examples.html

