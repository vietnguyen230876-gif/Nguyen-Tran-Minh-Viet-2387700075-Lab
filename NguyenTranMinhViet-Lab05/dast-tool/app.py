from flask import Flask, jsonify, request
import os
from runtime_monitor import RuntimeMonitor
from memory_analyzer import MemoryAnalyzer
from network_traffic_analyzer import NetworkTrafficAnalyzer
from security_behavior_checker import SecurityBehaviorChecker
from virtual_sandbox import VirtualSandbox

app = Flask(__name__)
pid = os.getpid()

@app.route("/api/monitor", methods=["GET"])
def monitor():
    rm = RuntimeMonitor(pid)
    return jsonify({
        "cpu_usage": rm.get_cpu_usage(),
        "memory_usage": rm.get_memory_usage(),
        "open_files": [f.path for f in rm.get_open_files()]
    })

@app.route("/api/sandbox", methods=["POST"])
def sandbox():
    data = request.json
    command = data.get("command")
    vs = VirtualSandbox()
    stdout, stderr = vs.run_isolated(command)
    return jsonify({"stdout": stdout, "stderr": stderr})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)