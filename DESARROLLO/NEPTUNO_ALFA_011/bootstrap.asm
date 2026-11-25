ORG $A200
    im 1
    ei
    ld ix,header
    ld de,17
    ld a,0
    scf
    call 1366
    jp nc,error
    ld ix,16384
    ld de,6912
    ld a,255
    scf
    call 1366
    jp nc,error
    di
    ld b,90
tone:
    ld a,16
    out ($fe),a
    ld c,100
hi:
    dec c
    jp nz,hi
    xor a
    out ($fe),a
    ld c,100
lo:
    dec c
    jp nz,lo
    dec b
    jp nz,tone
    ei
initial_release:
    halt
    call fire
    jp nz,initial_release
press:
    halt
    call fire
    jp z,press
confirm:
    halt
    call fire
    jp z,press
release_reset:
    ld d,8
release:
    halt
    call fire
    jp nz,release_reset
    dec d
    jp nz,release
load_engine:
    ld ix,header
    ld de,17
    ld a,0
    scf
    call 1366
    jp nc,error
    ld ix,24576
    ld de,12288
    ld a,255
    scf
    call 1366
    jp nc,error
    jp 24576
fire:
    ld bc,$7ffe
    in a,(c)
    bit 0,a
    jp z,yes
    ld bc,$001f
    in a,(c)
    and $f0
    cp $10
    jp nz,no
yes:
    ld a,1
    or a
    ret
no:
    xor a
    ret
error:
    ld a,2
    out ($fe),a
    ei
    ld bc,0
    ret
header:
    defs 17,0
