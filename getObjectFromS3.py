from subprocess import check_call

def _download_from_bucket(key, outPutFileName):

    call_args = [
        'aws',
        's3api',
        'get-object',
        '--bucket',
        'fornax-data-bucket',
        '--key',
        key,
        outPutFileName
    ]

    check_call(call_args)
