import twitter, datetime

user = 514844672

file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')

currentSession=open("/Users/joshuamapstone/Library/Application Support/Google/Chrome/Default/Current Session")
rawtext = currentSession.read()
lines = rawtext.splitlines()

historyURL = ""

for line in lines:
    if(line.find("//") != -1):
        startIndex = line.rfind("//") + 2
        endIndex = line.rfind("/")
        historyURL = line[startIndex:endIndex]
    
print(lastURL)


api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
statuses = api.GetUserTimeline(user)
print (statuses[0].text)


timestamp = datetime.datetime.utcnow()
response = api.PostUpdate(historyURL + " Good Website " + str(timestamp))
print("Status updated to: " + response.text)


