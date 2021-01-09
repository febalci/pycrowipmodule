import logging
from pycrowipmodule import CrowIPModuleClient
from pycrowipmodule import StatusState

_LOGGER = logging.getLogger(__name__)
COMMAND_ERR = "Cannot run this command while disconnected. Please run start() first."

class CrowIPAlarmPanel():
    """This class represents Crow IP Module alarm panel."""
        
    def __init__(self, host, port=5002, code='0000',
                 keepAliveInterval=30, eventLoop=None,
                 connectionTimeout=10):
        self._host = host
        self._port = port
        self._connectionTimeout = connectionTimeout
        self._code = code
        self._keepAliveInterval = keepAliveInterval
        self._maxZones = 16
        self._maxOutputs = 8
        self._maxAreas = 2
        self._client = None
        self._eventLoop = eventLoop

        self._zoneState = StatusState.get_initial_zone_state(self._maxZones)
        self._areaState = StatusState.get_initial_area_state(self._maxAreas)
        self._systemState = StatusState.get_initial_system_state()
        self._outputState = StatusState.get_initial_output_state(self._maxOutputs)

        self._zoneStateChangeCallback = self._defaultCallback
        self._areaStateChangeCallback = self._defaultCallback
        self._systemStateChangeCallback = self._defaultCallback
        self._outputStateChangeCallback = self._defaultCallback
        self._commandResponseCallback = self._defaultCallback
        self._connectedCallback = self._defaultCallback

        self._loginTimeoutCallback = self._defaultCallback

        loggingconfig = {'level': 'DEBUG',
                     'format': '%(asctime)s %(levelname)s <%(name)s %(module)s %(funcName)s> %(message)s',
                     'datefmt': '%a, %d %b %Y %H:%M:%S'}

        logging.basicConfig(**loggingconfig)

    @property
    def host(self):
        return self._host
        
    @property
    def port(self):
        return self._port

    @property
    def connection_timeout(self):
        return self._connectionTimeout
        
    @property
    def code(self):
        return self._code
                
    @property
    def keepalive_interval(self):
        return self._keepAliveInterval

    @property
    def zone_state(self):
        return self._zoneState

    @property
    def area_state(self):
        return self._areaState

    @property
    def system_state(self):
        return self._systemState

    @property
    def output_state(self):
        return self._outputState

    @property
    def callback_connected(self):
        return self._connectedCallback

    @callback_connected.setter
    def callback_connected(self, value):
        self._connectedCallback = value

    @property
    def callback_login_timeout(self):
        return self._loginTimeoutCallback

    @callback_login_timeout.setter
    def callback_login_timeout(self, value):
        self._loginTimeoutCallback = value

    @property
    def callback_command_response(self):
        return self._commandResponseCallback

    @callback_command_response.setter
    def callback_command_response(self, value):
        self._commandResponseCallback = value

    @property
    def callback_zone_state_change(self):
        return self._zoneStateChangeCallback

    @callback_zone_state_change.setter
    def callback_zone_state_change(self, value):
        self._zoneStateChangeCallback = value

    @property
    def callback_area_state_change(self):
        return self._areaStateChangeCallback

    @callback_area_state_change.setter
    def callback_area_state_change(self, value):
        self._areaStateChangeCallback = value

    @property
    def callback_system_state_change(self):
        return self._systemStateChangeCallback

    @callback_system_state_change.setter
    def callback_system_state_change(self, value):
        self._systemStateChangeCallback = value
        
    @property
    def callback_output_state_change(self):
        return self._outputStateChangeCallback

    @callback_output_state_change.setter
    def callback_output_state_change(self, value):
        self._outputStateChangeCallback = value

    def _defaultCallback(self, data):
        """This is the callback that occurs when the client doesn't subscribe."""
        _LOGGER.debug("Callback has not been set by client.")	    

    def start(self):
        """Connect to the Crow IP Module, and listen for events to occur."""
        logging.info(str.format("Connecting to Crow IP Module on host: {0}, port: {1}", self._host, self._port))
        self._client = CrowIPModuleClient(self, self._eventLoop)
        self._client.start()
        
    def stop(self):
        """Shut down and close our connection to the Crow IP Module."""
        if self._client:
            _LOGGER.info("Disconnecting from the Crow IP Module...")
            self._client.stop()
        else:
            _LOGGER.error(COMMAND_ERR)

    def arm_away(self):
        """Public method to arm/stay a partition."""
        if self._client:
            self._client.arm_away()
        else:
            _LOGGER.error(COMMAND_ERR)

    def arm_stay(self):
        """Public method to arm/away a partition."""
        if self._client:
            self._client.arm_stay()
        else:
            _LOGGER.error(COMMAND_ERR)


    def disarm(self, code):
        """Public method to disarm a partition."""
        if self._client:
            self._client.disarm(code)
        else:
            _LOGGER.error(COMMAND_ERR)

    def send_keypress(self, code):
        """Public method to disarm a partition."""
        if self._client:
            self._client.send_keys(code)
        else:
            _LOGGER.error(COMMAND_ERR)

    def panic_alarm(self, panic_type):
        """Public method to raise a panic alarm."""
        if self._client:
            self._client.panic_alarm(panic_type)
        else:
            _LOGGER.error(COMMAND_ERR)

    def command_output(self, outputNumber):
        """Public method to activate an output"""
        if self._client:
            self._client.toggle_output(outputNumber)
        else:
            _LOGGER.error(COMMAND_ERR)

    def relay_on(self, relayNo):
        """Public method to activate relay 1."""
        if self._client:
            self._client.activate_relay(relayNo)
        else:
            _LOGGER.error(COMMAND_ERR) 
