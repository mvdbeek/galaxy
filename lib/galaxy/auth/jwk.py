import os

from jwcrypto import jwk


def get_or_create_jwk(path, kid='galaxy-identity'):
    if os.path.exists(path):
        with open(path) as fh:
            return jwk.JWK.from_json(fh.read())
    else:
        key = jwk.JWK.generate(kty='RSA', crv='P-256', kid=kid)
        with open(path, 'w') as out:
            out.write(key.export())
        return key
