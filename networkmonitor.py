import subprocess, time, datetime
import re

while True:
    with open("./netspeedlog.csv", "a") as f:
        print("started mesuring")
        output = str(subprocess.check_output(["speedtest"]))
        downspeed = re.search("[0-9]*\.[0-9]* Mbit/s", output[output.find("Download:"):]).group()
        upspeed = re.search("[0-9]*\.[0-9]* Mbit/s", output[output.find("Upload:"):]).group()
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        weekday = datetime.datetime.now().strftime('%a')
        f.write(now + "," + weekday + "," + downspeed.replace(" ", ",") + "," + upspeed.replace(" ", ",") + \n)
        print("Done")
        time.sleep(60)
