import json
import sys
from pandas import DataFrame

filename = sys.argv[1]

data = json.load(open(filename))
frame_data = [(k, (len(v['following']), len(v['followers']))) for k,v in data.items()]
frame = DataFrame.from_items(frame_data, orient='index', columns=['following', 'followers'])

print frame

print '## Following'
print frame['following'].describe()
print frame.sort('following', ascending=False)[:10]

print '## Followers'
print frame['followers'].describe()
print frame.sort('followers', ascending=False)[:10]