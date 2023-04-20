import boto3
import json

from kinesis_settings import KinesisSettings

class KinesisFireHose(KinesisSettings):
 
    def __init__(self):
        KinesisSettings.__init__(self)
        self.client = boto3.client(
            "firehose",
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            region_name=self.aws_region,
        )
 
    def insert_item(self, json_data):
 
        response = self.client.put_record(
            DeliveryStreamName=self.stream_name,
            Record={
                'Data': bytes(
                    "{}\n".format(
                        json.dumps(
                            json_data
                        )
                    ).encode("UTF-8")
                ),
            }
        )
        print(response)
        return response
    