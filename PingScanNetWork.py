import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description="Ping Scan Network")
parser.add_argument("-network", dest="network", help="NetWork segment[For example 192.168.56]", required=True)
parser.add_argument("-machines", dest="machines", help="Machines number", type=int, required=True)
parser_args = parser.parse_args()

for ip in range(1, parser_args.machines + 1):
    ipAddress = parser_args.network + "." + str(ip)
    print("Scanning {0}".format(ipAddress))

    if sys.platform.startswith("linux"):
        # Linux
        output = subprocess.Popen(["/bin/ping", "-c 1", ipAddress], stdout= subprocess.PIPE).communicate()[0]
    elif sys.platform.startswith("win"):
        # Windows
        output = subprocess.Popen(["ping", ipAddress], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

    output = output.decode("utf-8")
    print("Output: ",output)

    if "Lost = 0" in output or "bytes from" in output:
        print("The Ip Address {0} has responsed with a ECHO_REPLY".format(ipAddress))
    else:
        print("Time is over/")

print('///')