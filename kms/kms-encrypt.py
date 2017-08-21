#import boto3 aws sdk library
import boto3
import base64

if __name__ == '__main__':    
    kms = boto3.client('kms')

    key_id = 'alias/keyName'
    encrypted_kms = kms.encrypt(KeyId=key_id, Plaintext='password')
    encrypted_blob = encrypted_kms[u'CiphertextBlob']
    encoded_password = base64.b64encode(encrypted_blob)
    print(encoded_password)
