'''Crow/AAP Alarm IP Module Status Definition'''

COMMANDS = {
    'arm': 'ARM',
    'stay': 'STAY',
    'disarm': 'KEYS', # Add ' codeE'
    'get_memory_events': 'MEME',
    'exit_memory_events': 'MEMX',
    'panic': 'PANIC',
    'toggle_chime': 'CHIME',
    'quick_arm_a': 'A',
    'quick_arm_b': 'B',
    'relay_1_on': 'RL1',
    'relay_2_on': 'RL2',
    'toogle_output_x': 'OO',
    'keys': 'KEYS',
    'status': 'STATUS',
}

RESPONSE_FORMATS = {
# ZONE MESSAGES
    r'ZO(?P<data>\d+)': {'name': 'Zone Open', 'handler': 'zone_state_change', 'attr': 'open', 'status': True},
    r'ZC(?P<data>\d+)': {'name': 'Zone Closed', 'handler': 'zone_state_change','attr': 'open', 'status': False},
    r'ZA(?P<data>\d+)': {'name': 'Zone Alarm', 'handler': 'zone_state_change', 'attr': 'alarm', 'status': True},
    r'ZR(?P<data>\d+)': {'name': 'Zone Alarm Restore', 'handler': 'zone_state_change','attr': 'alarm', 'status': False},
    r'ZBY(?P<data>\d+)': {'name': 'Zone Bypass', 'handler': 'zone_state_change', 'attr': 'bypass', 'status': True},
    r'ZBYR(?P<data>\d+)': {'name': 'Zone Bypass Restore', 'handler': 'zone_state_change','attr': 'bypass', 'status': False},
    r'ZTA(?P<data>\d+)': {'name': 'Zone Tamper', 'handler': 'zone_state_change', 'attr': 'tamper', 'status': True},
    r'ZTR(?P<data>\d+)': {'name': 'Zone Tamper Restore', 'handler': 'zone_state_change','attr': 'tamper', 'status': False},

# AREA MESSAGES
    'AA': {'name': 'Area A Armed', 'handler': 'area_state_change', 'attr': 'armed', 'area': '1', 'status': True},
    'AB': {'name': 'Area B Armed', 'handler': 'area_state_change','attr': 'armed', 'area': '2', 'status': True},
    'SA': {'name': 'Area A Stay Armed', 'handler': 'area_state_change', 'attr': 'stay_armed', 'area': '1', 'status': True},
    'SB': {'name': 'Area B Stay Armed', 'handler': 'area_state_change','attr': 'stay_armed', 'area': '2', 'status': True},
    'DA': {'name': 'Area A Disarmed', 'handler': 'area_state_change', 'attr': 'disarmed', 'area': '1', 'status': True},
    'DB': {'name': 'Area B Disarmed', 'handler': 'area_state_change','attr': 'disarmed', 'area': '2', 'status': True},
    'EAA': {'name': 'Area A Exit Delay', 'handler': 'area_state_change', 'attr': 'exit_delay', 'area': '1', 'status': True},
    'EAB': {'name': 'Area B Exit Delay', 'handler': 'area_state_change','attr': 'exit_delay', 'area': '2', 'status': True},
    'ESA': {'name': 'Area A Stay Exit Delay', 'handler': 'area_state_change', 'attr': 'stay_exit_delay', 'area': '1', 'status': True},
    'ESB': {'name': 'Area B Stay Exit Delay', 'handler': 'area_state_change','attr': 'stay_exit_delay', 'area': '2', 'status': True},

# OUTPUT MESSAGES
    r'OO(?P<data>\d+)': {'name': 'Output On', 'handler': 'output_state_change', 'attr': 'open', 'status': True},
    r'OC(?P<data>\d+)': {'name': 'Output Off', 'handler': 'output_state_change', 'attr': 'open', 'status': False},

# SYSTEM MESSAGES
    'MF': {'name': 'Mains Fail', 'handler': 'system_state_change', 'attr': 'mains', 'status': False},
    'MR': {'name': 'Mains Restore', 'handler': 'system_state_change','attr': 'mains', 'status': True},
    'BF': {'name': 'Battery Fail', 'handler': 'system_state_change', 'attr': 'battery', 'status': False},
    'BR': {'name': 'Battery Restore', 'handler': 'system_state_change', 'attr': 'battery', 'status': True},
    'TF': {'name': 'Tamper Fail', 'handler': 'system_state_change', 'attr': 'tamper', 'status': True},
    'TR': {'name': 'Tamper Restore', 'handler': 'system_state_change', 'attr': 'tamper', 'status': False},
    'LF': {'name': 'Line Fail', 'handler': 'system_state_change', 'attr': 'line', 'status': False},
    'LR': {'name': 'Line Restore', 'handler': 'system_state_change', 'attr': 'line', 'status': True},
    'DF': {'name': 'Dialler Fail', 'handler': 'system_state_change', 'attr': 'dialler', 'status': False},
    'DR': {'name': 'Dialler Restore', 'handler': 'system_state_change', 'attr': 'dialler', 'status': True},
    'RO': {'name': 'Ready On', 'handler': 'system_state_change', 'attr': 'ready', 'status': True},
    'NR': {'name': 'Not Ready', 'handler': 'system_state_change', 'attr': 'ready', 'status': False},
    'FF': {'name': 'Fuse Fail', 'handler': 'system_state_change', 'attr': 'fuse', 'status': False},
    'FR': {'name': 'Fuse Restore', 'handler': 'system_state_change', 'attr': 'fuse', 'status': True},
    'ZBF': {'name': 'Zone Battery Fail', 'handler': 'system_state_change', 'attr': 'zonebattery', 'status': False},
    'ZBR': {'name': 'Zone Battery Restore', 'handler': 'system_state_change', 'attr': 'zonebattery', 'status': True},
    'PBF': {'name': 'Pendant Battery Fail', 'handler': 'system_state_change', 'attr': 'pendantbattery', 'status': False},
    'PBR': {'name': 'Pendant Battery Restore', 'handler': 'system_state_change', 'attr': 'pendantbattery', 'status': True},
    'CTF': {'name': 'Code Tamper Fail', 'handler': 'system_state_change', 'attr': 'codetamper', 'status': True},
    'CTR': {'name': 'Code Tamper Restore', 'handler': 'system_state_change', 'attr': 'codetamper', 'status': False},
}
