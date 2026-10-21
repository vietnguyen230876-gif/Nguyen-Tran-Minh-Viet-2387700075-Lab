import os

class SecurityBehaviorChecker:
    def suspicious_calls(self):
        suspicious = []
        syscalls = ["os.system", "eval", "exec"]
        # Giả lập quét nội dung file hiện tại hoặc các file hệ thống
        content = "os.system eval exec" 
        for call in syscalls:
            if call in content:
                suspicious.append(call)
        return suspicious