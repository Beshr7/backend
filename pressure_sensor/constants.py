
CONFIGURATION_SCHEMA = {
    "type": "object",
    "properties": {

        "alert_threshold": {
            "type": "object",
            "properties": {
                "high": {"type": "number"},
                "low": {"type": "number"}
            },
            "required": ["high", "low"]
        },
        "calibration": {
            "type": "object",
            "properties": {
                "offset": {"type": "number"},
                "factor": {"type": "number"}
            },
            "required": ["offset", "factor"]
        }
    },
    "required": ["alert_threshold", "calibration"]
}
