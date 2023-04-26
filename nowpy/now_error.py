class NowError(Exception):
    INVALID_REQUEST = -32600
    UNKNOWN_METHOD = -32601
    BAD_PARAMETERS = -32602
    INTERNAL_ERROR = -32603
    USER_CANCELLED = -32000
    PROTOCOL_ERROR = -32001
    HW_LOCKED = -32002
    NETWORK_MISMATCH = -32003