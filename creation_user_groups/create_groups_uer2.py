# creation groupe, user,add user et autorisation avec boto3
import boto3
from botocore.exceptions import ClientError
# creation client pour le service 
C1 = boto3.client('iam')
#############################################################################################################################
# creation groupe de users
def create_groups(GroupName):
    try:
        response = C1.create_group(
           GroupName='Admins',
)
        print(response)
    except Exception as e:
        if e.response == 'EntityAlreadyExists':
           print("un group avec ce nom existe deja")
        elif e.response == 'LimitExceeded':
            print('vous avez atteint la limite du nombre de groupes dont vous avez droit')
        else:
            print("une erreur s'est produite")
#############################################################################################################################
#creation du user
def create_user(UserName):
    try:
        response = C1.create_user(
    UserName='Mir2',
)
        print(response)
    except Exception as e:
        if e.response == 'EntityAlreadyExists':
            print("un utilisateur avec ce nom existe deja")
        elif e.response == 'LimitExceeded':
            print("vous avez atteint la limite  d'utilisateurs a votre compte")
        else:
            print("une erreur s'est produite")
################################################################################################################################# 
# atribution des politiques ou permissions au user
def policy_user(PolicyArn, UserName):
    try:
        response = C1.attach_user_policy(
    PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
    UserName='Mir2',
)
        print(response)
    except Exception as e:
        if e.reponse == 'NoSuchEntity' :
            print("l'utilisateur n'existe pas")
        elif e.response == 'EntityAlreadyExists':
            print(" cette politique existe deja pour ceet utlisateur ")
        else :
            print("une erreur s'est produite")

####################################################################################################################################
# creation des clé d'access du user
def access_user(UserName):
    try:
        response = C1.create_access_key(
    UserName='Mir2',
)
        print(response)
    except Exception as e:
        if e.reponse == 'NoSuchEntity':
            print("cet utlisateur n'estite pas")
        elif e.response == 'AccessDenied':
            print("l'utilisateur n'a pas les permissions requises pour cette action")

        else:
            print("une erreur s'est produite")
        
#########################################################################################################################################
# ajout du user dans le groupe
def add_user_group(GroupName,UserName):
    try:
       response = C1.add_user_to_group(
    GroupName='Admins',
    UserName='Mir2',
)
       print(response) 
    except Exception as e:
        if e.response == 'EntityAlreadyExists':
            print("cet utilisateur des deja dans ce groupe")
        elif e.response == 'NoSuchEntity':
            print("le groupe specifier n'existe pas")
        else:
            print("une erreur ses produite")
#######################################################################################################################################"
# partie execution

GroupName='Admins'
create_groups(GroupName)

UserName='Mir2'
create_user(UserName)

PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess',
UserName='Mir2'
policy_user(PolicyArn, UserName)

access_user(UserName)  

add_user_group(GroupName,UserName)

    

