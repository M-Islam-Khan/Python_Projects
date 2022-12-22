import math
import speedtest

obj = speedtest.Speedtest()

bytes_to_mb = 1000000

print("Getting download speed...")
down_speed = round(obj.download() / bytes_to_mb, 2)

print("Getting upload speed...")
up_speed = round(obj.upload() / bytes_to_mb, 2)


print(f"Download Speed : {down_speed} Mbps")
print(f"Upload Speed : {up_speed}  Mbps")