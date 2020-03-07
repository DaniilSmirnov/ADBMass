from ppadb.client import Client as AdbClient

apk_path = "example.apk"

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

for device in devices:
    device.install(apk_path)

