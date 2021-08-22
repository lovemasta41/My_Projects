#required pip install azure-identity
#required pip install azure-mgmt-resource
#required pip install azure.mgmt.subscription
#azure account extension
from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.resource.resources import ResourceManagementClient

credentials = DefaultAzureCredential()
subs_client = SubscriptionClient(credential=credentials, baseurl=None, kwargs=any)

for x in subs_client.subscriptions.list():
    print(x.as_dict()['subscription_id'])
    res_client = ResourceManagementClient(credential=credentials,subscription_id=x.as_dict()['subscription_id'])
    for resource_group in res_client.resource_groups.list():
        print(resource_group.as_dict()['name'])

#print(f"successful credential: {credentials._successful_credential}")