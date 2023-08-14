# ce script permetra la creation d'un groupe, d'un user l'ajout de celui-ci dans le groupe cree et l'attribution des autorisation a ce user
################################################################################################################################################
# creation d'un groupe
import os
def create_group(group_name):
    try:
        os.system(f'aws iam create-group --group-name {"groupe_Mir"}')
    except :
        print("ce groupe existe déja")
###################################################################################################################################################
def create_user(user_name):
    try:
        os.system(f'aws iam create-user --user-name {"UserTest"}')
    except IOError:
        print("une erreur s'est produite")
#####################################################################################################################################################
def add_user_group():
    try:
        os.system(f'aws iam add-user-to-group --user-name {"UserTest"} --group-name  {"groupe_Mir"}')
    except PermissionError:
        print("vous n'avez pas les droits pour effectuer cet action")
####################################################################################################################################################
# partie execution
group_name = "groupe_Mir"
create_group(group_name)

user_name = "UserTest"
create_user(user_name)

add_user_group()

    
