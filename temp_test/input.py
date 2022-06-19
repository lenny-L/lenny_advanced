import json

import base64
import time
import unittest
from encodings.base64_codec import base64_decode

from fitportalsdk.common.credential import Credential
from fitportalsdk.common.sign import Sign


class AKSKTestCase(unittest.TestCase):
    def test_sign(self):
        ak = "11e566c6dd65421f9451345753c71de1"
        sk = "23949acc28744b1985d79a40f6967731"
        cred = Credential(access_key=ak, secret_key=sk, digest_mod="sha256")
        signature = Sign(cred).get_signature(time_stamp=time.time())
        print("signature:%s" % signature)
        # X-Auth-Signature
        self.assertIsInstance(signature, str)
        self.assertIsNotNone(signature)

    def test_unzip_sign(self):
        sign = "eyJhayI6ICI2NjY3NjIzNDEzMWM0YmI4YjQ2ODlhZWRhYTdlM2E0ZiIsICJhbGdvcml0aG0iOiAiU0hBMjU2IiwgInRpbWVzdGFtcCI6IDE2MzY5NDU0MzEuNDI0NTk5NH0=,b1f5848b57dacd2d0e919292005bc5507bc5ed082e3111ed9f40da06357b1773"
        base64_str, sign_str = sign.split(",")
        origin_dict = json.loads(base64.b64decode(base64_str.encode()).decode())
        print("origin_dict:%s" % origin_dict)
        print("-=-----")
        # base64_dict = base64_decode(base64_str)
        # ak, algorithm, timestamp = base64_dict.get('ak'), base64_dict.get('algorithm'), base64_dict.get('timestamp')
        # print("ak:%s" % ak)
        # print("algorithm: %s" % algorithm)
        # print("timestamp: %s" % timestamp)

if __name__ == '__main__':
    unittest.main()
