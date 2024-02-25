from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.holdtap import HoldTap
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()


'''
# TODO Comment one of these on each side
class SplitType:
    UART = const(1)
    I2C = const(2)  # unused
    ONEWIRE = const(3)  # unused
    BLE = const(4)
'''
keyboard.modules = [] # not sure if this line or the analogous line below is needed
keyboard.modules.append(Split(split_type=SplitType.UART, split_side=SplitSide.LEFT))
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

keyboard.extensions = []
keyboard.extensions.append(Oled()) 
keyboard.extensions.append(MediaKeys())


# Define key-codes for easier readability
_______ = KC.TRNS  # Transparent key (passes through the key from the lower layer)
XXXXXXX = KC.NO    # No action


''' From -> https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/layers.md
KC.DF(layer)      -->  Switches the default layer until the next time the keyboard powers off
KC.MO(layer)	  -->  Momentarily activates layer, switches off when you let go
KC.LM(layer, mod) -->  As MO(layer) but with mod active
KC.LT(layer, kc)  -->  Momentarily activates layer if held, sends kc if tapped
KC.TG(layer)      -->  Toggles the layer (enables it if not active, and vice versa)
KC.TO(layer)      -->  Activates layer and deactivates all other layers
KC.TT(layer)      -->  Momentarily activates layer if held, toggles it if tapped repeatedly
KC.HT(KC.A, KC.B) -->  Hold for A, tap for B
'''

# Define the key-map layers
MAIN_LAYER = 0
NUMBER_LAYER = 1
NAVIGATION_LAYER = 2
CS_LAYER = 3
SC2_LAYER_1 = 4
SC2_LAYER_2 = 5
DOTA_LAYER_1 = 6
DOTA_LAYER_2 = 7

# Later switching
MAIN_L  = KC.DF(MAIN_LAYER)
NUM_L   = KC.HT(KC.MO(NUMBER_LAYER), KC.TG(NUMBER_LAYER))
NAV_SFT = KC.HT(KC.LSFT, KC.TG(NAVIGATION_LAYER))  
CS_L    = KC.DF(CS_LAYER) 
SC2_L1  = KC.DF(SC2_LAYER_1)
SC2_L2  = KC.TG(SC2_LAYER_2)
DOT_L1  = KC.DF(DOTA_LAYER_1)
DOT_L2  = KC.TG(DOTA_LAYER_2)

# CSGO key-mods 
T1_HY = KC.HT(KC.N1, KC.Y)# Tap for KC.N1 hold for Y

# Key-map definition
keyboard.keymap = [
# 0 - Main layer
[
    KC.TAB,  KC.Q, KC.W, KC.E,    KC.R,    KC.T,      KC.Y,   KC.U,  KC.I,    KC.O,    KC.P,    XXXXXXX,\
    KC.CAPS, KC.A, KC.S, KC.D,    KC.F,    KC.G,      KC.H,   KC.J,  KC.K,    KC.L,    KC.SCLN, KC.ENT,\
    KC.LCTL, KC.Z, KC.X, KC.C,    KC.V,    KC.B,      KC.N,   KC.M,  KC.COMM, KC.DOT,  KC.SLSH, KC.BSLS,\
                         KC.LALT, KC.BSCP, NUM_L,     KC.ESC, KC.SPC, NAV_SFT, 
],
# 1 - Numbers + Symbols layer 
[
    KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,      KC.N6,    KC.N7,   KC.N8,   KC.N9,   KC.N0,   XXXXXXX,\
    KC.EQL,  KC.PLUS, KC.MINS, KC.ASTR, KC.DLR,  KC.AMPR,    KC.UNDS,  KC.LCBR, KC.RCBR, KC.LPRN, KC.RPRN, XXXXXXX,\
    XXXXXXX, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC,    KC.CIRC,  KC.AMPR, KC.ASTR, XXXXXXX, XXXXXXX, KC.PIPE,\
                               _______, _______, _______,    KC.RGUI,  _______, _______,
],
# 2 - Navigation layer (vim) + function keys + game layers
[
    KC.F1,   KC.F2,   KC.F3,  KC.F4,   KC.F5,   KC.F6,     XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, KC.VOLU,\
    KC.F7,   KC.F8,   KC.F9,  KC.F10,  KC.F11,  KC.F12,    KC.LEFT, KC.UP,   KC.DOWN, KC.RIGHT, XXXXXXX, KC.VOLD,\
    DOT_L1,  SC2_L1,  CS_L,   XXXXXXX, XXXXXXX, XXXXXXX,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, KC.MPLY,\
                               _______, _______, _______,   _______,  _______, _______,
],
# 3 - CSGO layer (TO DO: in CS, bind 'scoreboard' to 'V' & 'plant bomb' to 'C' & 'inspect' to 'T')
[
    KC.N1,   KC.Q, KC.W, KC.E,    KC.R,   KC.T,      KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
    KC.CAPS, KC.A, KC.S, KC.D,    KC.F,   KC.G,      KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.ESC,
    KC.LSFT, KC.Z, KC.X, KC.C,    KC.V,   KC.B,      KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
                         KC.LCTL, KC.N2,  KC.N3,     KC.ESC, KC.SPC, MAIN_L,
],
# 4 - Starcraft Layer 1 
[
    KC.TAB,  KC.Q, KC.W, KC.E,    KC.R,    KC.T,      KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
    KC.LSFT, KC.A, KC.S, KC.D,    KC.F,    KC.G,      KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.ESC,
    KC.LCTL, KC.Z, KC.X, KC.C,    KC.V,    KC.B,      KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
                         KC.LALT, KC.LCTL, SC2_L2,    KC.ESC, KC.SPC, MAIN_L,
],
# 5 - Starcraft Layer 2
[
    KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,      KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
    KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,      KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.ESC,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
                               _______, _______, _______,    KC.ESC, KC.SPC, MAIN_L,
],
# 6 - Dota 2 Layer 1 
[
    KC.TAB,  KC.Q, KC.W, KC.E,    KC.R,    KC.T,      KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
    KC.CAPS, KC.A, KC.S, KC.D,    KC.F,    KC.G,      KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.ESC,
    KC.LSFT, KC.Z, KC.X, KC.C,    KC.V,    KC.B,      KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
                         KC.LALT, KC.LCTL, SC2_L2,    KC.ESC, KC.SPC, MAIN_L,
],
# 7 - Dota 2 Layer 2
[
    KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,      KC.Y,   KC.U,   KC.I,    KC.O,    KC.P,    KC.BSPC,
    KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,      KC.H,   KC.J,   KC.K,    KC.L,    KC.SCLN, KC.ESC,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    KC.N,   KC.M,   KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
                               _______, _______, _______,    KC.ESC, KC.SPC, MAIN_L,
],
]


oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["0","1","2","3","4","5","6","7"]},
        corner_three={0:OledReactionType.STATIC,1:["Hello"]},
        corner_four={0:OledReactionType.LAYER,1:["main","nums","nav","CSGO",
                                                 "SC2", "SC2",
                                                 "DOTA","DOTA"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)

if __name__ == '__main__':
    #keyboard.go(hid_type=HIDModes.USB)
    keyboard.go()


































