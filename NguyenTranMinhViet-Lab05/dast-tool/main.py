import os
from runtime_monitor import RuntimeMonitor
from memory_analyzer import MemoryAnalyzer
from network_traffic_analyzer import NetworkTrafficAnalyzer
from security_behavior_checker import SecurityBehaviorChecker
from virtual_sandbox import VirtualSandbox

if __name__ == "__main__":
    pid = os.getpid()
    print("[+] Monitoring current process:", pid)
    
    rm = RuntimeMonitor(pid)
    print("CPU Usage:", rm.get_cpu_usage())
    print("Memory Usage:", rm.get_memory_usage())
    
    ma = MemoryAnalyzer()
    print("Overflow Test:", ma.check_overflow(2**64))
    
    nta = NetworkTrafficAnalyzer()
    print("Network Stats Active")
    
    sbc = SecurityBehaviorChecker()
    print("Suspicious Calls:", sbc.suspicious_calls())
    
    vs = VirtualSandbox()
    out, err = vs.run_isolated("echo Hello Sandbox")
    print("Sandbox stdout:", out)