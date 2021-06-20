from .Cipher import *

class TestCase:
    def setup_class(self):
        global cipher
        cipher = AESCipher(passphrase='test')

    def test_key(self):
        assert cipher.key == b'\x1cd#y\xe5\x8d?A/\x8f\xfe\x80\x1f\x814\x05\x94^PL\xf1\x10?\xf0[F\xd6\x1d\x98"\xad\x9a'

    def test_encrypt(self):
        global enc_content
        enc_content = cipher.encrypt(b'test')
        assert type(enc_content) is bytes
        assert enc_content == b'\xb3&\xe6\x07<<v\x9c\xf6\x05P\xad\xec\xc3\xc2)'

    def test_decrypt(self):
        dec_cont = cipher.decrypt(enc_content)
        assert type(enc_content) is bytes
        assert dec_cont == b'test'
    
    def test_export(self):
        cipher.export('test.dmp')
    
    def test_read(self):
        new_cipher = AESCipher.read('test.dmp')
        assert new_cipher.key == b'\x1cd#y\xe5\x8d?A/\x8f\xfe\x80\x1f\x814\x05\x94^PL\xf1\x10?\xf0[F\xd6\x1d\x98"\xad\x9a'
        assert new_cipher.encrypt(b'test') == b'\xb3&\xe6\x07<<v\x9c\xf6\x05P\xad\xec\xc3\xc2)'
        
 