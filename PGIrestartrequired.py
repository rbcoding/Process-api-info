"""
This script gets the list of the processes needing restart
values needed to be supplied to below code as per DT teanant: <tenantdetails>, <Token>
<tenantdetails> - example: https://kyh87588.sprint.dynatracelabs.com
<Token> : Token scope should be - ReadConfig (Read configuration) & DataExport (Access problem and event feed, metrics, and topology)
<Outputfilepath> : example: C:\\Users\\rohit.bisht\\Documents\\Code_output\\processmonitoringstatus.log
"""
import requests,json

#fetching the entityid from process

r = requests.get('https://<tenantdetails>/api/v1/entity/infrastructure/processes', headers= {'Authorization' : 'Api-Token <Token>'})

jsonresponse = r.json()

# Add process entity id's to a list
processids=[]
for item in jsonresponse:
    processids.append(item['entityId']) 
print(processids)


# Extracting process monitoring status and writing into a log file

for id in processids:
    modurl='https://<tenantdetails>/api/v1/entity/infrastructure/processes'
    param1= "entity="+id
       
    r2 = requests.get(modurl, headers= {'Authorization' : 'Api-Token <Token>'},params=param1)
    Project = "DT"
    jsonresponse2=r2.json()
    #print(jsonresponse2)
    monitoringstatus = jsonresponse2[0]['monitoringState']['restartRequired']
#    print(monitoringstatus)
    fileline = jsonresponse2[0]['displayName'] + " " + "Restart required"
   
    if monitoringstatus == True:
        print ("Restart required")
        f1 = open('<Outputfilepath>',mode='a')
        f1.write(str(fileline) + '\n')
        #f1.write('\n')
        f1.close()
    #else:
    #    print ("No restart needed")



# write process entity id's in a file
#with open('C:\\Users\\rohit.bisht\\Documents\\Code_output\\getprocessgroupdetails.log',mode='a') as f1:
#    for item in jsonresponse:
#        f1.write(f"{item['entityId']}")
#        f1.write("\n")
#f1.write('\n')
#f1.close()
