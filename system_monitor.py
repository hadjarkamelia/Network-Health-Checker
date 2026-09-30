import shutil

total, used, free = shutil.disk_usage("/")

print("===== DISK USAGE =====")

print(f"Total : {total // (1024**3)} GB")
print(f"Used  : {used // (1024**3)} GB")
print(f"Free  : {free // (1024**3)} GB")
`
===== DISK USAGE ===== 
 
===== Total : 512 GB =====
===== Used : 211 GB =====
===== Free : 301 GB ===== 
