ORG $8E91
tape_press:
    halt
    call 33121
    ld a,(fire)
    or a
    jp z,tape_press
tape_release_reset:
    ld d,8
tape_release:
    halt
    call 33121
    ld a,(fire)
    or a
    jp nz,tape_release_reset
    dec d
    jp nz,tape_release
    ret
