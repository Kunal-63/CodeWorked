import mysql.connector as con
import csv 

mydb = con.connect(host="localhost", user="root", passwd="root", database="airport_school_new")
cursor = mydb.cursor()

academic_gr = [
3956
,3957
,3958
,3959
,3960
,3961
,3962
,3963
,3964
,3965
,3966
,3967
,3969
,3970
,3971
,3972
,3973
,3974
,3975
,3976
,3977
,3978
,3979
,3980
,3981
,3982
,3983
,3984
,3985
,3986
,3987
,3988
,3989
,3990
,3991
,3992
,3993
,3994
,3995
,3997
,3998
,3999
,4000
,4001
,4002
,4003
,4004
,4005
,4006
,4007
,4008
,4009
,4010
,4011
,4012
,4013
,4014
,4015
,4016
,4017
,4018
,4020
,4021
,4023
,4024
,4025
,4026
,4027
,4028
,4029
,4030
,4031
,4032
,4033
,4034
,4035
,4036
,4037
,4038
,4039
,4040
,4041
,4042
,4043
,4044
,4045
,4046
,4048
,4049
,4050
,4051
,4052
,4053
,4054
,4055
,4056
,4057
,4058
,4059
,4060
,4061
,4062
,4063
,4064
,4065
,4067
,4068
,4069
,4070
,4071
,4072
,4073
,4074
,4075
,4078
,4079
,4080
,4081
,4082
,4083
,4084
,4085
,4086
,4087
,4088
,4089
,4090
,4091
,4092
,4093
,4094
,4096
,4097
,4098
,4100
,4101
,4102
,4103
,4104
,4105
,4107
,4108
,4112
,4130
,4131
,4133
,4217
,4445
,4446
,4448
,4454
,4456
,4457
,4500
,4501
,4713
,4714
,4715
,4716
,4728
,4736
,4737
,4782
,4786
,4794
,4576
,4577
,4578
,4579
,4580
,4581
,4582
,4583
,4584
,4585
,4586
,4587
,4588
,4589
,4590
,4591
,4592
,4593
,4594
,4595
,4596
,4597
,4598
,4599
,4600
,4601
,4602
,4603
,4604
,4605
,4606
,4607
,4608
,4609
,4610
,4611
,4612
,4613
,4614
,4615
,4616
,4617
,4618
,4619
,4620
,4621
,4622
,4623
,4624
,4625
,4626
,4627
,4628
,4629
,4630
,4631
,4632
,4633
,4634
,4635
,4636
,4637
,4638
,4639
,4640
,4641
,4642
,4643
,4644
,4645
,4646
,4647
,4648
,4649
,4650
,4651
,4652
,4653
,4654
,4655
,4656
,4657
,4658
,4659
,4660
,4661
,4662
,4663
,4664
,4665
,4666
,4667
,4668
,4669
,4670
,4671
,4672
,4673
,4674
,4675
,4676
,4677
,4678
,4679
,4680
,4681
,4682
,4683
,4684
,4685
,4686
,4687
,4688
,4689
,4690
,4692
,4693
,4694
,4695
,4696
,4697
,4698
,4699
,4700
,4701
,4702
,4703
,4704
,4705
,4706
,4707
,4708
,4709
,4729
,4734
,4790
,4229
,4230
,4231
,4232
,4233
,4234
,4235
,4236
,4237
,4238
,4239
,4240
,4241
,4242
,4243
,4244
,4245
,4246
,4247
,4248
,4249
,4250
,4251
,4252
,4253
,4254
,4255
,4256
,4257
,4258
,4259
,4260
,4261
,4262
,4263
,4264
,4265
,4266
,4267
,4268
,4269
,4271
,4272
,4273
,4274
,4275
,4276
,4277
,4278
,4279
,4280
,4281
,4282
,4283
,4284
,4285
,4286
,4287
,4288
,4289
,4290
,4291
,4292
,4293
,4294
,4295
,4296
,4297
,4298
,4299
,4300
,4301
,4302
,4303
,4304
,4305
,4306
,4307
,4308
,4309
,4310
,4311
,4312
,4313
,4315
,4316
,4317
,4318
,4319
,4320
,4321
,4322
,4323
,4324
,4325
,4326
,4327
,4328
,4329
,4330
,4331
,4332
,4333
,4334
,4335
,4336
,4337
,4338
,4339
,4340
,4341
,4342
,4343
,4344
,4345
,4346
,4347
,4348
,4350
,4351
,4352
,4353
,4354
,4355
,4356
,4357
,4358
,4359
,4360
,4361
,4362
,4363
,4365
,4367
,4368
,4369
,4370
,4371
,4449
,4461
,4474
,4496
,4509
,4517
,4710
,4711
,4712
,4735
,4738
,4742
,4778
,1370
,1381
,1385
,1391
,1398
,1410
,1422
,1427
,1437
,1442
,1452
,1479
,1480
,1505
,1654
,1763
,1993
,2602
,2753
,2758
,2768
,3025
,3075
,3591
,4220
,4774
,4775
,4776
,4777
,4784
,4785
,4787
,4789
,1282
,1366
,1368
,1369
,1371
,1372
,1373
,1374
,1375
,1376
,1377
,1378
,1379
,1380
,1382
,1384
,1387
,1392
,1393
,1395
,1396
,1399
,1400
,1401
,1402
,1404
,1405
,1406
,1407
,1408
,1411
,1413
,1415
,1416
,1417
,1418
,1419
,1420
,1424
,1425
,1426
,1431
,1433
,1434
,1435
,1438
,1439
,1440
,1441
,1443
,1444
,1446
,1447
,1450
,1451
,1455
,1457
,1459
,1460
,1463
,1484
,1492
,1494
,1516
,1518
,1519
,1521
,1522
,1664
,1674
,1679
,1692
,1771
,2095
,2100
,2115
,2117
,2121
,2155
,2522
,2603
,2746
,2804
,2874
,3085
,3086
,3087
,3088
,3089
,3361
,3365
,4114
,4115
,4206
,1502
,1821
,1822
,1823
,1825
,1826
,1827
,1829
,1830
,1831
,1832
,1835
,1836
,1837
,1838
,1842
,1843
,1845
,1847
,1848
,1849
,1851
,1852
,1854
,1855
,1856
,1858
,1861
,1862
,1864
,1866
,1868
,1869
,1874
,1878
,1879
,1881
,1885
,1887
,1888
,1889
,1897
,1899
,1924
,1926
,1927
,1928
,1936
,1940
,1941
,1945
,1960
,1965
,1970
,1985
,1989
,1992
,2040
,2041
,2043
,2044
,2045
,2046
,2048
,2050
,2052
,2053
,2054
,2057
,2060
,2064
,2065
,2066
,2067
,2077
,2084
,2097
,2103
,2109
,2112
,2120
,2169
,2175
,2264
,2276
,2299
,2300
,2336
,2340
,2495
,2496
,2497
,2516
,2518
,2521
,2554
,2565
,2764
,2771
,2845
,3020
,3022
,3026
,3037
,3038
,3059
,3117
,3360
,3362
,3401
,3433
,3583
,3585
,3832
,3850
,4138
,4411
,4414
,4416
,4417
,4418
,4419
,4420
,4421
,4422
,4423
,4424
,4425
,4426
,4427
,4428
,4429
,4430
,4431
,4432
,4460
,4462
,4467
,4468
,4473
,4480
,4483
,4485
,4486
,4488
,4491
,4492
,4494
,4498
,4506
,4508
,4510
,4515
,4516
,4552
,4723
,4727
,4732
,4792
,1998
,1999
,2000
,2001
,2003
,2005
,2006
,2008
,2010
,2011
,2012
,2013
,2014
,2015
,2016
,2017
,2018
,2019
,2020
,2021
,2024
,2025
,2026
,2028
,2029
,2030
,2031
,2033
,2034
,2035
,2037
,2055
,2058
,2059
,2061
,2062
,2063
,2068
,2073
,2074
,2075
,2076
,2081
,2082
,2083
,2092
,2094
,2116
,2118
,2122
,2127
,2128
,2129
,2130
,2131
,2146
,2159
,2160
,2178
,2179
,2188
,2190
,2197
,2202
,2205
,2208
,2227
,2230
,2235
,2236
,2252
,2254
,2257
,2258
,2266
,2271
,2274
,2279
,2280
,2289
,2290
,2298
,2301
,2329
,2335
,2480
,2481
,2482
,2484
,2489
,2525
,2542
,2568
,2592
,2594
,2630
,2742
,2744
,2767
,2777
,2811
,2858
,2862
,2863
,2864
,2865
,2866
,2867
,2873
,2876
,2877
,3021
,3035
,3045
,3080
,3120
,3609
,3655
,3665
,3849
,3910
,4117
,4136
,4394
,4395
,4396
,4397
,4398
,4399
,4400
,4401
,4402
,4403
,4404
,4405
,4406
,4407
,4408
,4409
,4410
,4476
,4495
,4497
,4512
,4513
,4518
,4553
,4556
,4573
,4780
,2080
,2195
,2196
,2198
,2199
,2201
,2203
,2206
,2207
,2209
,2210
,2211
,2212
,2213
,2214
,2215
,2216
,2217
,2218
,2219
,2220
,2221
,2223
,2224
,2225
,2226
,2228
,2229
,2232
,2233
,2234
,2237
,2238
,2239
,2240
,2241
,2242
,2243
,2244
,2245
,2246
,2247
,2248
,2249
,2250
,2251
,2260
,2262
,2263
,2267
,2268
,2269
,2270
,2272
,2273
,2291
,2293
,2296
,2297
,2311
,2313
,2316
,2318
,2320
,2321
,2322
,2333
,2338
,2339
,2355
,2358
,2376
,2377
,2383
,2384
,2388
,2396
,2441
,2442
,2443
,2444
,2445
,2446
,2447
,2448
,2450
,2451
,2452
,2455
,2457
,2458
,2462
,2463
,2464
,2468
,2469
,2487
,2530
,2629
,2656
,2727
,2730
,2731
,2766
,3015
,3016
,3017
,3018
,3019
,3055
,3056
,3060
,3064
,3073
,3129
,3130
,3131
,3132
,3135
,3136
,3138
,3139
,3341
,3342
,3343
,3344
,3346
,3347
,3348
,3443
,3588
,3653
,3661
,3848
,4106
,4127
,4139
,4222
,4379
,4380
,4381
,4382
,4383
,4384
,4385
,4386
,4387
,4388
,4389
,4390
,4391
,4392
,4393
,4452
,4453
,4487
,4502
,4514
,4731
,4739
,4779
,4795
,2389
,2390
,2391
,2392
,2393
,2394
,2395
,2397
,2398
,2399
,2400
,2401
,2402
,2403
,2404
,2405
,2406
,2407
,2408
,2409
,2410
,2411
,2412
,2413
,2414
,2415
,2416
,2417
,2418
,2419
,2420
,2421
,2422
,2423
,2424
,2426
,2427
,2429
,2430
,2431
,2432
,2433
,2434
,2435
,2436
,2437
,2438
,2439
,2453
,2454
,2460
,2461
,2465
,2470
,2471
,2472
,2475
,2477
,2478
,2479
,2486
,2488
,2490
,2491
,2492
,2515
,2523
,2524
,2526
,2531
,2574
,2591
,2604
,2605
,2606
,2608
,2609
,2610
,2611
,2612
,2613
,2614
,2615
,2616
,2617
,2619
,2620
,2621
,2622
,2624
,2625
,2627
,2671
,2673
,2674
,2676
,2678
,2679
,2682
,2683
,2707
,2708
,2711
,2712
,2720
,2722
,2723
,2726
,2729
,2787
,2808
,2813
,2846
,2856
,3034
,3036
,3043
,3053
,3143
,3340
,3350
,3353
,3354
,3355
,3370
,3371
,3374
,3375
,3376
,3377
,3379
,3380
,3382
,3383
,3384
,3385
,3386
,3388
,3389
,3391
,3392
,3393
,3396
,3397
,3399
,3446
,3447
,3448
,3451
,3582
,3590
,3595
,3845
,3846
,3847
,3913
,4128
,4211
,4372
,4373
,4374
,4375
,4376
,4377
,4378
,4507
,4725
,4730
,4793
,2631
,2634
,2636
,2637
,2638
,2640
,2641
,2642
,2643
,2644
,2645
,2646
,2647
,2648
,2649
,2650
,2651
,2652
,2653
,2654
,2655
,2657
,2658
,2659
,2660
,2662
,2663
,2664
,2665
,2666
,2667
,2668
,2669
,2670
,2672
,2675
,2680
,2684
,2685
,2687
,2688
,2689
,2690
,2691
,2692
,2693
,2694
,2695
,2696
,2697
,2699
,2701
,2702
,2703
,2704
,2706
,2714
,2716
,2717
,2719
,2721
,2732
,2734
,2735
,2736
,2737
,2739
,2740
,2745
,2752
,2756
,2757
,2761
,2769
,2775
,2794
,2796
,2797
,2798
,2799
,2800
,2809
,2810
,2815
,2821
,2829
,2841
,2843
,2847
,2850
,2851
,2853
,2854
,2855
,2869
,2872
,2879
,2987
,2988
,2989
,2990
,2991
,2992
,2993
,2996
,2997
,2998
,3000
,3001
,3002
,3003
,3012
,3013
,3014
,3046
,3063
,3069
,3074
,3108
,3111
,3149
,3329
,3330
,3331
,3332
,3333
,3335
,3337
,3338
,3339
,3351
,3352
,3400
,3449
,3605
,3608
,3612
,3615
,3616
,3617
,3618
,3619
,3620
,3621
,3622
,3623
,3624
,3625
,3626
,3627
,3628
,3629
,3630
,3631
,3632
,3633
,3634
,3635
,3636
,3637
,3645
,3656
,3657
,3658
,3659
,3660
,3867
,3954
,4140
,4554
,4722
,4724
,4741
,4744
,2880
,2881
,2882
,2883
,2884
,2885
,2886
,2887
,2888
,2889
,2890
,2891
,2892
,2893
,2894
,2895
,2896
,2900
,2901
,2902
,2903
,2904
,2905
,2906
,2907
,2908
,2909
,2910
,2911
,2912
,2913
,2914
,2915
,2916
,2917
,2918
,2919
,2920
,2921
,2922
,2923
,2925
,2926
,2927
,2928
,2929
,2930
,2933
,2934
,2935
,2936
,2937
,2938
,2939
,2940
,2941
,2942
,2943
,2944
,2945
,2946
,2947
,2948
,2949
,2950
,2951
,2953
,2954
,2955
,2956
,2957
,2958
,2959
,2960
,2961
,2962
,2963
,2964
,2965
,2967
,2968
,2969
,2971
,2972
,2973
,2974
,2975
,2976
,2977
,2978
,2979
,2980
,2981
,2983
,2984
,2985
,2986
,3004
,3005
,3006
,3007
,3008
,3009
,3010
,3011
,3044
,3071
,3082
,3107
,3145
,3281
,3282
,3283
,3284
,3285
,3286
,3287
,3288
,3289
,3290
,3291
,3292
,3294
,3295
,3296
,3297
,3298
,3299
,3300
,3301
,3303
,3304
,3305
,3306
,3307
,3308
,3310
,3312
,3313
,3314
,3315
,3316
,3317
,3318
,3319
,3320
,3323
,3324
,3327
,3421
,3442
,3445
,3647
,3654
,3662
,3831
,3842
,3843
,3844
,3856
,3858
,3862
,3865
,3866
,3920
,3921
,3923
,3926
,3928
,3929
,3930
,3931
,3932
,3934
,3935
,3936
,3937
,3940
,3941
,3942
,3943
,3945
,3947
,3948
,3949
,3951
,3952
,4201
,4349
,4447
,4511
,4561
,4574
,3157
,3158
,3159
,3160
,3161
,3162
,3163
,3164
,3165
,3166
,3167
,3168
,3169
,3170
,3171
,3172
,3173
,3174
,3175
,3176
,3177
,3178
,3179
,3181
,3182
,3183
,3184
,3186
,3187
,3188
,3189
,3190
,3191
,3192
,3193
,3194
,3196
,3197
,3198
,3199
,3200
,3201
,3202
,3203
,3204
,3205
,3206
,3207
,3208
,3209
,3210
,3211
,3212
,3213
,3214
,3215
,3216
,3217
,3218
,3219
,3220
,3221
,3222
,3223
,3224
,3226
,3227
,3228
,3229
,3230
,3231
,3232
,3233
,3234
,3236
,3237
,3238
,3240
,3241
,3242
,3243
,3244
,3245
,3246
,3247
,3248
,3249
,3251
,3252
,3253
,3254
,3255
,3257
,3259
,3260
,3261
,3262
,3263
,3264
,3268
,3269
,3272
,3273
,3274
,3275
,3276
,3277
,3278
,3279
,3280
,3321
,3326
,3450
,3575
,3576
,3579
,3593
,3594
,3599
,3603
,3652
,3668
,3669
,3834
,3838
,3839
,3840
,3841
,3871
,3917
,3953
,4132
,4137
,4142
,4143
,4144
,4145
,4146
,4147
,4148
,4149
,4150
,4151
,4152
,4153
,4154
,4155
,4156
,4157
,4158
,4159
,4160
,4161
,4162
,4163
,4164
,4165
,4166
,4168
,4169
,4170
,4171
,4204
,4212
,4214
,4215
,4219
,4226
,4444
,4451
,4503
,4504
,4555
,4567
,4719
,4721
,4743
,4791
,3452
,3453
,3454
,3455
,3457
,3458
,3460
,3462
,3463
,3464
,3465
,3466
,3467
,3468
,3469
,3470
,3471
,3472
,3473
,3474
,3475
,3476
,3477
,3478
,3479
,3480
,3481
,3482
,3483
,3484
,3485
,3486
,3487
,3488
,3489
,3490
,3491
,3492
,3493
,3494
,3495
,3497
,3498
,3499
,3500
,3502
,3504
,3505
,3506
,3507
,3508
,3509
,3510
,3511
,3512
,3513
,3514
,3515
,3516
,3517
,3518
,3519
,3520
,3521
,3522
,3523
,3524
,3525
,3526
,3527
,3528
,3529
,3530
,3531
,3532
,3533
,3534
,3535
,3536
,3538
,3539
,3540
,3541
,3542
,3543
,3544
,3545
,3546
,3547
,3548
,3549
,3550
,3551
,3552
,3553
,3554
,3555
,3556
,3557
,3558
,3559
,3560
,3561
,3562
,3563
,3564
,3565
,3566
,3567
,3568
,3569
,3570
,3573
,3577
,3580
,3587
,3827
,3828
,3835
,3836
,3837
,3854
,3857
,3911
,3946
,4095
,4099
,4118
,4119
,4223
,4224
,4225
,4364
,4464
,4490
,4519
,4520
,4521
,4522
,4523
,4524
,4525
,4526
,4527
,4528
,4529
,4530
,4531
,4532
,4533
,4534
,4535
,4536
,4538
,4539
,4540
,4541
,4542
,4543
,4544
,4545
,4546
,4547
,4549
,4550
,4551
,4557
,4558
,4717
,4718
,4720
,4733
,4745
,4783
,3670
,3671
,3672
,3673
,3674
,3675
,3676
,3677
,3678
,3679
,3680
,3681
,3682
,3683
,3685
,3686
,3687
,3688
,3689
,3690
,3691
,3692
,3693
,3694
,3695
,3696
,3697
,3698
,3699
,3700
,3701
,3702
,3703
,3704
,3705
,3706
,3707
,3708
,3709
,3710
,3711
,3712
,3713
,3715
,3716
,3717
,3718
,3719
,3720
,3721
,3722
,3723
,3724
,3725
,3726
,3727
,3728
,3729
,3730
,3732
,3733
,3734
,3735
,3736
,3737
,3738
,3739
,3740
,3741
,3742
,3745
,3746
,3747
,3749
,3751
,3752
,3753
,3756
,3757
,3758
,3759
,3760
,3762
,3763
,3764
,3765
,3766
,3767
,3769
,3771
,3772
,3773
,3774
,3775
,3776
,3777
,3778
,3779
,3780
,3781
,3782
,3783
,3784
,3785
,3786
,3787
,3788
,3791
,3793
,3795
,3796
,3797
,3798
,3800
,3802
,3803
,3804
,3806
,3807
,3808
,3809
,3810
,3811
,3814
,3815
,3816
,3818
,3819
,3820
,3821
,3822
,3823
,3824
,3826
,3829
,3830
,3863
,3864
,3868
,3916
,3955
,4109
,4111
,4121
,4124
,4134
,4208
,4221
,4227
,4228
,4450
,4455
,4466
,4548
,4559
,4560
,4575
,4726
,4740
,4746
,4747
,4748
,4749
,4750
,4751
,4752
,4753
,4754
,4755
,4756
,4757
,4758
,4759
,4760
,4761
,4762
,4763
,4764
,4765
,4766
,4767
,4768
,4769
,4770
,4771
,4772
,4773
,4781
,4788

]

with open(r"D:\ZETA CORE 2023-24\BACKUP\exmp_fees.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
       
        try:

            # if int(row[0]) in academic_gr:
            #     print(row)
                # cursor.execute('delete from academic_detail where gr_no=%s', (row[0],))
                # cursor.execute('delete from gr_check where gr_no=%s', (row[0],))
                # cursor.execute('delete from pending_fee_detail where gr_no=%s', (row[0],))
            cursor.execute("insert into exmp_fees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
                # cursor.execute('insert into academic_detail values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
                
                # cursor.execute("select * from std_fees where std='{}'".format(row[11]))
                # data = cursor.fetchall()
                # cursor.execute("insert into pending_fee_detail values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[row[0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6],data[0][7],data[0][8],data[0][9],data[0][10],data[0][11],data[0][12]])
                # cursor.execute("insert into gr_check values({},0,0,0,0,0,0,0)".format(row[0]))
                # cursor.execute("insert into fee_details values({},' ',' ',' ',' ',' ',' ',' ')".format(row[0]))
        except:
            pass
        mydb.commit()

