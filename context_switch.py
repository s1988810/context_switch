####################################################################
# The following program prints the average context_switch time
# and the histogram of the context_switch time per cpu and also
# the overall histogram. It accepts as input the output file
# of the systemtap context switch program and the number of the cpus
#   argv[1]: output of systemtap context _switch
#   argv[2]: number of cpus
#
import os 
import sys

def main(argv):
    num_cpus=argv[2]
    cs_start_time = {}
    cs_end_time = {}
    cs_counter = {}
    cs_overall = {}

    #initialize structures responsible for calculating results
    for i in range(0,num_cpus):
        cs_start_time[i]=0
        cs_end_time[i]=0
        cs_counter[i]=0
        cs_overall[i]=[]

    current_cs_time=0
    with open(argv[1], 'r') as sys_out:
        for l in sys_out.readlines():
            tokens = l.split()
            if (len(tokens) < 3):
                continue
            time_ns = int(tokens[0])
            cpu = int(tokens[1])
        if cs_start_time[cpu] == 0 and tokens[2] == 'CONTEXT_SWITCH_ON':
            cs_start_time[cpu] = time_ns
        if cs_end_time[cpu] == 0 and tokens[2] == 'CONTEXT_SWITCH_OFF':
            cs_end_time[cpu] = time_ns
            cs_counter[cpu] = cs_counter[cpu]+1
            current_cs_time = cs_end_time[cpu]-cs_start_time[cpu]
            cs_overall[cpu].append(current_cs_time)
            cs_end_time[cpu] = 0
            cs_start_time[cpu]=0

    values = cs_overall.values()
    total_sum = sum(values)
    values = cs_counter.values()
    total_counters = sum(values)
    
    print("Distribution Per CPU: ")
    
    for i in range(0,20):
        per_cpu_cs = cs_overall[i];
        hist = {}
        start = min(per_cpu_cs)
        end = max(per_cpu_cs)
        for j in range (start,end+1):
            hist[j] = 0
        for j in per_cpu_cs:
            hist[j]=hist[j]+ 1;
        buckets = ""
        buckets_values = ""
        for j in hist:
            buckets = buckets + hist.index(j) + " "
            buckets_values = buckets_values + "j "

        print("CPU" + i)
        print(buckets)
        print(buckets_values)


    print("Overall CS Histogram: ")
    overall_values = cs_overall.values()
    start = min(overall_values)
    end = max(per_cpu_cs)
    hist = {}
    for j in range (start,end+1):
        hist[j]=0
    for j in overall_values:
        hist[j]=hist[j]+ 1
    buckets=""
    buckets_values=""
    for j in hist:
        buckets = buckets + hist.index(j) + " "
        buckets_values = buckets_values + "j "
    
    
    print(buckets)
    print(buckets_values)

    print("Overall Average Context Switch Time: " + total_sum/total_counters)


if __name__ == "__main__":
  main(sys.argv)