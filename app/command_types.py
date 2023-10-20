from enum import Enum


class InputCommandType(Enum):
    GET_PARAMS = "get_params"
    GET_TEATS_STATUS = "get_teat_status"
    GET_POS = "get_pos"
    GET_TEATS_COORD = "get_teats_coord"
    MOVE_XY = "move_xy"
    MOVE_Z = "move_z"
    MOVE_STOP = "move_stop"
    ATTACH_TEAT = "attach_teat"
    DETACH_TEAT = "detach_teat"
    START_LASER = "start_laser"
    STOP_LASER = "stop_laser"
    BAD_COMMAND = "bad_command"


class OutputCommandType(Enum):
    GET_PARAMS = "get_params"
    GET_TEATS_STATUS = "get_teat_status"
    GET_POS = "get_pos"
    GET_TEATS_COORD = "get_teats_coord"
    MOVE_XY = "move_xy"
    MOVE_Z = "move_z"
    MOVE_STOP = "move_stop"
    ATTACH_TEAT = "attach_teat"
    DETACH_TEAT = "detach_teat"
    START_LASER = "start_laser"
    STOP_LASER = "stop_laser"


INPUT_COMMANDS = {cmd.value: cmd for cmd in InputCommandType}
OUTPUT_COMMANDS = {cmd: cmd.value for cmd in OutputCommandType}
