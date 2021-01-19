# https://blog.corujadeti.com.br/owasp-zed-attack-proxy-ferramenta-para-teste-de-vulnerabilidades-em-aplicacoes-web/
# https://tobias.ws/interceptando-conexoes-com-owasp-zed-attack-proxy/
# https://www.google.com/search?q=owasp+zap+windows&oq=OWASP+ZAP+w&aqs=chrome.1.69i57j0l4j69i60l3.4439j0j4&sourceid=chrome&ie=UTF-8


from zapv2 import ZAPv2
from pprint import pprint
import time, sys

if len(sys.argv) is not 2:
    print('Too short arguments.')
    sys.exit(1)
    
target = sys.argv[1]
zap = ZAPv2(proxies={'http': 'http://localhost:8080'})
zap.urlopen(target)
scanid = zap.spider.scan(target)
time.sleep(2)

while (int(zap.spider.status(scanid)) < 100):
    print('Spider progress %s: ' + zap.spider.status(scanid))
    time.sleep(2)
print('Spider completed')

# Give the passive scanner a chance to finish
time.sleep(5)
print('Scanning target %s' % target)

scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    print('Scan progress %: ' + zap.ascan.status(scanid))
    time.sleep(5)
print('Scan completed')

# Report the results
print('Hosts: ' + ', '.join(zap.core.hosts))
pprint (zap.core.alerts())
html = zap.core.htmlreport()
with open('report_file.html', 'a') as f:
    f.write(html)
