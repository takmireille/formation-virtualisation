# le but de ce script est de script est de cree un vpc, des subnets rattaché ceux-ci à une passerelle, creer une instance,et la rataché à au vpc ou à un subnet
import boto3
from botocore.exceptions import ClientError
# creation client pour le service 
C2 = boto3.client('ec2')
##############################################################################################################################################################
# creation du vpc
def create_vpc():
    try:
        response = C2.create_vpc(
           CidrBlock='12.0.0.0/16',
           Ipv4IpamPoolId='12.1.0.0/16',
           Ipv4NetmaskLength=16,
           DryRun=False,
           InstanceTenancy='default',
           TagSpecifications=[
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'vpc_name',
                    'Value': 'Mir2Vpc'
                },
            ]
        },
    ]
)
        print(response)
    except Exception as e:
        if e.response == 'CidrBlockConflict':
            print("cette plage d'IP est deja en utlisation")
        elif e.response == 'InvalidParameterValue':
            print("les valeurs specifiés pour les parametres sont invalides")

