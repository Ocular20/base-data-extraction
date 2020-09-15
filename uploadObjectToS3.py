from subprocess import check_call

def _upload_to_bucket(key, body):

    call_args = [
        'aws',
        's3api',
        'put-object',
        '--bucket',
        'fornax-data-bucket',
        '--key',
        key,
        '--body',
        body
    ]

    check_call(call_args)
