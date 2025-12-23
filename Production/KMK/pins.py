# firmware/board/pins.py
# imports pins for both XIAO and MCP23017
import board
import busio
from kmk_firmware.kmk.extensions.ioexpander import MCP23017
from kmk_firmware.kmk.extensions.display.ssd1306 import ssd1306

i2c = busio.I2C(board.SCL, board.SDA)       # I2C bus (XIAO default pins)
expander = MCP23017(i2c, address=0x20)      # MCP23017 at address 0x20
    
# OLED display
oled = SSD1306_I2C(
    128, 
    32, 
    i2c, 
    addr=0x3C
)

"""
K_<number>      - keys
ENC<n>_<signal> - encoders
LED_<name>      - LEDs 
"""

# reset
SYS_RESET = board.GP0 # reset pin

# keys
K_1 = expander.get_pin(8)    # SW1
K_2 = expander.get_pin(9)    # SW2
K_3 = expander.get_pin(10)   # SW3
K_4 = expander.get_pin(11)   # SW4
K_5 = expander.get_pin(12)   # SW5
K_6 = expander.get_pin(13)   # SW6
K_7 = expander.get_pin(14)   # SW7
K_8 = expander.get_pin(15)   # SW8

# encoder
ENC1_A  = expander.get_pin(0)   # ROT1_A
ENC1_B  = expander.get_pin(1)   # ROT1_B
ENC1_SW = expander.get_pin(2)   # ROT1_SW

ENC2_A  = expander.get_pin(3)   # ROT2_A
ENC2_B  = expander.get_pin(4)   # ROT2_B
ENC2_SW = expander.get_pin(5)   # ROT2_SW

"""
from pins import (
    DIRECT_PINS,
    ENC1_A, ENC1_B,
    ENC2_A, ENC2_B,
    LED_DATA,
)"""

ENCODER_PINS = (
    (ENC1_A, ENC1_B),
    (ENC2_A, ENC2_B),
)

DIRECT_PINS = (
    K_1, 
    K_2, 
    K_3, 
    K_4, 
    ENC1_SW,
    K_5, 
    K_6, 
    K_7, 
    K_8, 
    ENC2_SW
)

# LEDs
LED_DATA = board.GP1 # SK6812 MINI
