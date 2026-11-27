saved_sp equ $6803
ORG $A200
    ld (saved_sp),sp
row_0_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A21D),sp
    ld sp,$400C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_0_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A235),sp
    ld sp,$4018
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_1_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A24D),sp
    ld sp,$410C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_1_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A265),sp
    ld sp,$4118
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_2_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A27D),sp
    ld sp,$420C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_2_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A295),sp
    ld sp,$4218
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_3_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A2AD),sp
    ld sp,$430C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_3_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A2C5),sp
    ld sp,$4318
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_4_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A2DD),sp
    ld sp,$440C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_4_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A2F5),sp
    ld sp,$4418
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_5_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A30D),sp
    ld sp,$450C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_5_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A325),sp
    ld sp,$4518
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_6_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A33D),sp
    ld sp,$460C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_6_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A355),sp
    ld sp,$4618
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_7_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A36D),sp
    ld sp,$470C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_7_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A385),sp
    ld sp,$4718
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_8_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A39D),sp
    ld sp,$402C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_8_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A3B5),sp
    ld sp,$4038
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_9_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A3CD),sp
    ld sp,$412C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_9_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A3E5),sp
    ld sp,$4138
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_10_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A3FD),sp
    ld sp,$422C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_10_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A415),sp
    ld sp,$4238
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_11_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A42D),sp
    ld sp,$432C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_11_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A445),sp
    ld sp,$4338
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_12_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A45D),sp
    ld sp,$442C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_12_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A475),sp
    ld sp,$4438
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_13_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A48D),sp
    ld sp,$452C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_13_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A4A5),sp
    ld sp,$4538
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_14_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A4BD),sp
    ld sp,$462C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_14_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A4D5),sp
    ld sp,$4638
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_15_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A4ED),sp
    ld sp,$472C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_15_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A505),sp
    ld sp,$4738
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_16_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A51D),sp
    ld sp,$404C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_16_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A535),sp
    ld sp,$4058
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_17_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A54D),sp
    ld sp,$414C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_17_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A565),sp
    ld sp,$4158
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_18_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A57D),sp
    ld sp,$424C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_18_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A595),sp
    ld sp,$4258
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_19_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A5AD),sp
    ld sp,$434C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_19_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A5C5),sp
    ld sp,$4358
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_20_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A5DD),sp
    ld sp,$444C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_20_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A5F5),sp
    ld sp,$4458
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_21_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A60D),sp
    ld sp,$454C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_21_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A625),sp
    ld sp,$4558
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_22_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A63D),sp
    ld sp,$464C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_22_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A655),sp
    ld sp,$4658
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_23_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A66D),sp
    ld sp,$474C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_23_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A685),sp
    ld sp,$4758
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_24_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A69D),sp
    ld sp,$406C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_24_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A6B5),sp
    ld sp,$4078
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_25_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A6CD),sp
    ld sp,$416C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_25_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A6E5),sp
    ld sp,$4178
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_26_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A6FD),sp
    ld sp,$426C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_26_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A715),sp
    ld sp,$4278
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_27_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A72D),sp
    ld sp,$436C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_27_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A745),sp
    ld sp,$4378
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_28_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A75D),sp
    ld sp,$446C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_28_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A775),sp
    ld sp,$4478
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_29_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A78D),sp
    ld sp,$456C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_29_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A7A5),sp
    ld sp,$4578
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_30_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A7BD),sp
    ld sp,$466C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_30_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A7D5),sp
    ld sp,$4678
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_31_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A7ED),sp
    ld sp,$476C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_31_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A805),sp
    ld sp,$4778
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_32_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A81D),sp
    ld sp,$408C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_32_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A835),sp
    ld sp,$4098
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_33_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A84D),sp
    ld sp,$418C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_33_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A865),sp
    ld sp,$4198
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_34_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A87D),sp
    ld sp,$428C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_34_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A895),sp
    ld sp,$4298
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_35_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A8AD),sp
    ld sp,$438C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_35_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A8C5),sp
    ld sp,$4398
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_36_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A8DD),sp
    ld sp,$448C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_36_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A8F5),sp
    ld sp,$4498
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_37_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A90D),sp
    ld sp,$458C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_37_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A925),sp
    ld sp,$4598
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_38_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A93D),sp
    ld sp,$468C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_38_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A955),sp
    ld sp,$4698
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_39_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A96D),sp
    ld sp,$478C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_39_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A985),sp
    ld sp,$4798
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_40_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A99D),sp
    ld sp,$40AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_40_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A9B5),sp
    ld sp,$40B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_41_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A9CD),sp
    ld sp,$41AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_41_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A9E5),sp
    ld sp,$41B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_42_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($A9FD),sp
    ld sp,$42AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_42_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA15),sp
    ld sp,$42B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_43_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA2D),sp
    ld sp,$43AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_43_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA45),sp
    ld sp,$43B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_44_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA5D),sp
    ld sp,$44AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_44_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA75),sp
    ld sp,$44B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_45_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AA8D),sp
    ld sp,$45AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_45_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AAA5),sp
    ld sp,$45B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_46_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AABD),sp
    ld sp,$46AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_46_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AAD5),sp
    ld sp,$46B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_47_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AAED),sp
    ld sp,$47AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_47_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB05),sp
    ld sp,$47B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_48_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB1D),sp
    ld sp,$40CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_48_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB35),sp
    ld sp,$40D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_49_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB4D),sp
    ld sp,$41CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_49_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB65),sp
    ld sp,$41D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_50_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB7D),sp
    ld sp,$42CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_50_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AB95),sp
    ld sp,$42D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_51_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ABAD),sp
    ld sp,$43CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_51_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ABC5),sp
    ld sp,$43D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_52_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ABDD),sp
    ld sp,$44CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_52_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ABF5),sp
    ld sp,$44D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_53_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC0D),sp
    ld sp,$45CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_53_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC25),sp
    ld sp,$45D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_54_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC3D),sp
    ld sp,$46CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_54_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC55),sp
    ld sp,$46D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_55_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC6D),sp
    ld sp,$47CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_55_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC85),sp
    ld sp,$47D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_56_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AC9D),sp
    ld sp,$40EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_56_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ACB5),sp
    ld sp,$40F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_57_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ACCD),sp
    ld sp,$41EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_57_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ACE5),sp
    ld sp,$41F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_58_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ACFD),sp
    ld sp,$42EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_58_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD15),sp
    ld sp,$42F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_59_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD2D),sp
    ld sp,$43EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_59_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD45),sp
    ld sp,$43F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_60_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD5D),sp
    ld sp,$44EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_60_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD75),sp
    ld sp,$44F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_61_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AD8D),sp
    ld sp,$45EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_61_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ADA5),sp
    ld sp,$45F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_62_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ADBD),sp
    ld sp,$46EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_62_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ADD5),sp
    ld sp,$46F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_63_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($ADED),sp
    ld sp,$47EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_63_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE05),sp
    ld sp,$47F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_64_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE1D),sp
    ld sp,$480C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_64_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE35),sp
    ld sp,$4818
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_65_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE4D),sp
    ld sp,$490C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_65_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE65),sp
    ld sp,$4918
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_66_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE7D),sp
    ld sp,$4A0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_66_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AE95),sp
    ld sp,$4A18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_67_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AEAD),sp
    ld sp,$4B0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_67_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AEC5),sp
    ld sp,$4B18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_68_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AEDD),sp
    ld sp,$4C0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_68_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AEF5),sp
    ld sp,$4C18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_69_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF0D),sp
    ld sp,$4D0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_69_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF25),sp
    ld sp,$4D18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_70_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF3D),sp
    ld sp,$4E0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_70_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF55),sp
    ld sp,$4E18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_71_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF6D),sp
    ld sp,$4F0C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_71_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF85),sp
    ld sp,$4F18
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_72_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AF9D),sp
    ld sp,$482C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_72_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AFB5),sp
    ld sp,$4838
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_73_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AFCD),sp
    ld sp,$492C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_73_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AFE5),sp
    ld sp,$4938
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_74_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($AFFD),sp
    ld sp,$4A2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_74_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B015),sp
    ld sp,$4A38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_75_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B02D),sp
    ld sp,$4B2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_75_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B045),sp
    ld sp,$4B38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_76_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B05D),sp
    ld sp,$4C2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_76_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B075),sp
    ld sp,$4C38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_77_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B08D),sp
    ld sp,$4D2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_77_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B0A5),sp
    ld sp,$4D38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_78_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B0BD),sp
    ld sp,$4E2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_78_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B0D5),sp
    ld sp,$4E38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_79_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B0ED),sp
    ld sp,$4F2C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_79_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B105),sp
    ld sp,$4F38
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_80_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B11D),sp
    ld sp,$484C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_80_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B135),sp
    ld sp,$4858
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_81_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B14D),sp
    ld sp,$494C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_81_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B165),sp
    ld sp,$4958
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_82_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B17D),sp
    ld sp,$4A4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_82_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B195),sp
    ld sp,$4A58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_83_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B1AD),sp
    ld sp,$4B4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_83_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B1C5),sp
    ld sp,$4B58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_84_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B1DD),sp
    ld sp,$4C4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_84_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B1F5),sp
    ld sp,$4C58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_85_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B20D),sp
    ld sp,$4D4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_85_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B225),sp
    ld sp,$4D58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_86_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B23D),sp
    ld sp,$4E4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_86_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B255),sp
    ld sp,$4E58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_87_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B26D),sp
    ld sp,$4F4C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_87_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B285),sp
    ld sp,$4F58
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_88_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B29D),sp
    ld sp,$486C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_88_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B2B5),sp
    ld sp,$4878
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_89_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B2CD),sp
    ld sp,$496C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_89_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B2E5),sp
    ld sp,$4978
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_90_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B2FD),sp
    ld sp,$4A6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_90_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B315),sp
    ld sp,$4A78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_91_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B32D),sp
    ld sp,$4B6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_91_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B345),sp
    ld sp,$4B78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_92_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B35D),sp
    ld sp,$4C6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_92_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B375),sp
    ld sp,$4C78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_93_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B38D),sp
    ld sp,$4D6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_93_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B3A5),sp
    ld sp,$4D78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_94_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B3BD),sp
    ld sp,$4E6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_94_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B3D5),sp
    ld sp,$4E78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_95_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B3ED),sp
    ld sp,$4F6C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_95_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($8F00),sp
    ld sp,$4F78
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
    ld sp,(saved_sp)
    ret
ORG $B409
    ld (saved_sp),sp
row_96_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B426),sp
    ld sp,$488C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_96_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B43E),sp
    ld sp,$4898
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_97_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B456),sp
    ld sp,$498C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_97_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B46E),sp
    ld sp,$4998
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_98_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B486),sp
    ld sp,$4A8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_98_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B49E),sp
    ld sp,$4A98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_99_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B4B6),sp
    ld sp,$4B8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_99_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B4CE),sp
    ld sp,$4B98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_100_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B4E6),sp
    ld sp,$4C8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_100_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B4FE),sp
    ld sp,$4C98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_101_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B516),sp
    ld sp,$4D8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_101_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B52E),sp
    ld sp,$4D98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_102_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B546),sp
    ld sp,$4E8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_102_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B55E),sp
    ld sp,$4E98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_103_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B576),sp
    ld sp,$4F8C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_103_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B58E),sp
    ld sp,$4F98
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_104_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B5A6),sp
    ld sp,$48AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_104_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B5BE),sp
    ld sp,$48B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_105_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B5D6),sp
    ld sp,$49AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_105_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B5EE),sp
    ld sp,$49B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_106_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B606),sp
    ld sp,$4AAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_106_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B61E),sp
    ld sp,$4AB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_107_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B636),sp
    ld sp,$4BAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_107_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B64E),sp
    ld sp,$4BB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_108_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B666),sp
    ld sp,$4CAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_108_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B67E),sp
    ld sp,$4CB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_109_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B696),sp
    ld sp,$4DAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_109_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B6AE),sp
    ld sp,$4DB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_110_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B6C6),sp
    ld sp,$4EAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_110_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B6DE),sp
    ld sp,$4EB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_111_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B6F6),sp
    ld sp,$4FAC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_111_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B70E),sp
    ld sp,$4FB8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_112_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B726),sp
    ld sp,$48CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_112_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B73E),sp
    ld sp,$48D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_113_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B756),sp
    ld sp,$49CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_113_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B76E),sp
    ld sp,$49D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_114_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B786),sp
    ld sp,$4ACC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_114_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B79E),sp
    ld sp,$4AD8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_115_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B7B6),sp
    ld sp,$4BCC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_115_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B7CE),sp
    ld sp,$4BD8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_116_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B7E6),sp
    ld sp,$4CCC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_116_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B7FE),sp
    ld sp,$4CD8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_117_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B816),sp
    ld sp,$4DCC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_117_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B82E),sp
    ld sp,$4DD8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_118_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B846),sp
    ld sp,$4ECC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_118_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B85E),sp
    ld sp,$4ED8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_119_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B876),sp
    ld sp,$4FCC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_119_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B88E),sp
    ld sp,$4FD8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_120_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B8A6),sp
    ld sp,$48EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_120_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B8BE),sp
    ld sp,$48F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_121_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B8D6),sp
    ld sp,$49EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_121_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B8EE),sp
    ld sp,$49F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_122_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B906),sp
    ld sp,$4AEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_122_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B91E),sp
    ld sp,$4AF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_123_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B936),sp
    ld sp,$4BEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_123_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B94E),sp
    ld sp,$4BF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_124_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B966),sp
    ld sp,$4CEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_124_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B97E),sp
    ld sp,$4CF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_125_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B996),sp
    ld sp,$4DEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_125_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B9AE),sp
    ld sp,$4DF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_126_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B9C6),sp
    ld sp,$4EEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_126_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B9DE),sp
    ld sp,$4EF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_127_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($B9F6),sp
    ld sp,$4FEC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_127_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA0E),sp
    ld sp,$4FF8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_128_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA26),sp
    ld sp,$500C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_128_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA3E),sp
    ld sp,$5018
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_129_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA56),sp
    ld sp,$510C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_129_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA6E),sp
    ld sp,$5118
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_130_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA86),sp
    ld sp,$520C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_130_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BA9E),sp
    ld sp,$5218
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_131_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BAB6),sp
    ld sp,$530C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_131_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BACE),sp
    ld sp,$5318
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_132_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BAE6),sp
    ld sp,$540C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_132_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BAFE),sp
    ld sp,$5418
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_133_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB16),sp
    ld sp,$550C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_133_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB2E),sp
    ld sp,$5518
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_134_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB46),sp
    ld sp,$560C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_134_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB5E),sp
    ld sp,$5618
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_135_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB76),sp
    ld sp,$570C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_135_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BB8E),sp
    ld sp,$5718
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_136_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BBA6),sp
    ld sp,$502C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_136_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BBBE),sp
    ld sp,$5038
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_137_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BBD6),sp
    ld sp,$512C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_137_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BBEE),sp
    ld sp,$5138
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_138_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC06),sp
    ld sp,$522C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_138_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC1E),sp
    ld sp,$5238
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_139_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC36),sp
    ld sp,$532C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_139_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC4E),sp
    ld sp,$5338
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_140_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC66),sp
    ld sp,$542C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_140_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC7E),sp
    ld sp,$5438
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_141_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BC96),sp
    ld sp,$552C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_141_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BCAE),sp
    ld sp,$5538
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_142_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BCC6),sp
    ld sp,$562C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_142_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BCDE),sp
    ld sp,$5638
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_143_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BCF6),sp
    ld sp,$572C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_143_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD0E),sp
    ld sp,$5738
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_144_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD26),sp
    ld sp,$504C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_144_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD3E),sp
    ld sp,$5058
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_145_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD56),sp
    ld sp,$514C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_145_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD6E),sp
    ld sp,$5158
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_146_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD86),sp
    ld sp,$524C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_146_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BD9E),sp
    ld sp,$5258
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_147_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BDB6),sp
    ld sp,$534C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_147_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BDCE),sp
    ld sp,$5358
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_148_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BDE6),sp
    ld sp,$544C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_148_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BDFE),sp
    ld sp,$5458
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_149_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE16),sp
    ld sp,$554C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_149_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE2E),sp
    ld sp,$5558
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_150_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE46),sp
    ld sp,$564C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_150_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE5E),sp
    ld sp,$5658
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_151_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE76),sp
    ld sp,$574C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_151_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BE8E),sp
    ld sp,$5758
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_152_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BEA6),sp
    ld sp,$506C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_152_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BEBE),sp
    ld sp,$5078
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_153_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BED6),sp
    ld sp,$516C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_153_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BEEE),sp
    ld sp,$5178
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_154_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF06),sp
    ld sp,$526C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_154_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF1E),sp
    ld sp,$5278
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_155_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF36),sp
    ld sp,$536C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_155_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF4E),sp
    ld sp,$5378
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_156_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF66),sp
    ld sp,$546C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_156_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF7E),sp
    ld sp,$5478
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_157_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BF96),sp
    ld sp,$556C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_157_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BFAE),sp
    ld sp,$5578
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_158_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BFC6),sp
    ld sp,$566C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_158_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BFDE),sp
    ld sp,$5678
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_159_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($BFF6),sp
    ld sp,$576C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_159_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C00E),sp
    ld sp,$5778
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_160_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C026),sp
    ld sp,$508C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_160_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C03E),sp
    ld sp,$5098
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_161_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C056),sp
    ld sp,$518C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_161_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C06E),sp
    ld sp,$5198
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_162_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C086),sp
    ld sp,$528C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_162_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C09E),sp
    ld sp,$5298
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_163_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C0B6),sp
    ld sp,$538C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_163_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C0CE),sp
    ld sp,$5398
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_164_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C0E6),sp
    ld sp,$548C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_164_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C0FE),sp
    ld sp,$5498
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_165_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C116),sp
    ld sp,$558C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_165_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C12E),sp
    ld sp,$5598
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_166_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C146),sp
    ld sp,$568C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_166_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C15E),sp
    ld sp,$5698
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_167_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C176),sp
    ld sp,$578C
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_167_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C18E),sp
    ld sp,$5798
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_168_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C1A6),sp
    ld sp,$50AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_168_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C1BE),sp
    ld sp,$50B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_169_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C1D6),sp
    ld sp,$51AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_169_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C1EE),sp
    ld sp,$51B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_170_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C206),sp
    ld sp,$52AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_170_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C21E),sp
    ld sp,$52B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_171_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C236),sp
    ld sp,$53AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_171_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C24E),sp
    ld sp,$53B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_172_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C266),sp
    ld sp,$54AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_172_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C27E),sp
    ld sp,$54B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_173_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C296),sp
    ld sp,$55AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_173_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C2AE),sp
    ld sp,$55B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_174_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C2C6),sp
    ld sp,$56AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_174_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C2DE),sp
    ld sp,$56B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_175_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C2F6),sp
    ld sp,$57AC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_175_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C30E),sp
    ld sp,$57B8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_176_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C326),sp
    ld sp,$50CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_176_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C33E),sp
    ld sp,$50D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_177_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C356),sp
    ld sp,$51CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_177_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C36E),sp
    ld sp,$51D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_178_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C386),sp
    ld sp,$52CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_178_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C39E),sp
    ld sp,$52D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_179_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C3B6),sp
    ld sp,$53CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_179_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C3CE),sp
    ld sp,$53D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_180_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C3E6),sp
    ld sp,$54CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_180_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C3FE),sp
    ld sp,$54D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_181_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C416),sp
    ld sp,$55CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_181_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C42E),sp
    ld sp,$55D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_182_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C446),sp
    ld sp,$56CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_182_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C45E),sp
    ld sp,$56D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_183_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C476),sp
    ld sp,$57CC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_183_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C48E),sp
    ld sp,$57D8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_184_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C4A6),sp
    ld sp,$50EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_184_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C4BE),sp
    ld sp,$50F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_185_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C4D6),sp
    ld sp,$51EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_185_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C4EE),sp
    ld sp,$51F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_186_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C506),sp
    ld sp,$52EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_186_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C51E),sp
    ld sp,$52F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_187_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C536),sp
    ld sp,$53EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_187_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C54E),sp
    ld sp,$53F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_188_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C566),sp
    ld sp,$54EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_188_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C57E),sp
    ld sp,$54F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_189_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C596),sp
    ld sp,$55EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_189_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C5AE),sp
    ld sp,$55F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_190_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C5C6),sp
    ld sp,$56EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_190_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C5DE),sp
    ld sp,$56F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_191_0:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($C5F6),sp
    ld sp,$57EC
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
row_191_1:
    ld sp,0
    pop bc
    pop de
    pop hl
    exx
    pop bc
    pop de
    pop hl
    ld ($8F00),sp
    ld sp,$57F8
    push hl
    push de
    push bc
    exx
    push hl
    push de
    push bc
    ld sp,(saved_sp)
    ret