from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_encrypt_decrypt():
    # RSA 키 쌍 생성
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()

    # 메시지 정의
    message = "A".encode()

    # 공개 키로 메시지 암호화
    cipher_public = PKCS1_OAEP.new(key.publickey())
    encrypted_message = cipher_public.encrypt(message)
    print("Encrypted with public key:", base64.b64encode(encrypted_message).decode())

    # 개인 키로 암호화된 메시지 복호화
    cipher_private = PKCS1_OAEP.new(key)
    decrypted_message = cipher_private.decrypt(encrypted_message)
    print("Decrypted with private key:", decrypted_message.decode())

    # 공개 키로 복호화된 메시지 다시 암호화
    re_encrypted_message = cipher_public.encrypt(decrypted_message)
    print("Re-encrypted with public key:", base64.b64encode(re_encrypted_message).decode())

rsa_encrypt_decrypt()
