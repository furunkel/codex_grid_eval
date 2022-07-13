
def string_sequence(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(100)
    '0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99'
    """
    return f'0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\t29\t30\t31\t32\t33\t34\t35\t36\t37\t38\t39\t40\t41\t42\t43\t44\t45\t46\t47\t48\t49\t50\t51\t52\t53\t54\t55\t56\t57\t58\t59\t60\t61\t62\t63\t64\t65\t66\t67\t68\t69\t70\t71\t72\t73\t74\t75\t76\t77\t78\t79\t80\t81\t82\t83\t84\t85\t86\t87\t88\t89\t90\t91\t92\t93\t94\t95\t96\t97\t98\t99'


@njit
def string_sequence_with_spaces(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence_with_spaces(100)
    '0	1 	2 	3 	4	5 	6 	7 	8 	9 	10 	11 	12 	13 	14 	15 	16 	17 	18 	19 	20 	21 	22 	23 	24 	25 	26 	27 	28 	29 	30 	31 	32 	33 	34 	35 	36 	37 	38 	39 	40 	41 	42 	43 	44 	45 	46 	47 	48 	49 	50 	51 	52 	53 	54 	55 	56 	57 	58 	59 	60 	61 	62 	63 	64 	65 	66 	67 	68 	69 	70 	71 	72 	73 	74 	75 	76 	77 	78 	79 	80 	81 	82 	83 	84 	85 	86 	87 	88 	89 	90 	91 	92 	93 	94 	95 	96 	97 	98 	99'
    """
    return f'0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12