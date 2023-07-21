import convex
client = convex.ConvexClient('https://happy-animal-123.convex.cloud')

done = False
cursor = None
data = []

while not done:
    result = client.query('listMessages', {"paginationOpts": {"numItems": 5, "cursor": cursor}})
    cursor = result['continueCursor']
    done = result["isDone"]
    data.extend(result['page'])
    print('got', len(result['page']), 'results')

print('collected', len(data), 'results')