'''Crow/AAP Alarm IP Module Feedback Class for alarm state'''

class StatusState:
    # Zone State
    @staticmethod
    def get_initial_zone_state(maxZones):
        """Builds the proper zone state collection."""
        _zoneState = {}
        for i in range (1, maxZones+1):
            _zoneState[i] = {'status': {'open': False, 'bypass': False, 'alarm': False, 'tamper': False}, 
                                           'last_fault': 0}

        return _zoneState

    # Area State
    @staticmethod
    def get_initial_area_state(maxAreas):
        """Builds the proper alarm state collection."""

        _areaState = {}

        for i in range(1, maxAreas+1):
            _areaState[i] = {'status': {'alarm': False, 'armed': False, 'stay_armed': False, 
                                        'disarmed': False,'exit_delay': False, 'stay_exit_delay': False, 
                                        'alarm_zone': '', 'last_disarmed_by_user': '', 
                                        'last_armed_by_user': '' }}

        return _areaState

    # Output State
    @staticmethod
    def get_initial_output_state(maxOutputs):
        _outputState = {} 
        for i in range (1, maxOutputs+1):
            _outputState[i] = {'status': {'open': False}}
        return _outputState

    # System Status State
    @staticmethod
    def get_initial_system_state():
        _systemState = {'status':{'mains': True, 'battery': True,'tamper': False, 'line': True, 
                        'dialler': True,'ready': True, 'fuse': True, 'zonebattery': True, 
                        'pendantbattery': True, 'codetamper': False}}
        return _systemState







