"""
This script gets the list of the process groups where Process monitoring is enabled
values needed to be supplied to below code as per DT tenant: <tenantdetails>, <Token>, <Outputfilepath>
<tenantdetails> - example: https://kyh1111.sprint.dynatracelabs.com
<Token> : Token scope should be - ReadConfig (Read configuration) & DataExport (Access problem and event feed, metrics, and topology)
<Outputfilepath> : example: C:\\Users\\rohit.bisht\\Documents\\Code_output\\processmonitoringstatus.log
"""
import requests,json

#fetching the entityid from process

r = requests.get('https://<tenantdetails>/api/v1/entity/infrastructure/process-groups', headers= {'Authorization' : '<Token>'})

jsonresponse = r.json()

# Add process entity id's to a list
processids=[]
for item in jsonresponse:
    processids.append(item['entityId']) 
print(processids)


# Extracting process monitoring status and writing into a log file

for id in processids:
    modurl='https://<tenantdetails>/api/config/v1/anomalyDetection/processGroups/' + id
    print(modurl)
   
    r2 = requests.get(modurl, headers= {'Authorization' : 'Api-Token <Token>'})
    Project = "DT"
    print(r2.content)
    jsonresponse2=r2.json()
    monitoringstatus = jsonresponse2['availabilityMonitoring']['method']
    fileline = Project + " "+ id + " " + "process monitoring enabled"
   
    if monitoringstatus == "PROCESS_IMPACT":
        print ("Process monitoring enabled")
        f1 = open('<Outputfilepath>',mode='a')
        f1.write(str(fileline) + '\n')
        #f1.write('\n')
        f1.close()
    else:
        print ("process monitoring off")



# write process entity id's in a file
#with open('C:\\Users\\rohit.bisht\\Documents\\Code_output\\getprocessgroupdetails.log',mode='a') as f1:
#    for item in jsonresponse:
#        f1.write(f"{item['entityId']}")
#        f1.write("\n")
#f1.write('\n')
#f1.close()
