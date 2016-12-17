
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

def create_shadow_client(endpoint, ca_path, key_path, cert_path, client_id):
    # For certificate based connection
    client = AWSIoTMQTTShadowClient(client_id)

    # Configurations
    # For TLS mutual authentication
    client.configureEndpoint(endpoint, 8883)

    client.configureCredentials(ca_path, key_path, cert_path)

    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureConnectDisconnectTimeout(10)  # 10 sec
    client.configureMQTTOperationTimeout(5)  # 5 sec

    return client


def connect_to_shadow(client, name):
    client.connect()
    # Create a deviceShadow with persistent subscription
    return client.createShadowHandlerWithName(name, True)