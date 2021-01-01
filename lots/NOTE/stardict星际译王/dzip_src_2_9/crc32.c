unsigned long crcval;
unsigned long crctable[256];

unsigned long crc_reflect(unsigned long x, int bits)
{
	int i;
	unsigned long v = 0, b = 1 << (bits - 1);

	for (i = 0; i < bits; i++)
	{
		if (x & 1) v += b;
		x >>= 1; b >>= 1;
	}
	return v;
}

void crc_init(void)
{
	unsigned long crcpol = 0x04c11db7;
	unsigned long i, j, k;

	for (i = 0; i < 256; i++)
	{
		k = crc_reflect(i,8) << 24;
		for (j = 0; j < 8; j++)
			k = (k << 1) ^ ((k & 0x80000000)? crcpol : 0);
		crctable[i] = crc_reflect(k,32);
	}
}

void make_crc (unsigned char *ptr, int len)
{
	while (len--)
		crcval = (crcval >> 8) ^ crctable[(crcval & 0xff) ^ *ptr++];
}
