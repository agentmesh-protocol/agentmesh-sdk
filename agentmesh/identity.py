import hashlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization


class AgentIdentity:
    """
    Cryptographic identity for an AgentMesh agent.
    Generates an Ed25519 keypair and a unique agent:// URI.
    """

    def __init__(self, name: str):
        self.name = name
        self._private_key = Ed25519PrivateKey.generate()
        self._public_key = self._private_key.public_key()
        self.uri = self._build_uri()

    def _build_uri(self) -> str:
        pub_bytes = self._public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        prefix = hashlib.sha256(pub_bytes).hexdigest()[:8]
        return f"agent://{self.name}-{prefix}"

    def sign(self, data: bytes) -> bytes:
        return self._private_key.sign(data)

    def verify(self, data: bytes, signature: bytes) -> bool:
        try:
            self._public_key.verify(signature, data)
            return True
        except Exception:
            return False

    def __repr__(self):
        return f"<AgentIdentity uri={self.uri}>"
```

Commit message:
```
feat: add AgentIdentity with Ed25519 keypair
