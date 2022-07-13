
def string_sequence(n: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive.
    >>> string_sequence(100)
    '0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54	55	56	57	58	59	60	61	62	63	64	65	66	67	68	69	70	71	72	73	74	75	76	77	78	79	80	81	82	83	84	85	86	87	88	89	90	91	92	93	94	95	96	97	98	99'
    """
    return '\t'.join(str(i) for i in range(n))


def string_sequence_with_step(n: int, step: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive with a given step.
    >>> string_sequence_with_step(100, 10)
    '0	10	20	30	40	50	60	70	80	90'
    """
    return '\t'.join(str(i) for i in range(0, n, step))


def string_sequence_with_step_and_offset(n: int, step: int, offset: int) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive with a given step and offset.
    >>> string_sequence_with_step_and_offset(100, 10, 5)
    '5	15	25	35	45	55	65	75	85	95'
    """
    return '\t'.join(str(i) for i in range(offset, n, step))


def string_sequence_with_step_and_offset_and_prefix(n: int, step: int, offset: int, prefix: str) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive with a given step and offset.
    >>> string_sequence_with_step_and_offset_and_prefix(100, 10, 5, 'chr')
    'chr5	chr15	chr25	chr35	chr45	chr55	chr65	chr75	chr85	chr95'
    """
    return '\t'.join(prefix + str(i) for i in range(offset, n, step))


def string_sequence_with_step_and_offset_and_prefix_and_suffix(n: int, step: int, offset: int, prefix: str, suffix: str) -> str:
    """ Return a string containing tab-delimited numbers starting from 0 upto n exclusive with a given step and offset.
    >>> string_sequence_with_step_and