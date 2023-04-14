from minio import Minio


MINIO_ENDPOINT='amazon:9000'
MINIO_ACCESS_KEY='minioadmin'
MINIO_SECRET_KEY='minioadmin'

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

BUCKET_NAME = 'jojo-bucket'
FILE_NAME = 'yoyo.json'

# Essayez de créer le bucket s'il n'existe pas déjà
found = client.bucket_exists(BUCKET_NAME)
if not found:
    client.make_bucket(BUCKET_NAME)


try:
    client.fput_object(BUCKET_NAME, FILE_NAME, FILE_NAME)
    print(f'Le fichier {FILE_NAME} a été poussé avec succès dans le bucket {BUCKET_NAME}')
except :
    print('connard')