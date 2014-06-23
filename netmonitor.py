#
# Sets pmset AC sleep settings based on network activity over a 10 second period
#
# the poll function is based on the following: 
#   https://code.google.com/p/psutil/source/browse/examples/nettop.py?name=release-0.6.0
#

import psutil, time, subprocess

threshold = 60000       #threshold in bytes
sampleTime = 10         #amount of time to sample

def poll(interval):
    tot_before = psutil.network_io_counters()
    time.sleep(interval)
    tot_after = psutil.network_io_counters()
    return (tot_before, tot_after)

def main():
    (tot_before, tot_after) = poll(sampleTime)
    sent_diff = tot_after.bytes_sent-tot_before.bytes_sent
    recv_diff = tot_after.bytes_recv-tot_before.bytes_recv
    tot_diff = sent_diff + recv_diff
    if(tot_diff > threshold):
        subprocess.Popen(['sudo','/usr/bin/pmset','-c','0'])
    else:
        subprocess.Popen(['sudo','/usr/bin/pmset','-c','20'])

if __name__ == '__main__':
    main()

