import boto3

# informations d'identification AWS
aws_access_key = "AKIATOW4MSGJR4J2MRR6"
aws_secret_key = "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"
region_name = "eu-west-3"

# Créer une session AWS
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region_name
)

# Créer un client EC2 à partir de la session
ec2_client = session.client("ec2")

# Paramètres pour la création de l'instance
instance_params = {
    "ImageId": "ami-05b5a865c3579bbc4",
    "InstanceType": "t2.micro",
    #"KeyName": "mir11082023key",  # Remplacez par le nom de votre paire de clés
    "MinCount": 1,
    "MaxCount": 1,
    "TagSpecifications": [
        {
            "ResourceType": "instance",
            "Tags": [
                {"Key": "Name", "Value": "vm-Mirsur"}
            ]
        }
    ]
}

# Créer l'instance EC2
response = ec2_client.run_instances(**instance_params)

# Afficher les informations de l'instance créée
if "Instances" in response:
    instance = response["Instances"][0]
    print("Instance ID:", instance["InstanceId"])
    print("Public DNS:", instance.get("PublicDnsName"))
    print("Public IP:", instance.get("PublicIpAddress"))
else:
    print("La création de l'instance a échoué.")
