import subprocess

p = subprocess.Popen(
    "where chkdsk.exe",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)

exit_code = p.wait()
print(exit_code)

if p and p.stdout:
    for line in p.stdout.readlines():
        print(str(line, "UTF-8"))

