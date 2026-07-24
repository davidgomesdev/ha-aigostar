"""Constants for the Aigostar integration."""

DOMAIN = "aigostar"

# Alibaba Cloud IoT EU endpoint
ALIBABA_IOT_HOST = "eu-central-1.api-iot.aliyuncs.com"
ALIBABA_IOT_BASE = f"https://{ALIBABA_IOT_HOST}"
ENDPOINT_GET     = "/thing/properties/get"
ENDPOINT_SET     = "/thing/properties/set"

# API credentials extracted from the AigoSmart Android APK (public, not user secrets)
APP_KEY    = "28770785"
APP_SECRET = "41fd4a1eb18fa7ace5e2abbbe3867f93"

# Config entry keys
CONF_EMAIL       = "email"
CONF_PASSWORD    = "password"

# TSL property identifiers differ between Aigostar models, so the light entity
# resolves the actual identifier at runtime by matching the device's reported
# properties against these candidate lists (first match wins; order = default).
#
#   TG7100C (white CCT):       LightSwitch / Brightness / ColorTemperature
#   A60 RGB CCT (a1tgw5jbxTS):  powerstate  / brightness / colorTemperature
PROP_SWITCH_CANDIDATES     = ("LightSwitch", "powerstate")        # bool  0=off 1=on
PROP_BRIGHTNESS_CANDIDATES = ("Brightness", "brightness")         # int   1-100 (percentage)
PROP_COLOR_TEMP_CANDIDATES = ("ColorTemperature", "colorTemperature")  # int 0-100 (0=warm, 100=cool)
PROP_LIGHT_MODE            = "LightMode"                          # enum  0=white 1=color(RGB)

# Kelvin <-> Aigostar percentage conversion
KELVIN_WARM = 2700   # ColorTemperature = 0
KELVIN_COOL = 6500   # ColorTemperature = 100

# HA brightness 1-255 <-> Aigostar 1-100
HA_BRIGHT_MAX   = 255
AIGO_BRIGHT_MIN = 1
AIGO_BRIGHT_MAX = 100

SCAN_INTERVAL_SECONDS = 30
