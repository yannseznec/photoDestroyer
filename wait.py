import subprocess

p1 = subprocess.Popen(['echo', 'bobbyhadz.com'])
p2 = subprocess.Popen(['echo', 'google.com'])


exit_codes = [p.wait() for p in (p1, p2)]

print(exit_codes)