
# there are ways to connect to a aws sqs (simple Queue service)
# this is one othe the ways.j


def connection_queue(some_dict):
    # Create SQS client
    queue_url = os.getenv('http://aws-some-queue-url')
    sqs = boto3.client('sqs',
                       region_name='us-east-1')
    msg_uuid = str(uuid.uuid4())
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(some_dict),
        MessageDeduplicationId=msg_uuid, # this is optional
        MessageGroupId="1"
    )
