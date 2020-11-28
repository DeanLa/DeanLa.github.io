# <li class="list-group-item"><a href="https://www.deanla.com/apps/corona" target="_blank">
#                         מחולל חקירות אפידמיולוגיות</a></li>
tmplt = '''<li class="list-group-item"><a href="{href}" target="_blank">
                        {jobname}</a></li>
                        '''
html = ''
with open('jobs.html', 'r') as f:
    for line in f.readlines():
        if 'href' not in line:
            continue
        line = line.replace('<a href="/sentinelone/job/', 'http://jobs.jobvite.com/sentinelone/job/')
        line = line.replace('</a>', '')
        line = line.strip()
        href, jobname = line.split('">')
        html += tmplt.format(href=href, jobname=jobname)

print(html.strip())