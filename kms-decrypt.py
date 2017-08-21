#import aws sdk library
import boto3
import base64

if __name__ == '__main__':
    kms = boto3.client('kms')

    encrypted_password = 'djadjadjsdfdfdfdjfdjfdjfdjdjdddddddddddddddddddddddsasdfdadfadsfdsafasdf=='
    encoded_password = base64.b64decode(encrypted_password)
    decrypted_kms = kms.decrypt(CiphertextBlob=encoded_password)
    plaintext = decrypted_kms[u'Plaintext']
    print(plaintext)
