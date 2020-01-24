uLink ="https://indian-cities-api-nocbegfhqg.now.sh/cities"
import requests
r =requests.get(url=uLink)
onelist=[]
data=r.json()
for v in data:
    onelist.append(v['District']+", "+v['State'])

for uv in set(onelist):
    print(uv)

