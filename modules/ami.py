import boto3

from modules.colors import bcolors

class AmiAnalyzer():
    def __init__(self, owners, region_name):
        self.ec2 = boto3.client('ec2', region_name=region_name)
        self.owners = owners

    def find_public_ami(self):
        amis = self.ec2.describe_images(Owners=self.owners)

        for ami in amis['Images']:
            ami_id = ami['ImageId']
            if ami['Public']:
                print("{0}[WARNING]{1} AMI {2} is public!".format(bcolors.FAIL, bcolors.ENDC, ami_id))

        print("\n")
