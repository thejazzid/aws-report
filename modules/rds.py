import boto3

from modules.config import CONFIG
from modules.colors import bcolors

class RdsAnalyzer():
    def __init__(self):
        self.rds_client = boto3.client('rds')

    def find_rds_public(self):
        response = self.rds_client.describe_db_instances()

        for rds in response['DBInstances']:
            public = rds['PubliclyAccessible']
            rds_name = rds['DBInstanceIdentifier']
            engine = rds['Engine']

            if (public):
                print("{0}[WARNING]{1} RDS {2} with engine {3} is public!"\
                        .format(bcolors.FAIL, bcolors.ENDC, rds_name, engine))

