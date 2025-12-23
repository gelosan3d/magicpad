print("Starting macropad firmware")

from kmk_firmware.kmk.kmk_keyboard import KMKKeyboard
from board.pins import oled
from kmk_firmware.kmk.modules.layers import Layers
from kmk_firmware.kmk.keys import KC
keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)
NUM_LAYERS = 8  # define number of layers, 8 is max allowed 

current_layer = 0
def encoder_layer_cycle(direction):
    global current_layer
    if direction > 0:
        current_layer = (current_layer + 1) % NUM_LAYERS
    else:
        current_layer = (current_layer - 1) % NUM_LAYERS
    keyboard.active_layers = [current_layer]


from board.pins import (
    DIRECT_PINS,
    ENC1_A, ENC1_B,
    ENC2_A, ENC2_B,
    LED_DATA,
)

from kmk_firmware.kmk.scanners import DirectPins
keyboard.matrix = DirectPins (
    pins = DIRECT_PINS,
    value_when_pressed = False
)

from kmk_firmware.kmk.modules.encoders import EncoderHandler
encoder = EncoderHandler()
encoder.pins = (
    (ENC1_A, ENC1_B),
    (ENC2_A, ENC2_B),
)
encoder.map = [
    (
        lambda: encoder_layer_cycle(-1),    # CCW
        lambda: encoder_layer_cycle(+1),    # CW
        KC.NO,                              # press
    ), 
    (
        KC.NO,                              # CCW / placeholder
        KC.NO,                              # CW / placeholder
        KC.NO,                              # press / placeholder
    )
]
keyboard.modules.append(encoder)

from kmk_firmware.kmk.extensions.rgb import RGB
rgb = RGB(
    pixel_pin = LED_DATA,
    num_pixels = 2, 
    hue_default = 0,
    sat_default = 255,
    val_default = 64,
    animation_speed = 1,
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    # layer 0
    [
        KC.NO,    # K_1
        KC.NO,    # K_2
        KC.NO,    # K_3
        KC.NO,    # K_4
        KC.NO,    # ENC1 switch
        KC.NO,    # K_5
        KC.NO,    # K_6
        KC.NO,    # K_7
        KC.NO,    # K_8
        KC.NO,    # ENC2 switch
    ],
    # War Thunder
    [
        KC.NO,    # K_1
        KC.NO,    # K_2
        KC.NO,    # K_3
        KC.NO,    # K_4
        KC.NO,    # ENC1 switch
        KC.NO,    # K_5
        KC.NO,    # K_6
        KC.NO,    # K_7
        KC.NO,    # K_8
        KC.NO,    # ENC2 switch
    ],
    # layer 2
    [
        KC.NO,    # K_1
        KC.NO,    # K_2
        KC.NO,    # K_3
        KC.NO,    # K_4
        KC.NO,    # ENC1 switch
        KC.NO,    # K_5
        KC.NO,    # K_6
        KC.NO,    # K_7
        KC.NO,    # K_8
        KC.NO,    # ENC2 switch
    ]
]

"""
KC.LCTRL(KC.C)      # Ctrl+C
KC.LSHIFT(KC.A)     # Shift+A
KC.LALT(KC.TAB)     # Alt+Tab
"""
def update_oled():
    oled.fill(0)
    oled.text(str(current_layer), 0, 12, 1)
    oled.show()

"""
def before_scan():
    update_oled()

keyboard.before_matrix_scan = before_scan
"""

oled.fill(0)
oled.show()

keyboard.go()