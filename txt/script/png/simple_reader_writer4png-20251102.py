#__all__:goto
r'''[[[
e script/png/simple_reader_writer4png-20251102.py
[[
@20251102
cp -iv script/png/simple_reader_writer4png.py ../../python3_src/nn_ns/fileformat/png/
mv -iv script/png/simple_reader_writer4png.py script/png/simple_reader_writer4png-20251102.py
e ../../python3_src/nn_ns/fileformat/png/simple_reader_writer4png.py
]]

e script/png/simple_reader_writer4png.py
view script/png/site-packages/png/png.py
view script/png/site-packages/PIL/PngImagePlugin.py

script.png.simple_reader_writer4png
py -m nn_ns.app.debug_cmd   script.png.simple_reader_writer4png -x # -off_defs
py -m nn_ns.app.doctest_cmd script.png.simple_reader_writer4png:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %script.png.simple_reader_writer4png:cls@T    =T   +exclude_attrs5listed_in_cls_doc

#######
[[
new concepts:
    segment
    xpixel
    [segment =[def]= (palette_index|sample)]
    [xpixel =[def]= (boxed_palette_index|pixel)]
        [xpixel :: [segment]{len<-[1..=4]}]
        [pixel :: [sample]{len<-[1..=4]}]
        [boxed_palette_index :: [palette_index]{len==1}]
        [boxed_palette_index == (palette_index,)]


rename:
    pixel_entry --> segment
    sample_depth7uniform --> num_bits4sample7png
    bit_depth --> num_bits4segment
    8rows --> jrow2
    _per_ --> 4
    jinterlace -> jpass
    height_width_pair -> hw_size
    size4canvas --> wh_size4canvas
    size4reduced_image -> wh_size4reduced_image
]]


'#'; __doc__ = r'#'
>>>



#load:
py_adhoc_call   script.png.simple_reader_writer4png   ,load_png_file__mx8src_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/串联同文.png
py_adhoc_call   script.png.simple_reader_writer4png   @load_png_file8pixel_matrix7RGBA4src_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/串联同文.png



#convert{load,dump}:
py_adhoc_call   script.png.simple_reader_writer4png   @convert_png_file__switch01_interlace_method_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/串联同文.png   =None

py_adhoc_call   script.png.simple_reader_writer4png   @convert_png_file__switch01_interlace_method_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/串联同文.png   :../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-串联同文.png

py_adhoc_call   script.png.simple_reader_writer4png   @convert_png_file__switch01_interlace_method_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/串联同文.png   :../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-串联同文.png

py_adhoc_call   script.png.simple_reader_writer4png   @convert_png_file__switch01_interlace_method_   :../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-串联同文.png   :../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-tmp-串联同文.png

rm -iv ../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-串联同文.png ../../python3_src/haskell_src/Framework4Translation-ver5-images/tmp-tmp-串联同文.png

]]]'''#'''
__all__ = r'''
convert_png_file__switch01_interlace_method_
    load_png_file__both_mx8src_and_mx8png_
        load_png_file__mx8src_
        load_png_file__mx8png_
        load_png_file8pixel_matrix7RGBA4src_
    dump_png_file__pixel_matrix7RGBA4src_
        preprocess__pixel_matrix7RGBA4src_







png_file_signature
BaseError
    Error__eof
    Error__IDAT
    Error__PLTE__palette7RGB
    Error__bKGD
    Error__bit_depth
    Error__bytes_not_matched
    Error__chunk_infos_filled
    Error__chunk_infos_not_filled
    Error__chunk_length__IHDR
    Error__chunk_type
    Error__chunk_type__IDAT__decompressobj__eof
    Error__chunk_type__IDAT__decompressobj__unconsumed_tail
    Error__chunk_type__IDAT__decompressobj__unused_data
    Error__chunk_type__tRNS__alpha_used
    Error__chunk_type__unknown_critical
    Error__crc
    Error__key_existed
    Error__not_perfect_div
    Error__png_uint_31bit_overflow
    Error__png_uint_7bit_overflow
    Error__range
    Error__sBIT
    Error__tRNS__palette7A
    Error__tRNS__pixel7L8fully_transparent
    Error__tRNS__pixel7RGB8fully_transparent

    Error__segment
    Error__num_bits4segment
    Error__sample_depths7XXX4src
    Error__alpha_separation


mk_max_sample5depth_

fmap_tmay_
may2tmay_
may5tmay_

calc_crc32_
    validate_crc32_
perfect_div

ColorType4png
    Data4ColorType4png
    Nicknames4ColorType4png

IReadablePixelMatrix7RGBA
IWritablePixelMatrix7RGBA
    MutablePixelMatrix7RGBA

Reader4png
    load_png_file__both_mx8src_and_mx8png_
        load_png_file__mx8src_
        load_png_file__mx8png_
    load_png_file8pixel_matrix7RGBA4src_

    read_ex__seq_
    read_ex__bytes__size_le_
    read_ex__bytes__size_eq_
    decode8uint_BE_
        read_ex__uint_7bit_1byte_BE_
        read_ex__uint_31bit_4byte_BE_
        read_ex__uint_8bit_1byte_BE_
        read_ex__uint_16bit_2byte_BE_
        read_ex__uint_32bit_4byte_BE_
        read_ex__uint_BE__size_eq_

decode_IDAT_
    prepare4parse_IDAT__1_
    prepare4parse_IDAT__2_

    decompressX_
    split_into_scanlines_
        iter_split__rngs_
        iter_split__num_rows_
        iter_split__num_columns__last_row_incomplete__5iterator_
        iter_split__num_columns__last_row_incomplete__5seq_
    inv_filterX_
        inv_filter0__reduced_image_
    reconstruct_xpixels_
        xpixels5bytes8row_
        iter_split_bytes_into_uints__num_bits4uint_
    reconstruct_spng_image7xpixel_
    reconstruct_spng_image7pixel7RGBA_
        prepare4parse_IDAT__3_
    reconstruct_src_image7pixel7RGBA_
        fmap__lsls_


    mk_may_palette7RGBA_
    mk_sample_depth7uniform5bit_depth_
    mk_sample_depths7RGBA4png_
    mk_sample_depths7RGBA4src_
    mk_default_sample_depth7A4src__no_sBIT_
    mk_sample_depths7RGBA4src5sBIT_


jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace
    jpass2begin_step_pairs4jrow__4Adam7_interlace
    jpass2begin_step_pairs4jcolumn__4Adam7_interlace
    jpass2hw_size4macro_pixel4filling__4Adam7_interlace

    prepare4no_interlace_
    prepare4Adam7_interlace_

FilterType4filter_method0
    Predictors4filter_method0
    iter4filter_method0_
    inv_filter_method0_
    filter_method0_
        filter_method0__adaptive_






check_chunk_type__png_ver3_
is_ancillary__chunk_type_
check_five_byte_uints6IHDR_
check_wh_size4canvas
    check_pint_31bit_
    check_uint_31bit_

check_sample_depths7RGBA4src_
    check_matrix_shape__wh_
check_all_all_
    check_pixel_matrix7XXX_
    check_pixel7XXX_
check_may_pixel7XXX_




encode__seq_
encode__uint_BE__size_eq_
    encode__uint_4byte_BE_
    encode__uint_2byte_BE_

Writer4png
    write__png_file_signature_
    write__uint_4byte_BE_
    write__chunk_
        mk_may_chunk_data__IEND_
        mk_may_chunk_data__IHDR_
        mk_may_chunk_data__sBIT_
        mk_may_chunk_data__PLTE_
        mk_may_chunk_data__tRNS_
        mk_may_chunk_data__bKGD_
        mk_may_chunk_data_seq__IDAT_
            encode_IDAT_

encode_IDAT_
    mx5ij2v_
    interlaceX_
    scanline_
    xpixels2bytes8row_
    filterX_
    filter0__reduced_image_
    join_bytesss_
    compressX_
    cut_into_chunks_







dump_png_file__pixel_matrix7RGBA4src_
    preprocess__pixel_matrix7RGBA4src_

preprocess__pixel_matrix7RGBA4src_
    alpha_separation_
    alpha_compaction_
    try_indexing_
        mk_may_set__size_le_
        mk_may_counter__size_le_
    sample_depth_scaling_
        mk_lowerbound4sample_depth7uniform5sample_depths7XXX4src_
        mk_scale_sample_depth__std_
    rgb_merging_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
import zlib
from os import SEEK_END
from enum import IntEnum
from functools import cached_property
from itertools import islice, zip_longest, product, chain
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt, check_int_ge_le, check_may_, check_all_, check_pair, check_callable
#from seed.math.perfect_div import perfect_div
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'Counter:mk_Counter_'):
    from collections import Counter as mk_Counter_
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil import ceil_div, ceil_log2#perfect_div, perfect_kth_root_
    from seed.helper.ifNone import ifNone,ifNonef
    from seed.helper.repr_input import repr_helper
    from seed.io.open4with import open4rb_, open4wb_
    from seed.tiny_.containers import mk_tuple#mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str #xxx:null_tuple
    from seed.tiny_.funcs import echo#fst,snd
___end_mark_of_excluded_global_names__0___ = ...


__all__







png_file_signature = b'\x89PNG\r\n\x1a\n'

class BaseError(Exception):pass
class Error__eof(BaseError, EOFError):pass


class Error__IDAT(BaseError):pass
class Error__PLTE__palette7RGB(BaseError):pass
class Error__bKGD(BaseError):pass
class Error__bit_depth(BaseError):pass
class Error__bytes_not_matched(BaseError):pass
class Error__chunk_infos_filled(BaseError):pass
class Error__chunk_infos_not_filled(BaseError):pass
class Error__chunk_length__IHDR(BaseError):pass
class Error__chunk_type(BaseError):pass
class Error__chunk_type__IDAT__decompressobj__eof(BaseError):pass
class Error__chunk_type__IDAT__decompressobj__unconsumed_tail(BaseError):pass
class Error__chunk_type__IDAT__decompressobj__unused_data(BaseError):pass
class Error__chunk_type__tRNS__alpha_used(BaseError):pass
class Error__chunk_type__unknown_critical(BaseError):pass
class Error__crc(BaseError):pass
class Error__key_existed(BaseError):pass
class Error__not_perfect_div(BaseError):pass
class Error__png_uint_31bit_overflow(BaseError):pass
class Error__png_uint_7bit_overflow(BaseError):pass
class Error__range(BaseError):pass
class Error__sBIT(BaseError):pass
class Error__tRNS__palette7A(BaseError):pass
class Error__tRNS__pixel7L8fully_transparent(BaseError):pass
class Error__tRNS__pixel7RGB8fully_transparent(BaseError):pass

class Error__segment(BaseError):pass
class Error__num_bits4segment(BaseError):pass
class Error__sample_depths7XXX4src(BaseError):pass
class Error__alpha_separation(BaseError):pass











def mk_max_sample5depth_(sample_depth, /):
    max_sample = (1<<sample_depth) -1
    return max_sample


def calc_crc32_(bss, /):
    checksum = 0
    for bs in bss:
        checksum = zlib.crc32(bs, checksum)
    checksum &= 0xFF_FF_FF_FF
    return checksum
def validate_crc32_(checksum, bss, /):
    if not checksum == calc_crc32_(bss): raise Error__crc



def fmap_tmay_(x2y, tmay_x, /):
    if tmay_x:
        [x] = tmay_x
        y = x2y(x)
        tmay_y = (y,)
    else:
        tmay_y = tmay_x
    tmay_y
    return tmay_y
def may2tmay_(m, /):
    if m is None:
        return mk_tuple('')
    x = m
    return (x,)
def may5tmay_(tm, /):
    if tm:
        [x] = tm
        assert not None is x
        return x
    return None




def perfect_div(n, d, /):
    (q, r) = divmod(n, d)
    if r:
        raise Error__not_perfect_div
    return q

class ColorType4png(IntEnum):
    r'''
    [color_type == (6/Truecolor_with_alpha|4/Greyscale_with_alpha|3/Indexed_color|2/Truecolor|0/Greyscale)]
    [color_type :: uint%7 \-\{1,5}]
    [color_type == [palette_used]1 + [truecolor_used]2 + [alpha_used]4]
    '''#'''
    Greyscale = 0
    Truecolor = 2
    Indexed_color = 3
    Greyscale_with_alpha = 4
    Truecolor_with_alpha = 6

    @cached_property
    def without_alpha_used(sf, /):
        if not sf.alpha_used:
            return sf
        ot = ColorType4png(sf.value ^ Data4ColorType4png.weight4alpha_used)
        assert ot.value ^ sf.value == Data4ColorType4png.weight4alpha_used
        assert not ot.alpha_used
        return ot
    @cached_property
    def without_truecolor_used(sf, /):
        if not sf.truecolor_used:
            return sf
        ot = ColorType4png(sf.value ^ Data4ColorType4png.weight4truecolor_used)
        assert ot.value ^ sf.value == Data4ColorType4png.weight4truecolor_used
        assert not ot.truecolor_used
        return ot
    @cached_property
    def palette_used(sf, /):
        return bool(sf.value & Data4ColorType4png.weight4palette_used)
    @cached_property
    def truecolor_used(sf, /):
        return bool(sf.value & Data4ColorType4png.weight4truecolor_used)
    @cached_property
    def alpha_used(sf, /):
        return bool(sf.value & Data4ColorType4png.weight4alpha_used)

    @cached_property
    def num_segments4xpixel(sf, /):
        '-> uint{>0} # [segment =[def]= (palette_index|sample)] # [xpixel =[def]= (boxed_palette_index|pixel)] # [xpixel :: [segment]{len<-[1..=4]}] # [pixel :: [sample]{len<-[1..=4]}] # [boxed_palette_index == (palette_index,)]'
        if sf.palette_used:
            return 1
        return (3 if sf.truecolor_used else 1) + sf.alpha_used
    @cached_property
    def num_channels4pixel(sf, /):
        '-> uint{>0}'
        if sf.palette_used:
            return 3
        return sf.num_segments4xpixel
    def bit_depth2num_bits4xpixel(sf, bit_depth, /):
        num_bits4segment = bit_depth
        num_bits4xpixel = num_bits4segment*sf.num_segments4xpixel
        return num_bits4xpixel
class Data4ColorType4png:
    weight4palette_used = 1
    weight4truecolor_used = 2
    weight4alpha_used = 4
    values4color_type = (0,2,3,4,6)
class Nicknames4ColorType4png:
    L = ColorType4png.Greyscale
    RGB = ColorType4png.Truecolor
    P = ColorType4png.Indexed_color
    LA = ColorType4png.Greyscale_with_alpha
    RGBA = ColorType4png.Truecolor_with_alpha
Nicknames4ColorType4png.L.values4bit_depth = (1,2,4,8,16)
Nicknames4ColorType4png.P.values4bit_depth = (1,2,4,8)
Nicknames4ColorType4png.LA.values4bit_depth = (8,16)
Nicknames4ColorType4png.RGBA.values4bit_depth = (8,16)
Nicknames4ColorType4png.RGB.values4bit_depth = (8,16)

assert ColorType4png.Greyscale_with_alpha.value == 4
assert ColorType4png.Greyscale_with_alpha is ColorType4png(4)
assert ColorType4png.Greyscale_with_alpha.alpha_used
assert not ColorType4png.Greyscale.alpha_used
try:
    ColorType4png(1)
except Exception:
    pass
else:
    raise Exception(ColorType4png.__new__)

class IReadablePixelMatrix7RGBA(ABC):
    'IReadablePixelMatrix7RGBA{wh_size4canvas/(width4canvas, height4canvas), sample_depths7RGBA4src/(,,,), color_type4png, may pixel7RGB8fully_transparent/(,,), may pixel7RGB8background_color/(,,), may palette7RGB/[(,,)]{len<=256}, may palette7A/[sample7A]{len<=len(palette7RGB)}}'
    __slots__ = ()
    @abstractmethod
    def get_pixel7RGBA_at_(sf, idx8row, idx8column, /):
        'uint%height4canvas -> uint%width4canvas -> pixel7RGBA/(uint%2**sample_depth4R, uint%2**sample_depth4G, uint%2**sample_depth4B, uint%2**sample_depth4A)'
#class IMutablePixelMatrix7RGBA(ABC):
class IWritablePixelMatrix7RGBA(ABC):
    'IWritablePixelMatrix7RGBA{wh_size4canvas/(width4canvas, height4canvas), sample_depths7RGBA4src/(,,,), color_type4png, may pixel7RGB8fully_transparent/(,,), may pixel7RGB8background_color/(,,), may palette7RGB/[(,,)]{len<=256}, may palette7A/[sample7A]{len<=len(palette7RGB)}}'
    __slots__ = ()
    @abstractmethod
    def set_pixel7RGBA_at_(sf, idx8row, idx8column, pixel7RGBA, /):
        'uint%height4canvas -> uint%width4canvas -> pixel7RGBA/(uint%2**sample_depth4R, uint%2**sample_depth4G, uint%2**sample_depth4B, uint%2**sample_depth4A) -> None'



class MutablePixelMatrix7RGBA(IWritablePixelMatrix7RGBA, IReadablePixelMatrix7RGBA):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *sf._part1_params4repr, sf._mx)
    def __init__(sf, wh_size4canvas, sample_depths7RGBA4src, color_type4png, may_pixel7RGB8fully_transparent, may_pixel7RGB8background_color, may_palette7RGB, may_palette7A, may_mx, /):
        sf._part1_params4repr = (wh_size4canvas, sample_depths7RGBA4src, color_type4png, may_pixel7RGB8fully_transparent, may_pixel7RGB8background_color, may_palette7RGB, may_palette7A)
        #########
        check_type_is(ColorType4png, color_type4png)
        check_type_is(tuple, sample_depths7RGBA4src)
        check_sample_depths7RGBA4src_(sample_depths7RGBA4src)
        (width4canvas, height4canvas) = wh_size4canvas
        if may_mx is None:
            mx = [[None]*width4canvas for _ in range(height4canvas)]
        else:
            mx = may_mx
            mx = list(map(list, mx))
            assert len(mx) == height4canvas
            assert set(map(len, mx)) == {width4canvas}
        mx
        sf._mx = mx
        sf._ct = color_type4png
        sf._tRNS7pixel = may_pixel7RGB8fully_transparent
        sf._tRNS7RGB = may_palette7RGB
        sf._tRNS7A = may_palette7A
            # * [has:tRNS_chunk{palette7A/alpha_table}]@Indexed_color
            # * [has:tRNS_chunk{pixel7RGB8fully_transparent|pixel7L8fully_transparent}]@(Truecolor|Greyscale)
        sf._bKGD = may_pixel7RGB8background_color
        #########
        sf._sBIT = sample_depths7RGBA4src
        #########
        ###after: ._sBIT
        #       !! sf.max_sample7A
        #########
        may_palette7RGBA = mk_may_palette7RGBA_(sf.max_sample7A, may_palette7RGB, may_palette7A)
        assert color_type4png.palette_used is (not None is may_palette7RGBA)
        sf._tRNS7RGBA = may_palette7RGBA
        #########



    @cached_property
    def sample_depth7R(sf, /):
        return sf._sBIT[0]
    @cached_property
    def sample_depth7G(sf, /):
        return sf._sBIT[1]
    @cached_property
    def sample_depth7B(sf, /):
        return sf._sBIT[2]
    @cached_property
    def sample_depth7A(sf, /):
        return sf._sBIT[3]


    @cached_property
    def max_sample7R(sf, /):
        return mk_max_sample5depth_(sf.sample_depth7R)
    @cached_property
    def max_sample7G(sf, /):
        return mk_max_sample5depth_(sf.sample_depth7G)
    @cached_property
    def max_sample7B(sf, /):
        return mk_max_sample5depth_(sf.sample_depth7B)
    @cached_property
    def max_sample7A(sf, /):
        return mk_max_sample5depth_(sf.sample_depth7A)


    @override
    def get_pixel7RGBA_at_(sf, idx8row, idx8column, /):
        return sf._mx[idx8row][idx8column]
    @override
    def set_pixel7RGBA_at_(sf, idx8row, idx8column, pixel7RGBA, /):
        check_type_is(tuple, pixel7RGBA)
        assert len(pixel7RGBA) == 4
        (R, G, B, A) = pixel7RGBA
        check_int_ge_le(0, sf.max_sample7R, R)
        check_int_ge_le(0, sf.max_sample7G, G)
        check_int_ge_le(0, sf.max_sample7B, B)
        check_int_ge_le(0, sf.max_sample7A, A)
        color_type4png = sf._ct
        if color_type4png.palette_used:
            assert pixel7RGBA in sf._tRNS7RGBA

        if not color_type4png.truecolor_used:
            assert R == G == B

        if not color_type4png.alpha_used:
            if not color_type4png.palette_used:
                if not None is sf._tRNS7pixel:
                    assert A == (0 if (R, G, B) == sf._tRNS7pixel else sf.max_sample7A)
                else:
                    assert A == sf.max_sample7A
        sf._mx[idx8row][idx8column] = pixel7RGBA
#end-class MutablePixelMatrix7RGBA(IWritablePixelMatrix7RGBA, IReadablePixelMatrix7RGBA):







def read_ex__seq_(sz, read_ex_, array, begin, end, /):
    check_int_ge(0, sz)
    xs = []
    for _ in range(sz):
        (x, begin) = read_ex_(array, begin, end)
        xs.append(x)
    return (tuple(xs), begin)

def read_ex__uint_7bit_1byte_BE_(array, begin, end, /):
    (u, _begin) = read_ex__uint_8bit_1byte_BE_(array, begin, end)
    if not u < 0x80:raise Error__png_uint_7bit_overflow
    return (u, _begin)
def read_ex__uint_31bit_4byte_BE_(array, begin, end, /):
    (u, _begin) = read_ex__uint_32bit_4byte_BE_(array, begin, end)
    if not u < 0x80_00_00_00:raise Error__png_uint_31bit_overflow
    return (u, _begin)

def read_ex__uint_8bit_1byte_BE_(array, begin, end, /):
    sz = 1
    return read_ex__uint_BE__size_eq_(sz, array, begin, end)
def read_ex__uint_16bit_2byte_BE_(array, begin, end, /):
    sz = 2
    return read_ex__uint_BE__size_eq_(sz, array, begin, end)
def read_ex__uint_32bit_4byte_BE_(array, begin, end, /):
    sz = 4
    return read_ex__uint_BE__size_eq_(sz, array, begin, end)
def read_ex__uint_BE__size_eq_(sz, array, begin, end, /):
    (bs, _begin) = read_ex__bytes__size_eq_(sz, array, begin, end)
    u = decode8uint_BE_(bs)
    return (u, _begin)
def decode8uint_BE_(bs, /):
    u = int.from_bytes(bs, 'big', signed=False)
    return u


def read_ex__bytes__size_le_(sz, array, begin, end, /):
    if not 0 <= begin <= end <= len(array):raise Error__range
    check_int_ge(0, sz)
    _begin = min(end, begin+sz)
    return (array[begin:_begin], _begin)
def read_ex__bytes__size_eq_(sz, array, begin, end, /):
    (bs, _begin) = read_ex__bytes__size_le_(sz, array, begin, end)
    if not len(bs) == sz:raise Error__eof
    return (bs, _begin)


def load_png_file__mx8src_(may_ibfile_or_ipath8png_file, /):
    '-> (sample_depths7RGBA4png, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image)'
    ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)) = load_png_file__both_mx8src_and_mx8png_(may_ibfile_or_ipath8png_file)
    return (sample_depths7RGBA4png, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image)
def load_png_file__mx8png_(may_ibfile_or_ipath8png_file, /):
    '-> (sample_depths7RGBA4src, sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)'
    ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)) = load_png_file__both_mx8src_and_mx8png_(may_ibfile_or_ipath8png_file)
    return (sample_depths7RGBA4src, sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)

def load_png_file__both_mx8src_and_mx8png_(may_ibfile_or_ipath8png_file, /, *, with_image_info_dict=False):
    '-> ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image))'
    with open4rb_(may_ibfile_or_ipath8png_file) as ibfile:
        sf = Reader4png(ibfile, may_position7start:=0)
        result4decode_IDAT = sf.gmk_result4decode_IDAT_()
        image_info_dict = sf.image_info_dict
    if with_image_info_dict:
        return (result4decode_IDAT, image_info_dict)
    return result4decode_IDAT
def load_png_file8pixel_matrix7RGBA4src_(may_ibfile_or_ipath8png_file, /, *, with_image_info_dict=False):
    with open4rb_(may_ibfile_or_ipath8png_file) as ibfile:
        sf = Reader4png(ibfile, may_position7start:=0)
        pixel_matrix7RGBA4src = sf.load8pixel_matrix7RGBA4src_()
        image_info_dict = sf.image_info_dict
    if with_image_info_dict:
        return (pixel_matrix7RGBA4src, image_info_dict)
    return pixel_matrix7RGBA4src

class Reader4png:
    def _mk_blank_pixel_matrix8image7RGBA_(sf, wh_size4canvas, sample_depths7RGBA4src, color_type4png, may_pixel7RGB8fully_transparent, may_pixel7RGB8background_color, may_palette7RGB, may_palette7A, /):
        'wh_size4canvas/(width4canvas/pint, height4canvas/pint) -> sample_depths7RGBA4src/(sample_depth4R/pint, sample_depth4G/pint, sample_depth4B/pint, sample_depth4A/pint) -> ColorType4png -> may pixel7RGB8fully_transparent/(uint%2**sample_depth4R, uint%2**sample_depth4G, uint%2**sample_depth4B) -> may pixel7RGB8background_color -> may palette7RGB/[(,,)]{len<=256} -> may palette7A/[sample7A]{len<=len(palette7RGB)} -> IWritablePixelMatrix7RGBA'
        return MutablePixelMatrix7RGBA(wh_size4canvas, sample_depths7RGBA4src, color_type4png, may_pixel7RGB8fully_transparent, may_pixel7RGB8background_color, may_palette7RGB, may_palette7A, may_mx:=None)
    def __init__(sf, ibfile, may_position7start, /):
        if may_position7start is None:
            position7start = ibfile.tell()
        else:
            position7start = may_position7start
        position7start
        check_int_ge(0, position7start)
        ibfile.seek(0, SEEK_END)
        position7eof = ibfile.tell()
        ibfile.seek(position7start)
        check_int_ge_le(0, position7eof, position7start)

        sf.ibfile = ibfile
        sf.position7start = position7start
        sf.position7eof = position7eof
        sf.chunk_type2indices8chunk = {}
        sf.chunk_infos = []
        sf.chunk_infos_filled = False
        sf.image_info_dict = {}
        #sf.pixel_matrix7RGBA4src_loaded = False
        sf.chunk_infos_handled = False
    def tell__abs_(sf, /):
        position = sf.ibfile.tell()
        return position
    def seek__abs_(sf, position, /):
        check_int_ge_le(0, sf.position7eof, position) ### !!! MUST !!! ### otherwise may move to nowhere
        sf.ibfile.seek(position)
    def seek__rel_(sf, offset, /):
        position = sf.ibfile.tell() +offset
        sf.ibfile.seek(position)
    def seek7start_(sf, /):
        sf.seek__abs_(sf.position7start)
    def read__size_le_(sf, sz, /):
        return sf.ibfile.read(sz)
    def read__size_eq_(sf, sz, /):
        bs = sf.read__size_le_(sz)
        if not len(bs) == sz:raise Error__eof
        return bs
    def match_and_skip_bytes_(sf, bs, /):
        if not bs == sf.read__size_eq_(len(bs)):
            raise Error__bytes_not_matched
    def read__uint_31bit_4byte_BE_(sf, /):
        u = sf.read__uint_32bit_4byte_BE_()
        if not u < 0x80_00_00_00:raise Error__png_uint_31bit_overflow
        return u
    def read__uint_32bit_4byte_BE_(sf, /):
        bs = sf.read__size_eq_(4)
        u = decode8uint_BE_(bs)
        return u
    def read__chunk_type_(sf, /):
        chunk_type = bs = sf.read__size_eq_(4)
        sf.check__chunk_type_(chunk_type)
        return chunk_type
    def check__chunk_type_(sf, chunk_type, /):
        check_chunk_type__png_ver3_(chunk_type)
    def is_known_critical__chunk_type_(sf, chunk_type, /):
        return chunk_type in b'IHDR PLTE IDAT IEND'
    def read_chunk_info_(sf, /):
        len4data = sf.read__uint_31bit_4byte_BE_()
        chunk_type = sf.read__chunk_type_()
        position4data = sf.tell__abs_()
        sf.seek__rel_(len4data)
        crc4typ_dat = sf.read__uint_32bit_4byte_BE_()
        chunk_info = (chunk_type, position4data, len4data, crc4typ_dat)
        return chunk_info

    def fill_chunk_infos_(sf, /):
        if sf.chunk_infos_filled:
            return
        d = sf.chunk_type2indices8chunk
        ls = sf.chunk_infos
        if ls:raise Error__chunk_infos_filled
        sf.seek7start_()
        sf.match_and_skip_bytes_(png_file_signature)
        while 1:
            chunk_info = sf.read_chunk_info_()
            (chunk_type, position4data, len4data, crc4typ_dat) = chunk_info
            if not ls and not chunk_type == b'IHDR':raise Error__chunk_type
            idc = d.setdefault(chunk_type, [])
            ichunk = len(ls)
            idc.append(ichunk)
            ls.append(chunk_info)
            sf.on_appended_chunk_info_(ichunk, chunk_info)
            if chunk_type == b'IEND':break

        #sf.handle_chunk_info__IHDR_(0, ls[0])
        sf.handle_chunk_info_(0, ls[0])
            # color_type required by .validate_chunk_order_()
        sf.validate_chunk_order_()
        sf.chunk_infos_filled = True
    def validate_chunk_order_(sf, /):
        '[IHDR < { tIME? , iTXt* , tEXt* , zTXt* , { eXIf? , pHYs? , sPLT* , {(iCCP|cICP|sRGB)?,cHRM?,gAMA?,mDCV?,cLLI?,sBIT?} < PLTE? < {[PLTE]hIST?,bKGD?,tRNS?} , acTL? < [acTL]fcTL? } < IDAT+ < [acTL](fcTL < fdAT+)+ } < IEND]'
        if sf.chunk_infos_filled:
            return
        color_type4png = sf.image_info_dict['color_type']
        d = sf.chunk_type2indices8chunk
        ls = sf.chunk_infos
        if not ls:raise Error__chunk_infos_not_filled
        def g_(chunk_type, /):
            return d.get(chunk_type, [])
        def has_(chunk_type, /):
            return bool(g_(chunk_type))
        def filter__chunk_types_(chunk_types, /):
            if type(chunk_types) is bytes:
                chunk_types = chunk_types.split()
            chunk_types = tuple(filter(has_, chunk_types))
            return chunk_types
        def check_before(chunk_type7before, chunk_type7after, /):
            idcL = g_(chunk_type7before)
            idcR = g_(chunk_type7after)
            if idcL and idcR and not idcL[-1] < idcR[0]:raise AssertionError(chunk_type7before, chunk_type7after, idcL, idcR)
        def check_beforess(chunk_types7before, chunk_types7after, /):
            chunk_types7before = filter__chunk_types_(chunk_types7before)
            chunk_types7after = filter__chunk_types_(chunk_types7after)
            for (chunk_type7before, chunk_type7after) in product(chunk_types7before, chunk_types7after):
                check_before(chunk_type7before, chunk_type7after)

        #########
        ichunk4IEND = len(ls) -1
        assert (idc:=g_(chunk_type:=b'IHDR')) == [0], (chunk_type, idc)
        assert (idc:=g_(chunk_type:=b'IEND')) == [ichunk4IEND], (chunk_type, idc)
        assert (idc:=g_(chunk_type:=b'IDAT')) and idc[0]+len(idc) == idc[-1]+1, (chunk_type, idc)
        assert not color_type4png.palette_used or len(idc:=g_(chunk_type:=b'PLTE')) == 1, (chunk_type, idc)

        #########
        chunk_types7optional = b'tIME eXIf pHYs iCCP cICP sRGB cHRM gAMA mDCV cLLI sBIT PLTE hIST bKGD tRNS acTL'.split()
        for chunk_type in chunk_types7optional:
            assert len(idc:=g_(chunk_type)) < 2, (chunk_type, idc)

        #########
        chunk_types7exclusive = b'iCCP cICP sRGB'.split()
        assert (sz:=sum(len(g_(chunk_type)) for chunk_type in chunk_types7exclusive)) < 2, (chunk_types7exclusive, sz)

        #########
        assert not has_(b'hIST') or has_(b'PLTE')
        assert has_(b'fcTL') is has_(b'acTL')
        assert has_(b'fdAT') is has_(b'acTL')
        assert not (color_type4png.alpha_used and has_(b'tRNS'))

        #########
        check_beforess(b'eXIf pHYs sPLT iCCP cICP sRGB cHRM gAMA mDCV cLLI sBIT PLTE hIST bKGD tRNS acTL', b'IDAT')
        check_beforess(b'IDAT', b'fdAT')
        assert (idc4IDAT:=g_(b'IDAT')) and (len(idc4fcTL:=g_(b'fcTL')) < 2 or idc4IDAT[-1] < idc4fcTL[1]), (idc4IDAT, idc4fcTL)

        #########
        check_beforess(b'iCCP cICP sRGB cHRM gAMA mDCV cLLI sBIT', b'PLTE')
        check_beforess(b'PLTE', b'hIST bKGD tRNS')

        #########
        return
    #end-def validate_chunk_order_(sf, /):
    def on_appended_chunk_info_(sf, ichunk, chunk_info, /):
        chunk_type = chunk_info[0]
        if not is_ancillary__chunk_type_(chunk_type):
            # critical
            if not sf.is_known_critical__chunk_type_(chunk_type):raise Error__chunk_type__unknown_critical(chunk_type)
        tag = chunk_type.decode('ascii')
        nm = f'on_appended_chunk_info__{tag}_'
        m = getattr(sf, nm, None)
        if not m is None:
            f = m
            f(ichunk, chunk_info)

    def on_appended_chunk_info__IHDR_(sf, ichunk, chunk_info, /):
        pass

    def read__chunk_typ_dat5ichunk_(sf, ichunk, /, *, to_validate_crc:bool):
        chunk_info = sf.chunk_infos[ichunk]
        chunk_typ_dat = sf.read__chunk_typ_dat5chunk_info_(chunk_info, to_validate_crc=to_validate_crc)
        return chunk_typ_dat
    def read__chunk_typ_dat5chunk_info_(sf, chunk_info, /, *, to_validate_crc:bool):
        (chunk_type, position4data, len4data, crc4typ_dat) = chunk_info
        sf.seek__abs_(position4data)
        chunk_data = sf.read__size_eq_(len4data)
        if to_validate_crc:
            validate_crc32_(crc4typ_dat, [chunk_type, chunk_data])
        chunk_typ_dat = (chunk_type, chunk_data)
        return chunk_typ_dat

    def handle_chunk_infos_(sf, /):
        'to fill image_info_dict'
        if sf.chunk_infos_handled:
            return
        for ichunk, chunk_info in enumerate(sf.chunk_infos):
            sf.handle_chunk_info_(ichunk, chunk_info)
            sf.on_handled_chunk_info_(ichunk, chunk_info)
        sf.chunk_infos_handled = True
    def handle_chunk_info_(sf, ichunk, chunk_info, /):
        chunk_type = chunk_info[0]
        tag = chunk_type.decode('ascii')
        nm = f'handle_chunk_info__{tag}_'
        m = getattr(sf, nm, None)
        if not m is None:
            f = m
            chunk_typ_dat = sf.read__chunk_typ_dat5ichunk_(ichunk, to_validate_crc=True)
            (_chunk_type, chunk_data) = chunk_typ_dat
            f(ichunk, chunk_type, chunk_data)

    def on_handled_chunk_info_(sf, ichunk, chunk_info, /):
        pass
    def handle_chunk_info__IHDR_(sf, ichunk, chunk_type, chunk_data, /):
        r'''[[[
        [chunk_data4IHDR == (width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method)]

        [width4canvas,height4canvas :: pint_31bit___big_endian_4byte]
        [bit_depth, color_type, compression_method, filter_method, interlace_method :: uint_8bit_1byte{public_value@uint_7bit_1byte}{private_value@{>=128}}]
          [compression_method <- {0}]
              # (deflate compression with a sliding window of at most 32768 bytes)
          [filter_method <- {0}]
              # (adaptive filtering with five basic filter types)
          [interlace_method <- {0,1}]
              # (no_interlace|Adam7_interlace)
          [color_type <- {0,2,3,4,6}]
          [bit_depth <- {1,2,4,8,16}{depends on color_type}]
              #Bit depth restrictions for each color type are imposed to simplify implementations and to prohibit combinations that do not compress well.
        Greyscale:
          L1,L2,L4,L8,L16
          [pixel{L} == (L/luminance,)]
          no:PLTE_chunk

        Truecolor:
          RGB8,RGB16
          [pixel{RGB} == (R,G,B)]
          PLTE_chunk?

        Indexed_color:
          P1,P2,P4,P8
          [pixel{L} == (P/palette_index,)]
          [sample_depth7uniform{P} === 8]
          PLTE_chunk!


        Greyscale_with_alpha:
          LA8,LA16
          [pixel{LA} == (L,A)]
          no:PLTE_chunk

        Truecolor_with_alpha:
          RGBA8,RGBA16
          [pixel{RGBA} == (R,G,B,A)]
          PLTE_chunk?


        [sample_depth7uniform{color_type} === 8 if color_type==P else bit_depth{color_type}]


        #]]]'''#'''
        #######
        d = sf.image_info_dict
        if 'color_type' in d:
            # color_type required by .validate_chunk_order_()
            return
        #######
        len4data = len(chunk_data)
        if not len4data == 13:
            # 13==4+4+5
            raise Error__chunk_length__IHDR(len4data)
        i, j = 0, len(chunk_data)
        (wh_size4canvas, i) = read_ex__seq_(2, read_ex__uint_31bit_4byte_BE_, chunk_data, i, j)
        (width4canvas, height4canvas) = wh_size4canvas
        (_5byte, i) = read_ex__seq_(5, read_ex__uint_7bit_1byte_BE_, chunk_data, i, j)
        if not i == len(chunk_data):raise 000
        check_wh_size4canvas(wh_size4canvas)
        (bit_depth, color_type, compression_method, filter_method, interlace_method) = _5byte
        check_five_byte_uints6IHDR_(bit_depth, color_type, compression_method, filter_method, interlace_method)
        color_type4png = ColorType4png(color_type)

        sample_depth7uniform = mk_sample_depth7uniform5bit_depth_(bit_depth, color_type4png)

        #######
        d['width4canvas'] = width4canvas
        d['height4canvas'] = height4canvas
        d['bit_depth'] = bit_depth
        d['color_type'] = color_type4png
        d['compression_method'] = compression_method
        d['filter_method'] = filter_method
        d['interlace_method'] = interlace_method
        #######
        d['wh_size4canvas'] = wh_size4canvas
        d['sample_depth7uniform'] = sample_depth7uniform
        #######
        return
        chunk_data4IHDR = (width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method)
        return chunk_data4IHDR
        return (*wh_size4canvas, *_5byte)
    def handle_chunk_info__PLTE_(sf, ichunk, chunk_type, chunk_data, /):
        r'''[[[
        [chunk_data4PLTE == palette_entries :: [palette_entry/pixel7RGB_3byte]{1<=len<=256}]
            #不论原图sample_depths7XXX4src是多少,[palette_entry.sample_depth==8]
            #   考虑到lossless:要么[max(sample_depths7XXX4src) <= 8]要么我猜[所有颜色均可依照my_extended_sample_depth_scaling脱水]
            # palette_entry不一定都被用到
            # 允许palette_entry重复出现
        [len(palette_entries) == len(chunk_data4PLTE)///3]


        #]]]'''#'''
        num_palette_entries7RGB = perfect_div(len(chunk_data), 3)
        palette7RGB = []
        for j3 in range(0, 3*num_palette_entries7RGB, 3):
            palette_entry = pixel7RGB = _3byte = chunk_data[j3:j3+3]
            palette7RGB.append(palette_entry)
        palette7RGB = tuple(palette7RGB)
        if not 1 <= len(palette7RGB) <= 256:raise Error__PLTE__palette7RGB
        d = sf.image_info_dict
        d['palette7RGB'] = palette7RGB
        return
    def handle_chunk_info__IDAT_(sf, ichunk, chunk_type, chunk_data, /):
        d = sf.image_info_dict
        chunk_data_seq4IDAT = d.setdefault('chunk_data_seq4IDAT', [])
        chunk_data_seq4IDAT.append(chunk_data)
        return
    def handle_chunk_info__IEND_(sf, ichunk, chunk_type, chunk_data, /):
        len4data = len(chunk_data)
        if not len4data == 0:
            raise Error__chunk_length__IHDR(len4data)
        return
    def handle_chunk_info__tRNS_(sf, ichunk, chunk_type, chunk_data, /):
        r'''[[[
        含tRNS两种情况:
          * [has:tRNS_chunk{palette7A/alpha_table}]@Indexed_color
          * [has:tRNS_chunk{pixel7RGB8fully_transparent|pixel7L8fully_transparent}]@(Truecolor|Greyscale)

        Greyscale/0:
          [chunk_data4tRNS{L} == pixel7L8fully_transparent/grey_sample_value :: uint_2byte_BE]

        Truecolor/2:
          [chunk_data4tRNS{RGB} == pixel7RGB8fully_transparent/(red_sample_value,green_sample_value,blue_sample_value) :: (uint_2byte_BE,uint_2byte_BE,uint_2byte_BE)]
          #(0|2):
            If the image bit depth is less than 16, the least significant bits are used.
              # 『image bit depth』应该是指png.sample_depth7uniform，而非 原图sample_depths7XXX4src，这里的pixel保存的是sample_depth_scaling后的值，因为已经放大过，所以只是低端保存而无需再放大，16bit只是容器
              #Decoders have to postpone any sample depth rescaling until after the pixels have been tested for transparency.

        Indexed_color/3:
          [chunk_data4tRNS{P} == palette7A/alpha_table :: [uint_1byte]*len(palette7A)]
            #3:
            [1 <= len(palette7A) <= len(palette7RGB) <= 256]
              # palette7A 尾部填充 (max_alpha)
              填充


        #]]]'''#'''
        d = sf.image_info_dict
        match d['color_type']:
            case ColorType4png.Indexed_color:
                palette7RGB = d['palette7RGB']#@PLTE
                palette7A = alpha_table = chunk_data
                if not len(palette7A) <= len(palette7RGB):raise Error__tRNS__palette7A
                #palette7A = tuple(palette7A)
                d['palette7A'] = palette7A
            case ColorType4png.Greyscale:
                if not len(chunk_data) == 2:raise Error__tRNS__pixel7L8fully_transparent
                (u, _begin) = read_ex__uint_16bit_2byte_BE_(chunk_data, 0, len(chunk_data))
                assert _begin == len(chunk_data)
                pixel7L8fully_transparent = (u,)
                d['pixel7L8fully_transparent'] = pixel7L8fully_transparent
                pixel7RGB8fully_transparent = pixel7L8fully_transparent*3
                assert len(pixel7RGB8fully_transparent) == 3
                d['pixel7RGB8fully_transparent'] = pixel7RGB8fully_transparent
            case ColorType4png.Truecolor:
                if not len(chunk_data) == 6:raise Error__tRNS__pixel7RGB8fully_transparent
                (pixel7RGB8fully_transparent, _begin) = read_ex__seq_(3, read_ex__uint_16bit_2byte_BE_, chunk_data, 0, len(chunk_data))
                assert _begin == len(chunk_data)
                assert len(pixel7RGB8fully_transparent) == 3
                d['pixel7RGB8fully_transparent'] = pixel7RGB8fully_transparent

            case color_type4png:
                assert color_type4png.alpha_used
                raise Error__chunk_type__tRNS__alpha_used(color_type4png)
        return
    def handle_chunk_info__sBIT_(sf, ichunk, chunk_type, chunk_data, /):
        r'''[[[
        即:原图:sample_depths7XXX4src{color_type}
        [significant_bits{X} :: uint_1byte]
            #有效位数
        [1 <= significant_bits{X} <= sample_depth7uniform]
            # Each depth specified in sBIT shall be greater than zero and less than or equal to the sample depth (which is 8 for indexed-color images, and the bit depth given in IHDR for other color types).

        [chunk_data4sBIT{L} == significant_bits{L}]
          #significant_greyscale_bits
        [chunk_data4sBIT{(RGB|P)} == (significant_bits{R},significant_bits{G},significant_bits{B})]
        [chunk_data4sBIT{LA} == (significant_bits{L},significant_bits{A})]
        [chunk_data4sBIT{RGBA} == (significant_bits{R},significant_bits{G},significant_bits{B},significant_bits{A})]

        tRNS=>(L|RGB|P) 而sBIT@(L|RGB|P)皆无:significant_bits{A}
        #Note that sBIT does not provide a sample depth for the alpha channel that is implied by a tRNS chunk; in that case, all of the sample bits of the alpha channel are to be treated as significant.
        #   If the sBIT chunk is not present, then all of the sample bits of all channels are to be treated as significant.


        #]]]'''#'''
        d = sf.image_info_dict
        color_type4png = d['color_type']
        if not len(chunk_data) == color_type4png.num_channels4pixel:raise Error__sBIT
        sample_depths7XXX4src = significant_bits = chunk_data
        sample_depth7uniform = d['sample_depth7uniform']
        if not max(sample_depths7XXX4src) <= sample_depth7uniform:raise Error__sBIT #xxx:bit_depth
        if not min(sample_depths7XXX4src) >= 1:raise Error__sBIT
        d['sample_depths7XXX4src'] = sample_depths7XXX4src
        return

    def gmk_sample_depths7RGBA4png_(sf, /):
        if not sf.chunk_infos_handled: sf.handle_chunk_infos_()
        d = sf.image_info_dict
        m = d.get('sample_depths7RGBA4png')
        if m:
            #handle_chunk_info__sBIT_
            return m
        sample_depth7uniform = d['sample_depth7uniform']
        sample_depths7RGBA4png = mk_sample_depths7RGBA4png_(sample_depth7uniform)
        d['sample_depths7RGBA4png'] = sample_depths7RGBA4png
        return sf.gmk_sample_depths7RGBA4png_()
    def gmk_sample_depths7RGBA4src_(sf, /):
        if not sf.chunk_infos_handled: sf.handle_chunk_infos_()
        d = sf.image_info_dict
        m = d.get('sample_depths7RGBA4src')
        if m:
            #handle_chunk_info__sBIT_
            return m
        bit_depth = d['bit_depth']
        color_type4png = d['color_type']
        num_bits4sample7png = d['sample_depth7uniform']
        may_sample_depths7XXX4src = d.get('sample_depths7XXX4src')
        sample_depths7RGBA4src = mk_sample_depths7RGBA4src_(bit_depth, color_type4png, num_bits4sample7png, may_sample_depths7XXX4src)
        sf.set_sample_depths7RGBA4src_(sample_depths7RGBA4src)
        return sf.gmk_sample_depths7RGBA4src_()
    def set_sample_depths7RGBA4src_(sf, sample_depths7RGBA4src, /):
        assert len(sample_depths7RGBA4src) == 4
        assert max(sample_depths7RGBA4src) <= 16
        assert min(sample_depths7RGBA4src) >= 1
        #xxx:sample_depths7RGBA4src = bytes(sample_depths7RGBA4src)
        sample_depths7RGBA4src = tuple(sample_depths7RGBA4src)
        d = sf.image_info_dict
        if 'sample_depths7RGBA4src' in d: raise Error__key_existed
        d['sample_depths7RGBA4src'] = sample_depths7RGBA4src
        return
    def get_num_bits4sample7png_(sf, /):
        #sample_depth7uniform==num_bits4sample7png
        d = sf.image_info_dict
        num_bits4sample7png = d['sample_depth7uniform']
        return num_bits4sample7png


    def handle_chunk_info__bKGD_(sf, ichunk, chunk_type, chunk_data, /):
        r'''[[[
        [chunk_data4bKGD{P} == palette_index :: uint_1byte]
        [chunk_data4bKGD{(L|LA)} == pixel7L/grey_sample_value :: uint_2byte_BE]
        [chunk_data4bKGD{(RGB|RGBA)} == pixel7RGB/(red_sample_value,green_sample_value,blue_sample_value) :: (uint_2byte_BE,uint_2byte_BE,uint_2byte_BE)]
            #see:chunk_data4tRNS
            #不必再放大，因为值本身已放大，这里只是提供一个足够大的存储空间
            #If the image bit depth is less than 16, the least significant bits are used.



        #]]]'''#'''
        d = sf.image_info_dict
        color_type4png = d['color_type']
        N = Nicknames4ColorType4png
        match color_type4png:
            case N.P:
                if not len(chunk_data) == 1:raise Error__bKGD
                [palette_index8bg] = chunk_data
                d['palette_index8bg'] = palette_index8bg
                pixel7RGB8bg = d['palette7RGB'][palette_index8bg]
            case N.L | N.LA:
                if not len(chunk_data) == 2:raise Error__bKGD
                (u, _begin) = read_ex__uint_16bit_2byte_BE_(chunk_data, 0, len(chunk_data))
                assert _begin == len(chunk_data)
                pixel7L8bg = (u,)
                d['pixel7L8bg'] = pixel7L8bg
                pixel7RGB8bg = pixel7L8bg*3
            case N.RGB | N.RGBA:
                if not len(chunk_data) == 6:raise Error__bKGD
                (pixel7RGB8bg, _begin) = read_ex__seq_(3, read_ex__uint_16bit_2byte_BE_, chunk_data, 0, len(chunk_data))
                assert _begin == len(chunk_data)
            case _:
                raise 000
        pixel7RGB8bg
        assert len(pixel7RGB8bg) == 3
        d['pixel7RGB8background_color'] = pixel7RGB8bg
        return
    #.def handle_chunk_info__pHYs_(sf, ichunk, chunk_type, chunk_data, /):
    #.    pass
    #.def handle_chunk_info__gAMA_(sf, ichunk, chunk_type, chunk_data, /):
    #.    pass


    def gmk_result4decode_IDAT_(sf, /):
        d = sf.image_info_dict
        if not None is (result4decode_IDAT:=d.get('result4decode_IDAT')):
            return result4decode_IDAT
        sf.fill_chunk_infos_()
        sf.handle_chunk_infos_()
        #########
        # get params of decode_IDAT_
        #########
        wh_size4canvas = d['wh_size4canvas']
        color_type4png = d['color_type']
        may_pixel7RGB8fully_transparent = d.get('pixel7RGB8fully_transparent')
        may_pixel7RGB8background_color = d.get('pixel7RGB8background_color')
        may_palette7RGB = d.get('palette7RGB')
        may_palette7A = d.get('palette7A')

        #########
        #decode_IDAT_
        #########
        #sample_depths7RGBA4png = sf.gmk_sample_depths7RGBA4png_()
        bit_depth = d['bit_depth']
        may_sample_depths7XXX4src = d.get('sample_depths7XXX4src')

        compression_method = d['compression_method']
        filter_method = d['filter_method']
        interlace_method  = d['interlace_method']
        chunk_data_seq4IDAT = d['chunk_data_seq4IDAT']
        may_pixel7L8fully_transparent = d.get('pixel7L8fully_transparent')

        check_int_ge_lt(0, 1, compression_method)
        check_int_ge_lt(0, 1, filter_method)
        check_int_ge_lt(0, 2, interlace_method)
        result4decode_IDAT = decode_IDAT_(may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    bit_depth, color_type4png, wh_size4canvas, filter_method, interlace_method, compression_method, chunk_data_seq4IDAT)
        ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)) = result4decode_IDAT

        d['result4decode_IDAT'] = result4decode_IDAT
        return sf.gmk_result4decode_IDAT_()

    def load8pixel_matrix7RGBA4src_(sf, /):
        d = sf.image_info_dict
        if not None is (pixel_matrix7RGBA4src:=d.get('pixel_matrix7RGBA4src')):
            #if sf.pixel_matrix7RGBA4src_loaded:
            return pixel_matrix7RGBA4src
        result4decode_IDAT = sf.gmk_result4decode_IDAT_()
        ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)) = result4decode_IDAT
        #########
        #mk blank pixel_matrix7RGBA4src
        #########
        pixel_matrix7RGBA4src = sf.mk_blank_pixel_matrix8image7RGBA_()

        #########
        # fill pixel_matrix7RGBA4src
        #########
        wh_size4canvas = d['wh_size4canvas']
        (width4canvas, height4canvas) = wh_size4canvas
        for idx8row, idx8column in product(range(height4canvas), range(width4canvas)):
            pixel7RGBA4src = jrow2pixels7RGBA7src_image[idx8row][idx8column]
            pixel_matrix7RGBA4src.set_pixel7RGBA_at_(idx8row, idx8column, pixel7RGBA4src)
        #########
        d['pixel_matrix7RGBA4src'] = pixel_matrix7RGBA4src
        #sf.pixel_matrix7RGBA4src_loaded = True
        return sf.load8pixel_matrix7RGBA4src_()
    def mk_blank_pixel_matrix8image7RGBA_(sf, /):
        '-> IWritablePixelMatrix7RGBA'
        d = sf.image_info_dict
        #########
        # get params of pixel_matrix7RGBA4src
        #########
        sample_depths7RGBA4src = sf.gmk_sample_depths7RGBA4src_()
        wh_size4canvas = d['wh_size4canvas']
        color_type4png = d['color_type']
        may_pixel7RGB8fully_transparent = d.get('pixel7RGB8fully_transparent')
        may_pixel7RGB8background_color = d.get('pixel7RGB8background_color')
        may_palette7RGB = d.get('palette7RGB')
        may_palette7A = d.get('palette7A')

        #########
        #mk blank pixel_matrix7RGBA4src
        #########
        pixel_matrix7RGBA4src = sf._mk_blank_pixel_matrix8image7RGBA_(wh_size4canvas, sample_depths7RGBA4src, color_type4png, may_pixel7RGB8fully_transparent, may_pixel7RGB8background_color, may_palette7RGB, may_palette7A)
        return pixel_matrix7RGBA4src
#fill_chunk_infos_
#    on_appended_chunk_info__IHDR_
#read__chunk_typ_dat5ichunk_
#handle_chunk_infos_
#    on_handled_chunk_info_
#    handle_chunk_info__IHDR_

def decode_IDAT_(may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    bit_depth, color_type4png, wh_size4canvas, filter_method, interlace_method, compression_method, chunk_data_seq4IDAT, /):
    r'''[[[
    compressed_bytes4scanlines4interlaced_png_image
    :decompressX_:
    filtered_bytes4scanlines4interlaced_png_image
    :split_into_scanlines_:
    jpass2jrow2filtered_bytes7reduced_image
    :inv_filterX_:
    jpass2jrow2bytes7reduced_image
    :reconstruct_xpixels_:
    jpass2jrow2xpixels7reduced_image
    :reconstruct_spng_image7xpixel_:
    jrow2xpixels7spng_image
    :reconstruct_spng_image7pixel7RGBA_:
    jrow2pixels7RGBA7spng_image
        sample_depths7RGBA4png
    :reconstruct_src_image7pixel7RGBA_:
    jrow2pixels7RGBA7src_image
        sample_depths7RGBA4src
        ===pixel_matrix7RGBA4src
    #]]]'''#'''

    sample_depth7uniform = mk_sample_depth7uniform5bit_depth_(bit_depth, color_type4png)
    num_bits4sample7png = sample_depth7uniform
    sample_depths7RGBA4png = mk_sample_depths7RGBA4png_(sample_depth7uniform)
    sample_depths7RGBA4src = mk_sample_depths7RGBA4src_(bit_depth, color_type4png, num_bits4sample7png, may_sample_depths7XXX4src)

    filtered_bytes4scanlines4interlaced_png_image = decompressX_(compression_method, chunk_data_seq4IDAT)
    (num_bits4xpixel, num_bytes4filter_gap, num_segments4xpixel, num_bits4segment) = prepare4parse_IDAT__1_(bit_depth, color_type4png)
    (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling) = prepare4parse_IDAT__2_(interlace_method, wh_size4canvas)
    (jpass2jrow2filtered_bytes7reduced_image, jpass2wh_size4reduced_image) = split_into_scanlines_(interlace_method, num_bits4xpixel, jpass2wh_size4reduced_image, filtered_bytes4scanlines4interlaced_png_image)
    jpass2jrow2bytes7reduced_image = inv_filterX_(filter_method, num_bytes4filter_gap, jpass2jrow2filtered_bytes7reduced_image)
    jpass2jrow2xpixels7reduced_image = reconstruct_xpixels_(num_bits4segment, num_segments4xpixel, jpass2wh_size4reduced_image, jpass2jrow2bytes7reduced_image)
    jrow2xpixels7spng_image = reconstruct_spng_image7xpixel_(interlace_method, wh_size4canvas, jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling, jpass2jrow2xpixels7reduced_image)
    jrow2pixels7RGBA7spng_image = reconstruct_spng_image7pixel7RGBA_(color_type4png, sample_depths7RGBA4png, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent, jrow2xpixels7spng_image)
    jrow2pixels7RGBA7src_image = reconstruct_src_image7pixel7RGBA_(sample_depths7RGBA4png, sample_depths7RGBA4src, jrow2pixels7RGBA7spng_image)
    return ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image))
def decompressX_(compression_method, chunk_data_seq4IDAT, /):
    if not compression_method == 0:raise NotImplementedError(f'compression_method={compression_method}')
    #.compressed_bytes4scanlines4interlaced_png_image = b''.join(chunk_data_seq4IDAT)
    dobj = zlib.decompressobj()
    bss8out = []
    sz = 0
    for sz, bs8delta in enumerate(chunk_data_seq4IDAT, 1):
        bss8out.append(dobj.decompress(bs8delta))
        if dobj.eof:
            if not sz == len(chunk_data_seq4IDAT):raise Error__chunk_type__IDAT__decompressobj__eof
            break
    bss8out.append(dobj.flush())
    if dobj.unused_data:raise Error__chunk_type__IDAT__decompressobj__unused_data
    if dobj.unconsumed_tail:raise Error__chunk_type__IDAT__decompressobj__unconsumed_tail
    #########
    filtered_bytes4scanlines4interlaced_png_image = b''.join(bss8out)
    return filtered_bytes4scanlines4interlaced_png_image

def prepare4parse_IDAT__1_(bit_depth, color_type4png, /):
    #########
    num_bits4xpixel = color_type4png.bit_depth2num_bits4xpixel(bit_depth)
    #.num_bytes4filter_gap = max(1, num_bits4xpixel//8)
    num_bytes4filter_gap = perfect_div(num_bits4xpixel, 8) if num_bits4xpixel > 8 else 1
    num_segments4xpixel = color_type4png.num_segments4xpixel
    num_bits4segment = bit_depth
    return (num_bits4xpixel, num_bytes4filter_gap, num_segments4xpixel, num_bits4segment)
def prepare4parse_IDAT__2_(interlace_method, wh_size4canvas, /):
    if not 0 <= interlace_method <= 1:raise NotImplementedError(f'interlace_method={interlace_method}')
    #########
    match interlace_method:
        case 0:
            prepare_ = prepare4no_interlace_
        case 1:
            prepare_ = prepare4Adam7_interlace_
        case _:
            raise 000
    prepare_
    (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling) = prepare_(wh_size4canvas)
    return (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling)
def prepare4parse_IDAT__3_(color_type4png, sample_depths7RGBA4png, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent, /):
    sample_depths7RGBA4png
        #xxx:sample_depths7RGBA4src
    sample_depth7A4png = sample_depths7RGBA4png[3]
    max_sample7A4png = mk_max_sample5depth_(sample_depth7A4png)

    N = Nicknames4ColorType4png
    match color_type4png:
        case N.P:
            may_palette7RGB, may_palette7A
            if None is may_palette7RGB:raise 000
            may_palette7RGBA = mk_may_palette7RGBA_(max_sample7A4png, may_palette7RGB, may_palette7A)
            if None is may_palette7RGBA:raise 000
            palette7RGBA = may_palette7RGBA
            def xpixel2pixel7RGBA4png_(xpixel, /):
                boxed_palette_index = xpixel
                [palette_index] = boxed_palette_index
                return palette7RGBA[palette_index]
        case N.L:
            may_pixel7L8fully_transparent
            #xxx:if None is may_pixel7L8fully_transparent:raise 000
            def xpixel2pixel7RGBA4png_(xpixel, /):
                pixel7L = xpixel
                [L] = pixel7L
                pixel7RGB = pixel7L*3
                A = 0 if pixel7L == may_pixel7L8fully_transparent else max_sample7A4png
                pixel7RGBA = (*pixel7RGB, A)
                return pixel7RGBA
        case N.RGB:
            may_pixel7RGB8fully_transparent
            #xxx:if None is may_pixel7RGB8fully_transparent:raise 000
            def xpixel2pixel7RGBA4png_(xpixel, /):
                pixel7RGB = xpixel
                assert len(pixel7RGB) == 3
                A = 0 if pixel7RGB == may_pixel7RGB8fully_transparent else max_sample7A4png
                pixel7RGBA = (*pixel7RGB, A)
                return pixel7RGBA
        case N.LA:
            def xpixel2pixel7RGBA4png_(xpixel, /):
                pixel7LA = xpixel
                (L,A) = pixel7LA
                pixel7RGBA = (L,L,L,A)
                return pixel7RGBA
        case N.RGBA:
            def xpixel2pixel7RGBA4png_(xpixel, /):
                pixel7RGBA = xpixel
                assert len(pixel7RGBA) == 4
                return pixel7RGBA
        case _:
            raise 000
    xpixel2pixel7RGBA4png_
    return xpixel2pixel7RGBA4png_


def split_into_scanlines_(interlace_method, num_bits4xpixel, jpass2wh_size4reduced_image, filtered_bytes4scanlines4interlaced_png_image, /):
    if not 0 <= interlace_method <= 1:raise NotImplementedError(f'interlace_method={interlace_method}')
    #########
    jpass2rng4bytes4reduced_image = []
    j = 0
    for (width4reduced_image, height4reduced_image) in jpass2wh_size4reduced_image:
        num_bytes4raw_row4reduced_image = ceil_div(width4reduced_image * num_bits4xpixel, 8)
        num_bytes4filtered_row4reduced_image = num_bytes4raw_row4reduced_image + bool(num_bytes4raw_row4reduced_image)
            # !! ++filter_type_byte
        # (height4reduced_image, num_bytes4filtered_row4reduced_image)
        num_bytes4reduced_image = (height4reduced_image * num_bytes4filtered_row4reduced_image)
        # (height4reduced_image, num_bytes4reduced_image)
        k = j + num_bytes4reduced_image
        rng4bytes4reduced_image = (j, k)
        # (height4reduced_image, rng4bytes4reduced_image)
        jpass2rng4bytes4reduced_image.append(rng4bytes4reduced_image)
        777; j = k
    jpass2rng4bytes4reduced_image
    total_bytes = j
    if not len(filtered_bytes4scanlines4interlaced_png_image) == total_bytes:raise Error__IDAT


    #########
    jpass2filtered_bytes8reduced_image = tuple(iter_split__rngs_(jpass2rng4bytes4reduced_image, filtered_bytes4scanlines4interlaced_png_image))

    #########
    jpass2jrow2filtered_bytes7reduced_image = []
    for ft_bs8reduced_image, (width4reduced_image, height4reduced_image) in zip(jpass2filtered_bytes8reduced_image, jpass2wh_size4reduced_image):
        ft_bss8reduced_image = tuple(iter_split__num_rows_(height4reduced_image, ft_bs8reduced_image))
        jpass2jrow2filtered_bytes7reduced_image.append(ft_bss8reduced_image)
    jpass2jrow2filtered_bytes7reduced_image = tuple(jpass2jrow2filtered_bytes7reduced_image)
    return (jpass2jrow2filtered_bytes7reduced_image, jpass2wh_size4reduced_image)

def iter_split__rngs_(rngs, seq, /):
    for j, k in rngs:
        yield seq[j:k]
def iter_split__num_rows_(num_rows, seq, /):
    if not seq:
        # [num_rows == 0]or[num_columns==0]
        return
    num_columns = perfect_div(len(seq), num_rows)
    for i in range(0, len(seq), num_columns):
        yield seq[i:i+num_columns]
    return
def iter_split__num_columns__last_row_incomplete__5seq_(num_columns, seq, /):
    '-> Iter subseq{may not tuple}'
    check_int_ge(1, num_columns)
    for j in range(0, 1+len(seq), num_columns):
        row = seq[j:j+num_columns]
        yield row
    assert 0 <= len(row) < num_columns


def iter_split__num_columns__last_row_incomplete__5iterator_(num_columns, it, /, *, mk_row_=tuple):
    '[last row ALWAYS BE incomplete row{maybe empty}]'
    if not iter(it) is it:raise TypeError
    check_int_ge(1, num_columns)
    while 1:
        row = mk_row_(islice(it, 0, num_columns))
        yield row
        if not len(row) == num_columns:
            break

def inv_filterX_(filter_method, num_bytes4filter_gap, jpass2jrow2filtered_bytes7reduced_image, /):
    if not filter_method == 0:raise NotImplementedError(f'filter_method={filter_method}')
    777;inv_filter_method0_
    jpass2jrow2bytes7reduced_image = tuple(inv_filter0__reduced_image_(num_bytes4filter_gap, jrow2filtered_bytes7reduced_image) for jrow2filtered_bytes7reduced_image in jpass2jrow2filtered_bytes7reduced_image)
    return jpass2jrow2bytes7reduced_image
def inv_filter0__reduced_image_(num_bytes4filter_gap, jrow2filtered_bytes7reduced_image, /):
    jrow2bytes7reduced_image = []
    may_payload_bs8prev_row = None
    for bs8filtered_row4reduced_image in jrow2filtered_bytes7reduced_image:
        assert bs8filtered_row4reduced_image
        u8filter_type_byte = bs8filtered_row4reduced_image[0]
        filter_type = FilterType4filter_method0(u8filter_type_byte)
        payload_bs8filtered_row = bs8filtered_row4reduced_image[1:]
        payload_bs8row = inv_filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, filter_type, payload_bs8filtered_row)
        assert len(payload_bs8row) == len(payload_bs8filtered_row)
        jrow2bytes7reduced_image.append(payload_bs8row)
        777; may_payload_bs8prev_row = payload_bs8row
    jrow2bytes7reduced_image = tuple(jrow2bytes7reduced_image)
    return jrow2bytes7reduced_image
def reconstruct_xpixels_(num_bits4segment, num_segments4xpixel, jpass2wh_size4reduced_image, jpass2jrow2bytes7reduced_image, /):
    jpass2jrow2xpixels7reduced_image = []
    for jrow2bytes7reduced_image, (width4reduced_image, height4reduced_image) in zip(jpass2jrow2bytes7reduced_image, jpass2wh_size4reduced_image):
        #num_segments4row = num_segments4xpixel * width4reduced_image
        jrow2xpixels7reduced_image = []
        for payload_bs8row in jrow2bytes7reduced_image:
            xpixels8row = xpixels5bytes8row_(num_bits4segment, num_segments4xpixel, width4reduced_image, payload_bs8row)
            jrow2xpixels7reduced_image.append(xpixels8row)
        jrow2xpixels7reduced_image = tuple(jrow2xpixels7reduced_image)
        jpass2jrow2xpixels7reduced_image.append(jrow2xpixels7reduced_image)
    jpass2jrow2xpixels7reduced_image = tuple(jpass2jrow2xpixels7reduced_image)

    return jpass2jrow2xpixels7reduced_image
def xpixels5bytes8row_(num_bits4segment, num_segments4xpixel, width4reduced_image, payload_bs8row, /):
    iter_segments8row_pad = iter_split_bytes_into_uints__num_bits4uint_(num_bits4segment, payload_bs8row)
    xpixels8row_pad = [*iter_split__num_columns__last_row_incomplete__5iterator_(num_segments4xpixel, iter_segments8row_pad)]
        # [xpixels8row_pad :: [xpixel]]
        # [xpixels8row_pad :: [[segment]]]
    #bug:if not len(xpixels8row_pad) == 1+width4reduced_image:raise Exception(len(xpixels8row_pad), width4reduced_image, (num_bits4segment, num_segments4xpixel))
    #   !! MAYBE [num_bits4xpixel < 8]
    #       e.g.[num_bits4xpixel := 1]@Indexed_color
    num_xpixels8pad = len(xpixels8row_pad) -width4reduced_image
    if not num_xpixels8pad >= 1:raise 000
    segmentss8padding = xpixels8row_pad[width4reduced_image:]
    if any(chain.from_iterable(segmentss8padding)):raise Error__IDAT(segmentss8padding)
    xpixels8row = tuple(xpixels8row_pad[:width4reduced_image])
    if not len(xpixels8row) == width4reduced_image:raise 000
    return xpixels8row
def iter_split_bytes_into_uints__num_bits4uint_(num_bits4uint, bs, /):
    if num_bits4uint < 8:
        return _impl__iter_split_bytes_into_uints__num_bits4uint_lt8_(num_bits4uint, bs)
    return _impl__iter_split_bytes_into_uints__num_bits4uint_ge8_(num_bits4uint, bs)
def _impl__iter_split_bytes_into_uints__num_bits4uint_lt8_(num_bits4uint, bs, /):
    u2us = _nb2u2us[num_bits4uint]
    #bug:return map(u2us.__getitem__, bs)
    return chain.from_iterable(map(u2us.__getitem__, bs))
def _split_byte_into_uints(num_bits4uint, u8byte, /):
    num_uints4byte = perfect_div(8, num_bits4uint)
    def __(u, /):
        mask = mk_max_sample5depth_(num_bits4uint)
        for _ in range(num_uints4byte):
            yield u&mask
            u >>= num_bits4uint
    us = tuple(__(u8byte))[::-1]
    return us
_nb2u2us = {num_bits4uint:tuple(_split_byte_into_uints(num_bits4uint, u8byte) for u8byte in range(0x1_00)) for num_bits4uint in [1,2,4]}
def _impl__iter_split_bytes_into_uints__num_bits4uint_ge8_(num_bits4uint, bs, /):
    num_bytes4uint = perfect_div(num_bits4uint, 8)
    num_uints = perfect_div(len(bs), num_bytes4uint)
    return map(decode8uint_BE_, iter_split__num_rows_(num_uints, bs))

def reconstruct_spng_image7xpixel_(interlace_method, wh_size4canvas, jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling, jpass2jrow2xpixels7reduced_image, /):
    if not 0 <= interlace_method <= 1:raise NotImplementedError(f'interlace_method={interlace_method}')

    if interlace_method == 0:
        #no_interlace
        [jrow2xpixels7spng_image] = jpass2jrow2xpixels7reduced_image
    elif interlace_method == 1:
        #Adam7_interlace
        (width4canvas, height4canvas) = wh_size4canvas
        r2c2x = [[None]*width4canvas for _ in range(height4canvas)]
        for jpass, ((width4reduced_image, height4reduced_image), (idcR, idcC), jrow2xpixels7reduced_image) in enumerate(zip(jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2jrow2xpixels7reduced_image)):
            #for idx8row, idx8column in product(idcR, idcC):
            for jrow4reduced_image, jcolumn4reduced_image in product(range(height4reduced_image), range(width4reduced_image)):
                xpixel = jrow2xpixels7reduced_image[jrow4reduced_image][jcolumn4reduced_image]
                idx8row = idcR[jrow4reduced_image]
                idx8column = idcC[jcolumn4reduced_image]
                r2c2x[idx8row][idx8column] = xpixel
            r2c2x
        r2c2x
        assert not any(x is None  for c2x in r2c2x for x in c2x)
        jrow2xpixels7spng_image = tuple(map(tuple, r2c2x))
    else:
        raise 000
    jrow2xpixels7spng_image

    return jrow2xpixels7spng_image
def reconstruct_spng_image7pixel7RGBA_(color_type4png, sample_depths7RGBA4png, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent, jrow2xpixels7spng_image, /):
    xpixel2pixel7RGBA4png_ = prepare4parse_IDAT__3_(color_type4png, sample_depths7RGBA4png, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent)
    jrow2pixels7RGBA7spng_image = fmap__lsls_(xpixel2pixel7RGBA4png_, jrow2xpixels7spng_image)
    return jrow2pixels7RGBA7spng_image
def fmap__lsls_(x2y, xss, /):
    yss = tuple(tuple(map(x2y, xs)) for xs in xss)
    return yss
def reconstruct_src_image7pixel7RGBA_(sample_depths7RGBA4png, sample_depths7RGBA4src, jrow2pixels7RGBA7spng_image, /):
    assert len(sample_depths7RGBA4png) == 4
    assert len(sample_depths7RGBA4src) == 4
    if sample_depths7RGBA4src == sample_depths7RGBA4png:
        jrow2pixels7RGBA7src_image = jrow2pixels7RGBA7spng_image
    else:
        diffs = tuple(map(int.__sub__, sample_depths7RGBA4png, sample_depths7RGBA4src))
        assert min(diffs) >= 0
        def src_pixel5png_pixel_(png_pixel, /):
            assert len(png_pixel) == 4
            src_pixel = tuple(map(int.__rshift__, png_pixel, diffs))
            return src_pixel
        jrow2pixels7RGBA7src_image = fmap__lsls_(src_pixel5png_pixel_, jrow2pixels7RGBA7spng_image)
    return jrow2pixels7RGBA7src_image #===pixel_matrix7RGBA4src

r'''[[[
sample_depth7A = ?sample_depth7uniform@png?  ([P]8|[A]bit_depth|[L|RGB]1)@src
    LA|RGBA -> bit_depth/sample_depth7uniform@png/scr
    P -> palette7A max_alpha ... 8/sample_depth7uniform@png/scr
    L|RGB -> pixel7RGB8fully_transparent ... 1@src ?bit_depth/sample_depth7uniform@png?

sample_depth7RGB = ?sample_depth7uniform@png sBIT@src
    LA|RGBA|L|RGB -> bit_depth/sample_depth7uniform@png sBIT@src
    P -> 8/sample_depth7uniform@png sBIT@src


#]]]'''#'''
def mk_may_palette7RGBA_(max_sample7A, may_palette7RGB, may_palette7A, /):
    # [1 <= len(palette7A) <= len(palette7RGB) <= 256]
    if not None is may_palette7RGB:
        palette7RGB = may_palette7RGB
        if not 1 <= len(palette7RGB) <= 256:raise Error__PLTE__palette7RGB
        if not None is may_palette7A:
            palette7A = may_palette7A
            if not 0 <= len(palette7A) <= len(palette7RGB) <= 256:raise Error__tRNS__palette7A
        else:
            palette7A = ()
        palette7A
        assert 0 <= len(palette7A) <= len(palette7RGB) <= 256
        #.palette7A_ex = palette7A + (max_sample7A,)*(len(palette7RGB) -len(palette7A))
        #.it = zip(palette7RGB, palette7A)
        it = zip_longest(palette7RGB, palette7A, fillvalue=max_sample7A)
        palette7RGBA = tuple((R,G,B,A) for (R,G,B), A in it)
        may_palette7RGBA = palette7RGBA
    else:
        may_palette7RGBA = None
    return may_palette7RGBA
def mk_sample_depth7uniform5bit_depth_(bit_depth, color_type4png, /):
    sample_depth7uniform = 8 if color_type4png.palette_used else bit_depth
    return sample_depth7uniform
def mk_lowerbound4sample_depth7uniform5sample_depths7XXX4src_(sample_depths7XXX4src, /):
    lowerbound4sample_depth7uniform = 1<<ceil_log2(max(sample_depths7XXX4src))
    return lowerbound4sample_depth7uniform
def mk_sample_depths7RGBA4png_(sample_depth7uniform, /):
    num_bits4sample7png = sample_depth7uniform
    sample_depths7RGBA4png = (num_bits4sample7png,)*4
    return sample_depths7RGBA4png
def mk_sample_depths7RGBA4src_(bit_depth, color_type4png, num_bits4sample7png, may_sample_depths7XXX4src, /):
    if not None is may_sample_depths7XXX4src:
        # has:sBIT
        sample_depths7XXX4src = may_sample_depths7XXX4src
        sample_depths7RGBA4src = mk_sample_depths7RGBA4src5sBIT_(color_type4png, sample_depths7XXX4src)
    else:
        # no:sBIT
        sample_depth7A4src = mk_default_sample_depth7A4src__no_sBIT_(bit_depth, color_type4png)
        num_bits4sample4nonA7src = num_bits4sample7png
        sample_depths7RGB4src = (num_bits4sample4nonA7src,)*3
        sample_depths7RGBA4src = (*sample_depths7RGB4src, sample_depth7A4src)
    sample_depths7RGBA4src
    assert len(sample_depths7RGBA4src) == 4
    return sample_depths7RGBA4src
def mk_default_sample_depth7A4src__no_sBIT_(bit_depth, color_type4png, /):
    num_bits4segment = bit_depth
    if color_type4png.alpha_used:
        # (LA|RGBA)
        A = num_bits4segment # 无sBIT=>全部有效
    elif color_type4png.palette_used:
        # P
        A = 8 # 1byte,全部有效
    else:
        # (L|RGB)
        A = 1 # 完全透明vs完全不透明
    A
    sample_depth7A4src = A
    return sample_depth7A4src
def mk_sample_depths7RGBA4src5sBIT_(color_type4png, sample_depths7XXX4src, /):
    N = Nicknames4ColorType4png
    match color_type4png:
        case N.LA:
            [L,A] = sample_depths7XXX4src
            sample_depths7RGBA4src = (L,L,L,A)
        case N.L:
            #see:pixel7L8fully_transparent
            A = 1 # 完全透明vs完全不透明
            [L] = sample_depths7XXX4src
            sample_depths7RGBA4src = (L,L,L,A)
        case N.P:
            #see:palette7A,sBIT # 1byte,全部有效
            A = 8
            [R,G,B] = sample_depths7XXX4src
            sample_depths7RGBA4src = (R,G,B,A)
        case N.RGB:
            #see:pixel7RGB8fully_transparent
            A = 1 # 完全透明vs完全不透明
            [R,G,B] = sample_depths7XXX4src
            sample_depths7RGBA4src = (R,G,B,A)
        case N.RGBA:
            [R,G,B,A] = sample_depths7XXX4src
            sample_depths7RGBA4src = (R,G,B,A)
        case _:
            raise 000
    return sample_depths7RGBA4src


r'''[[[
Adam7_interlace:
  #抽取(pass_extraction)以 像素(pixel) 为单位 而非字节
  # 但 filtering 以 字节 为 单位,但以 像素 为 间隔 关联 (间隔字节数:1 if bit_depth < 8 else bit_depth*num_channels6dat_mx///8)
1 6 4 6 2 6 4 6
7 7 7 7 7 7 7 7
5 6 5 6 5 6 5 6
7 7 7 7 7 7 7 7
3 6 4 6 3 6 4 6
7 7 7 7 7 7 7 7
5 6 5 6 5 6 5 6
7 7 7 7 7 7 7 7

#]]]'''#'''
jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace = (
(((0,8), (0,8), (8,8))
,((0,8), (4,8), (8,4))
,((4,8), (0,4), (4,4))
,((0,4), (2,4), (4,2))
,((2,4), (0,2), (2,2))
,((0,2), (1,2), (2,1))
,((1,2), (0,1), (2,1))
))
    #.#=>: mx[0::8,0::8]
    #.#=>: mx[0::8,0::4]
    #.#=>: mx[0::4,0::4]
    #.#=>: mx[0::4,0::2]
    #.#=>: mx[0::2,0::2]
    #.#=>: mx[0::2,0::1]
    #.#=>: mx[0::1,0::1]
assert len(jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace) == 7
def _extract(j, xss, /):
    return tuple(xs[j] for xs in xss)
jpass2begin_step_pairs4jrow__4Adam7_interlace = _extract(0, jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace)
jpass2begin_step_pairs4jcolumn__4Adam7_interlace = _extract(1, jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace)
jpass2hw_size4macro_pixel4filling__4Adam7_interlace = _extract(2, jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace)

def prepare4no_interlace_(wh_size4canvas, /):
    (width4canvas, height4canvas) = wh_size4canvas
    idc8rows = range(height4canvas)
    idc8columns = range(width4canvas)
    jpass2idc_pair4RC4reduced_image = ((idc8rows, idc8columns),)
    jpass2wh_size4reduced_image = (wh_size4canvas,)
    jpass2hw_size4macro_pixel4filling = ((1,1),)
    return (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling)
def prepare4Adam7_interlace_(wh_size4canvas, /):
    (width4canvas, height4canvas) = wh_size4canvas
    idc8rows = range(height4canvas)
    idc8columns = range(width4canvas)
    idc_pairs4RC = []
    for (begin4jrow, step4jrow), (begin4jcolumn, step4jcolumn), (height4macro_pixel4filling, width4macro_pixel4filling) in jpass2begin_step_pairs4jrow_jcolumn_and_hw_size4macro_pixel4filling__4Adam7_interlace:
        idc_pairs4RC.append((idc8rows[begin4jrow::step4jrow], idc8columns[begin4jcolumn::step4jcolumn]))
    idc_pairs4RC
    assert len(idc_pairs4RC) == 7
    jpass2idc_pair4RC4reduced_image = tuple(idc_pairs4RC)
    jpass2wh_size4reduced_image = tuple((len(idcC), len(idcR)) for idcR, idcC in idc_pairs4RC)
        # (width4reduced_image:=len(idcC), height4reduced_image:=len(idcR))
    #
    jpass2hw_size4macro_pixel4filling = jpass2hw_size4macro_pixel4filling__4Adam7_interlace
    return (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling)
    #######
    #Adam7_interlace:
    # 1 6 4 6 2 6 4 6
    # 7 7 7 7 7 7 7 7
    # 5 6 5 6 5 6 5 6
    # 7 7 7 7 7 7 7 7
    # 3 6 4 6 3 6 4 6
    # 7 7 7 7 7 7 7 7
    # 5 6 5 6 5 6 5 6
    # 7 7 7 7 7 7 7 7
    #######
    #.#1:
    #.idc_pairs4RC.append((idc8rows[0::8], idc8columns[0::8]))
    #.#=>: mx[0::8,0::8]

    #.#2:
    #.idc_pairs4RC.append((idc8rows[0::8], idc8columns[4::8]))
    #.#=>: mx[0::8,0::4]

    #.#3:
    #.idc_pairs4RC.append((idc8rows[4::8], idc8columns[0::4]))
    #.#=>: mx[0::4,0::4]

    #.#4:
    #.idc_pairs4RC.append((idc8rows[0::4], idc8columns[2::4]))
    #.#=>: mx[0::4,0::2]

    #.#5:
    #.idc_pairs4RC.append((idc8rows[2::4], idc8columns[0::2]))
    #.#=>: mx[0::2,0::2]

    #.#6:
    #.idc_pairs4RC.append((idc8rows[0::2], idc8columns[1::2]))
    #.#=>: mx[0::2,0::1]

    #.#7:
    #.idc_pairs4RC.append((idc8rows[1::2], idc8columns[0::1]))
    #.#=>: mx[0::1,0::1]


class FilterType4filter_method0(IntEnum):
    #filter_type
    NONE = 0
    Sub = 1
    Up = 2
    Average = 3
    Paeth = 4
    @cached_property
    def predictor(sf, /):
        return getattr(Predictors4filter_method0, sf.name)
    # [[[
FilterType4filter_method0.__doc__ = r'''
filter_type


9.1 Filter methods and filter types
  #Filtering transforms the PNG image with the goal of improving compression.
  #Filter type bytes are associated only with non-empty scanlines. No filter type bytes are present in an empty pass.
  #Filters are applied to bytes, not to pixels, regardless of the bit depth or color type of the image.

Table 10 Named filter bytes
Figure 19 Positions of filter bytes a, b and c relative to x
  c ... b
  a ... x
      #a/left, b/above, c/upper_left
      x:the byte being filtered;
      a:the byte corresponding to x in the pixel immediately before the pixel containing x (or the byte immediately before x, when the bit depth is less than 8);
      b:the byte corresponding to x in the previous scanline;

[filter_method==0]
    #Only filter method 0 is defined by this specification.
    #Filter method 0 specifies exactly this set of five filter types and this shall not be extended.
    #   {None/0, Sub/1, Up/2, Average/3, Paeth/4}
[predictor(a,b,c) -> x7pred]
[filter{predictor}(a,b,c;x) =[def]= x-predictor(a,b,c)]
[reconstruction{predictor}(a,b,c;y) =[def]= y+predictor(a,b,c)]
[predictor{filter_method:=0,filter_type:=None/0}(a,b,c) =[def]= 0]
[predictor{filter_method:=0,filter_type:=Sub/1}(a,b,c) =[def]= a]
[predictor{filter_method:=0,filter_type:=Up/2}(a,b,c) =[def]= b]
[predictor{filter_method:=0,filter_type:=Average/3}(a,b,c) =[def]= (a+b)//2] # floor()
[predictor{filter_method:=0,filter_type:=Paeth/4}(a,b,c) =[def]= PaethPredictor(a,b,c)]
def PaethPredictor(a,b,c):
    p = a + b - c
    pa = abs(p - a) # abs(b-c)
    pb = abs(p - b) # abs(a-c)
    pc = abs(p - c) # abs(a+b-2*c)
    if pa <= pb and pa <= pc then Pr = a
        # 认为a最近似x的条件:abs(b-c)最小#理解为 平行线相应近似
    else if pb <= pc then Pr = b
        # 认为b最近似x的条件:abs(a-c)最小#理解为 平行线相应近似
    else Pr = c
        # 认为c最近似x的条件:abs(a+b-2*c)最小#理解为 对角和近似
    return Pr

#不存在的位置，其值缺省为0
  #For all filters, the bytes "to the left of" the first pixel in a scanline shall be treated as being zero.
  #For filters that refer to the prior scanline, the entire prior scanline and bytes "to the left of" the first pixel in the prior scanline shall be treated as being zeroes for the first scanline of a reduced image.

'''#'''
    #]]]


class Predictors4filter_method0:
    def NONE(left, above, diagonal, /):
        return 0
    def Sub(left, above, diagonal, /):
        return left
    def Up(left, above, diagonal, /):
        return above
    def Average(left, above, diagonal, /):
        return (left+above)//2
    def Paeth(left, above, diagonal, /):
        gL = abs(d0:=above - diagonal)
        gA = abs(d1:=left - diagonal)
        gD = abs(d0 + d1)
        gs = ((gL,0), (gA,1), (gD,2))
        (gX, j) = min(gs)
        return (left, above, diagonal)[j]

#.def __():
#.    for nm in FilterType4filter_method0:
#.        FilterType4filter_method0[nm].predictor = getattr(Predictors4filter_method0, nm)
#.__()
assert FilterType4filter_method0.Paeth.predictor is Predictors4filter_method0.Paeth

class _ZeroSeq:
    def __getitem__(sf, j, /):
        return 0
_zero_seq = _ZeroSeq()
def iter4filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, payload_bs8curr_row, /):
    '-> Iter (j, (left, above, diagonal), x) # [payload_bs8curr_row MUST BE original, i.e. unfiltered][payload_bs8curr_row :: bytearray if reconstruction else bytes]'
    #MAYBE:changing when iter:check_type_is(bytearray, payload_bs8curr_row)
    check_int_ge(0, num_bytes4filter_gap)
    payload_bs8prev_row = ifNone(may_payload_bs8prev_row, _zero_seq)
    for j in range(len(payload_bs8curr_row)):
        above = payload_bs8prev_row[j]
        x     = payload_bs8curr_row[j]
        _j = j -num_bytes4filter_gap
        if _j < 0:
            diagonal = 0
            left = 0
        else:
            diagonal = payload_bs8prev_row[_j]
            left     = payload_bs8curr_row[_j]
        yield (j, (left, above, diagonal), x)

def inv_filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, filter_type, payload_bs8filtered_row, /):
    f = filter_type.predictor
    payload_bs8curr_row = bytearray(payload_bs8filtered_row)
    it = iter4filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, payload_bs8curr_row)
    for (j, (left, above, diagonal), dx) in it:
        _x = f(left, above, diagonal)
        x = _x + dx
        payload_bs8curr_row[j] = x&0xFF
    payload_bs8curr_row

    payload_bs8row = bytes(payload_bs8curr_row)
    return payload_bs8row
def filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, filter_type, payload_bs8curr_row, /):
    '-> payload_bs8filtered_row'
    f = filter_type.predictor
    it = iter4filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, payload_bs8curr_row)
    def __(f, /):
        for (j, (left, above, diagonal), x) in it:
            _x = f(left, above, diagonal)
            dx = x -_x
            yield dx&0xFF
    payload_bs8filtered_row = bytes(__(f))
    return payload_bs8filtered_row

FilterType4filter_method0.__members__
assert 5 == len(FilterType4filter_method0)
def filter_method0__adaptive_(num_bytes4filter_gap, may_payload_bs8prev_row, payload_bs8curr_row, /):
    '-> typed_bs4filtered_row'
    if not payload_bs8curr_row:
        return b''

    def __():
        #for u8filter_type_byte in range(len(FilterType4filter_method0.__members__)):
        for u8filter_type_byte in range(len(FilterType4filter_method0)):
            filter_type = FilterType4filter_method0(u8filter_type_byte)
            payload_bs8filtered_row = filter_method0_(num_bytes4filter_gap, may_payload_bs8prev_row, filter_type, payload_bs8curr_row)
            assert len(payload_bs8curr_row) == len(payload_bs8filtered_row)
            yield (u8filter_type_byte, payload_bs8filtered_row)
    (u8filter_type_byte, payload_bs8filtered_row) = min(__(), key=_key_func_4filter_method0__adaptive_)
    filter_type_byte = bytes([u8filter_type_byte])
    typed_bs4filtered_row = filter_type_byte + payload_bs8filtered_row
    return typed_bs4filtered_row
def _key_func_4filter_method0__adaptive_(x, /):
    (u8filter_type_byte, payload_bs8filtered_row) = x
    us = set(payload_bs8filtered_row)
    max_u = max(us)
    return (len(us), max_u-min(us), max_u, u8filter_type_byte)


def check_chunk_type__png_ver3_(chunk_type, /):
    check_type_is(bytes, chunk_type)
    if not len(chunk_type) == 4:raise Error__chunk_type
    if not chunk_type.isalpha():raise Error__chunk_type
        # png_3 => regex"[A-Za-z]{4}"
    return
def is_ancillary__chunk_type_(chunk_type, /):
    critical_vs_ancillary = chunk_type[0:1].islower()
    return critical_vs_ancillary
    public_vs_private = chunk_type[1:2].islower()
    reserved = chunk_type[2:3].islower()
    unsafe_to_copy__vs__safe_to_copy = chunk_type[3:4].islower()

def check_five_byte_uints6IHDR_(bit_depth, color_type, compression_method, filter_method, interlace_method, /):
    #handle_chunk_info__IHDR_
    #   [chunk_data4IHDR == (width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method)]
    check_int_ge_lt(0, 17, bit_depth)
    check_int_ge_lt(0, 7, color_type)
    check_int_ge_lt(0, 1, compression_method)
    check_int_ge_lt(0, 1, filter_method)
    check_int_ge_lt(0, 2, interlace_method)
    color_type4png = ColorType4png(color_type)
    assert color_type4png.value in Data4ColorType4png.values4color_type
    if not bit_depth in color_type4png.values4bit_depth:raise Error__bit_depth(bit_depth, color_type4png)
def check_matrix_shape__wh_(wh_size4mx, mx, /):
    (width4mx, height4mx) = wh_size4mx
    assert len(mx) == height4mx
    assert all(len(row) == width4mx for row in mx)
def check_all_all_(check_, mx, /):
    check_all_([check_all_, check_], mx)
def check_may_pixel7XXX_(sample_depths7XXX, may_pixel7XXX, /):
    check_may_([check_pixel7XXX_, sample_depths7XXX], may_pixel7XXX)
def check_pixel7XXX_(sample_depths7XXX, pixel7XXX, /):
    check_type_is(tuple, pixel7XXX)
    check_all_([check_int_ge, 0], pixel7XXX)
    assert len(pixel7XXX) == len(sample_depths7XXX)
    assert all(sample <= mk_max_sample5depth_(sample_depth) for sample, sample_depth in zip(pixel7XXX, sample_depths7XXX))
def check_pixel_matrix7XXX_(wh_size4canvas, sample_depths7XXX, pixel_matrix7XXX, /):
    check_matrix_shape__wh_(wh_size4canvas, pixel_matrix7XXX)
    check_all_all_([check_pixel7XXX_, sample_depths7XXX], pixel_matrix7XXX)

def check_wh_size4canvas(wh_size4canvas, /):
    check_pair(wh_size4canvas)
    (width4canvas, height4canvas) = wh_size4canvas
    check_pint_31bit_(width4canvas)
    check_pint_31bit_(height4canvas)
def check_pint_31bit_(u, /):
    check_int_ge_lt(1, 0x80_00_00_00, u)
def check_uint_31bit_(u, /):
    check_int_ge_lt(0, 0x80_00_00_00, u)

def check_sample_depths7RGBA4src_(sample_depths7RGBA4src, /):
    check_type_is(tuple, sample_depths7RGBA4src)
    if not len(sample_depths7RGBA4src) == 4:raise TypeError
    check_all_([check_int_ge_lt, 1, 17], sample_depths7RGBA4src)

class Writer4png:
    #Reader4png
    #handle_chunk_info__IHDR_
    #   [chunk_data4IHDR == (width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method)]
    def __init__(sf, /, bit_depth, color_type, compression_method, filter_method, interlace_method,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color):
        check_five_byte_uints6IHDR_(bit_depth, color_type, compression_method, filter_method, interlace_method)
        sf.args = (bit_depth, color_type, compression_method, filter_method, interlace_method,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color)
        sf.color_type4png = ColorType4png(color_type)
    def write__ij2xpixel7png_(sf, obfile, wh_size4canvas, jrow_jcolumn2xpixel7png_, /):
        '[ij2xpixel7png_/jrow_jcolumn2xpixel7png_{after:sample_depth_scaling}{after:alpha_separation,indexing,RGB_merging,alpha_compaction}]'
        check_wh_size4canvas(wh_size4canvas)
        check_callable(jrow_jcolumn2xpixel7png_)
        (width4canvas, height4canvas) = wh_size4canvas
        ij2xpixel7png_ = jrow_jcolumn2xpixel7png_
        jrow2xpixels7spng_image = mx5ij2v_(height4canvas, width4canvas, ij2xpixel7png_)
        sf.write__xpixel_matrix7png_(obfile, wh_size4canvas, jrow2xpixels7spng_image)
    def write__xpixel_matrix7png_(sf, obfile, wh_size4canvas, jrow2xpixels7spng_image, /):
        '[jrow2xpixels7spng_image{after:sample_depth_scaling}{after:alpha_separation,indexing,RGB_merging,alpha_compaction}]'
        check_wh_size4canvas(wh_size4canvas)
        (width4canvas, height4canvas) = wh_size4canvas
        (bit_depth, color_type, compression_method, filter_method, interlace_method,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color) = sf.args
        color_type4png = sf.color_type4png
        write__png_file_signature_(obfile)
        sf.write_chunk__tag_(obfile, b'IHDR', [width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method])
        sf.write_chunk__tag_(obfile, b'sBIT', [color_type4png, may_sample_depths7XXX4src])
        sf.write_chunk__tag_(obfile, b'PLTE', [color_type4png, may_palette7RGB])
        sf.write_chunk__tag_(obfile, b'tRNS', [color_type4png, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent])
        sf.write_chunk__tag_(obfile, b'bKGD', [color_type4png, may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color])
        sf.write_chunk__tag_(obfile, b'IDAT', [color_type4png, bit_depth, compression_method, filter_method, interlace_method, width4canvas, height4canvas, jrow2xpixels7spng_image], many=True)
            #mk_may_chunk_data_seq__IDAT_
        sf.write_chunk__tag_(obfile, b'IEND', [])
        return
    def write_chunk__tag_(sf, obfile, chunk_type, args, /, *, many=False):
        tag = chunk_type.decode('ascii')
        s = '_seq' if many else ''
        mk_may_chunk_data__XXXX_ = globals()[f'mk_may_chunk_data{s}__{tag}_']
        m = mk_may_chunk_data__XXXX_(*args)
        if m is None:
            return
        if many:
            chunk_data_seq = m
        else:
            chunk_data = m
            chunk_data_seq = [chunk_data]
        chunk_data_seq
        for chunk_data in chunk_data_seq:
            write__chunk_(obfile, chunk_type, chunk_data)
#end-class Writer4png:
def write__png_file_signature_(obfile, /):
    obfile.write(png_file_signature)
def write__chunk_(obfile, chunk_type, chunk_data, /):
    check_type_is(bytes, chunk_type)
    check_type_is(bytes, chunk_data)
    check_chunk_type__png_ver3_(chunk_type)
    len4data = len(chunk_data)
    check_uint_31bit_(len4data)
    crc4typ_dat = calc_crc32_([chunk_type, chunk_data])

    write__uint_4byte_BE_(obfile, len4data)
    obfile.write(chunk_type)
    obfile.write(chunk_data)
    write__uint_4byte_BE_(obfile, crc4typ_dat)
    return
def write__uint_4byte_BE_(obfile, u, /):
    bs = encode__uint_4byte_BE_(u)
    obfile.write(bs)
def encode__uint_4byte_BE_(u, /):
    return encode__uint_BE__size_eq_(4, u)
def encode__uint_2byte_BE_(u, /):
    return encode__uint_BE__size_eq_(2, u)
def encode__uint_BE__size_eq_(num_bytes4uint, u, /):
    bs = u.to_bytes(num_bytes4uint, 'big', signed=False)
    assert len(bs) == num_bytes4uint
    return bs
def encode__seq_(encode_, xs, /):
    return b''.join(map(encode_, xs))

def mk_may_chunk_data__IEND_():
    chunk_data = b''
    return chunk_data
def mk_may_chunk_data__IHDR_(width4canvas, height4canvas, bit_depth, color_type, compression_method, filter_method, interlace_method, /):
    #handle_chunk_info__IHDR_
    _5byte = bytes([bit_depth, color_type, compression_method, filter_method, interlace_method])
    chunk_data = b''.join(
        [encode__uint_4byte_BE_(width4canvas)
        ,encode__uint_4byte_BE_(height4canvas)
        ,_5byte
        ])
    return chunk_data
def mk_may_chunk_data__sBIT_(color_type4png, may_sample_depths7XXX4src, /):
    #handle_chunk_info__sBIT_
    if None is may_sample_depths7XXX4src:
        return
    sample_depths7XXX4src = may_sample_depths7XXX4src
    assert len(sample_depths7XXX4src) == color_type4png.num_channels4pixel
    assert max(sample_depths7XXX4src) < 17
    chunk_data = bytes(sample_depths7XXX4src)
    return chunk_data
def mk_may_chunk_data__PLTE_(color_type4png, may_palette7RGB, /):
    #handle_chunk_info__PLTE_
    if None is may_palette7RGB:
        assert not color_type4png.palette_used
        return
    #xxx:assert color_type4png.palette_used
    palette7RGB = may_palette7RGB
    assert 1 <= len(palette7RGB) <= 256
    assert set(map(len, palette7RGB)) <= {3}
    chunk_data = bytes(chain.from_iterable(palette7RGB))
    return chunk_data
def mk_may_chunk_data__tRNS_(color_type4png, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent, /):
    #handle_chunk_info__tRNS_
    if all(None is m for m in [may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent]):
        return
    assert not color_type4png.alpha_used
    N = Nicknames4ColorType4png
    match color_type4png:
        case N.L:
            if None is may_pixel7L8fully_transparent:return
            pixel7L8fully_transparent = may_pixel7L8fully_transparent
            [L] = pixel7L8fully_transparent
            chunk_data = encode__uint_2byte_BE_(L)
        case N.RGB:
            if None is may_pixel7RGB8fully_transparent:return
            pixel7RGB8fully_transparent = may_pixel7RGB8fully_transparent
            [R,G,B] = pixel7RGB8fully_transparent
            chunk_data = encode__seq_(encode__uint_2byte_BE_, [R,G,B])
        case N.P:
            if None is may_palette7A:return
            palette7A = may_palette7A
            chunk_data = bytes(palette7A)
        case _:
            raise 000
    chunk_data
    return chunk_data
def mk_may_chunk_data__bKGD_(color_type4png, may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color, /):
    #handle_chunk_info__bKGD_
    if all(None is m for m in [may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color]):
        return
    N = Nicknames4ColorType4png
    match color_type4png.without_alpha_used:
        case N.L:
            if None is may_pixel7L8background_color:return
            pixel7L8background_color = may_pixel7L8background_color
            [L] = pixel7L8background_color
            chunk_data = encode__uint_2byte_BE_(L)
        case N.RGB:
            if None is may_pixel7RGB8background_color:return
            pixel7RGB8background_color = may_pixel7RGB8background_color
            [R,G,B] = pixel7RGB8background_color
            chunk_data = encode__seq_(encode__uint_2byte_BE_, [R,G,B])
        case N.P:
            if None is may_xpixel7P8background_color:return
            xpixel7P8background_color = may_xpixel7P8background_color
            [palette_index8bg] = xpixel7P8background_color
            chunk_data = bytes([palette_index8bg])
        case _:
            raise 000
    chunk_data
    return chunk_data
def mk_may_chunk_data_seq__IDAT_(color_type4png, bit_depth, compression_method, filter_method, interlace_method, width4canvas, height4canvas, jrow2xpixels7spng_image, /):
    #old:mk_may_chunk_data__IDAT_
    chunk_data_seq4IDAT = encode_IDAT_(color_type4png, bit_depth, compression_method, filter_method, interlace_method, width4canvas, height4canvas, jrow2xpixels7spng_image)
    return chunk_data_seq4IDAT
def encode_IDAT_(color_type4png, bit_depth, compression_method, filter_method, interlace_method, width4canvas, height4canvas, jrow2xpixels7spng_image, /):
    r'''[[[
    '[jrow2xpixels7spng_image{after:sample_depth_scaling}{after:alpha_separation,indexing,RGB_merging,alpha_compaction}] # hence neednot:may_sample_depths7XXX4src'

    ij2xpixel7png_
    :mx5ij2v_:
    jrow2xpixels7spng_image
    :interlaceX_:
    jpass2jrow2xpixels7reduced_image
    :scanline_:
    jpass2jrow2bytes7reduced_image
    :filterX_:
    jpass2jrow2filtered_bytes7reduced_image
    :join_bytesss_:
    filtered_bytes4scanlines4interlaced_png_image
    :compressX_:
    compressed_bytes4scanlines4interlaced_png_image
    :cut_into_chunks_:
    chunk_data_seq4IDAT

    #]]]'''#'''
    #########
    wh_size4canvas = (width4canvas, height4canvas)
    (num_bits4xpixel, num_bytes4filter_gap, num_segments4xpixel, num_bits4segment) = prepare4parse_IDAT__1_(bit_depth, color_type4png)
    (jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, jpass2hw_size4macro_pixel4filling) = prepare4parse_IDAT__2_(interlace_method, wh_size4canvas)
    #########
    #.jrow2xpixels7spng_image = mx5ij2v_(height4canvas, width4canvas, ij2xpixel7png_)
    jpass2jrow2xpixels7reduced_image = interlaceX_(interlace_method, jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, wh_size4canvas, jrow2xpixels7spng_image)
    jpass2jrow2bytes7reduced_image = scanline_(num_bits4segment, num_segments4xpixel, jpass2wh_size4reduced_image, jpass2jrow2xpixels7reduced_image)
    jpass2jrow2filtered_bytes7reduced_image = filterX_(filter_method, num_bytes4filter_gap, jpass2jrow2bytes7reduced_image)
    filtered_bytes4scanlines4interlaced_png_image = join_bytesss_(jpass2jrow2filtered_bytes7reduced_image)
    compressed_bytes4scanlines4interlaced_png_image = compressX_(compression_method, filtered_bytes4scanlines4interlaced_png_image)
    chunk_data_seq4IDAT = cut_into_chunks_(compressed_bytes4scanlines4interlaced_png_image)
    return chunk_data_seq4IDAT

def mx5ij2v_(num_rows, num_columns, ij2v_, /):
    mx = tuple(tuple(ij2v_(jrow, jcolumn) for jcolumn in range(num_columns)) for jrow in range(num_rows))
    return mx

def interlaceX_(interlace_method, jpass2wh_size4reduced_image, jpass2idc_pair4RC4reduced_image, wh_size4canvas, jrow2xpixels7spng_image, /):
    #reconstruct_spng_image7xpixel_
    if not 0 <= interlace_method <= 1:raise NotImplementedError(f'interlace_method={interlace_method}')
    if interlace_method == 0:
        #no_interlace
        jpass2jrow2xpixels7reduced_image = (jrow2xpixels7spng_image,)
    elif interlace_method == 1:
        #Adam7_interlace
        jpass2jrow2xpixels7reduced_image = []
        for (idcR, idcC) in jpass2idc_pair4RC4reduced_image:
            jrow2xpixels7reduced_image = tuple(mk_tuple(xpixels8row7png[idcC.start::idcC.step]) for xpixels8row7png in jrow2xpixels7spng_image[idcR.start::idcR.step])
            jpass2jrow2xpixels7reduced_image.append(jrow2xpixels7reduced_image)
        jpass2jrow2xpixels7reduced_image = tuple(jpass2jrow2xpixels7reduced_image)
    else:
        raise 000
    return jpass2jrow2xpixels7reduced_image
def scanline_(num_bits4segment, num_segments4xpixel, jpass2wh_size4reduced_image, jpass2jrow2xpixels7reduced_image, /):
    jpass2jrow2bytes7reduced_image = []
    for (width4reduced_image, height4reduced_image), jrow2xpixels7reduced_image in zip(jpass2wh_size4reduced_image, jpass2jrow2xpixels7reduced_image):
        num_segments4row = num_segments4xpixel * width4reduced_image
        if num_bits4segment < 8:
            num_segments4byte = perfect_div(8, num_bits4segment)
            num_bytes4row = ceil_div(num_segments4row, num_segments4byte)
            segments8padding = (0,)*(num_bytes4row*num_segments4byte -num_segments4row)
            #imay_num_segments4byte = num_segments4byte
        else:
            num_bytes4segment = perfect_div(num_bits4segment, 8)
            num_bytes4row = num_bytes4segment * num_segments4row
            segments8padding = ()
            #imay_num_segments4byte = -1
        num_bytes4row
        segments8padding
        #imay_num_segments4byte
        jrow2bytes7reduced_image = []
        for xpixels8row in jrow2xpixels7reduced_image:
            bs8row = xpixels2bytes8row_(num_bits4segment, num_bytes4row, segments8padding, xpixels8row)
            jrow2bytes7reduced_image.append(bs8row)
        jrow2bytes7reduced_image = tuple(jrow2bytes7reduced_image)
        jpass2jrow2bytes7reduced_image.append(jrow2bytes7reduced_image)
    jpass2jrow2bytes7reduced_image = tuple(jpass2jrow2bytes7reduced_image)
    return jpass2jrow2bytes7reduced_image
def xpixels2bytes8row_(num_bits4segment, num_bytes4row, segments8padding, xpixels8row, /):
    #xpixels5bytes8row_
    iter_segments8row = chain.from_iterable(xpixels8row)
    iter_segments8row_pad = chain(iter_segments8row, segments8padding)
    if num_bits4segment < 8:
        #num_segments4byte = imay_num_segments4byte
        #iter_split__num_columns__last_row_incomplete__5iterator_(num_segments4byte, iter_segments8row_pad)
        num_bits4segment
        def f(us, /):
            v = 0
            for u in us:
                v = (v<<num_bits4segment) ^ u
            return v
        segments8row_pad = tuple(iter_segments8row_pad)
        if not max(segments8row_pad) <= mk_max_sample5depth_(num_bits4segment):raise Error__segment
        if not min(segments8row_pad) >= 0:raise Error__segment
        bs = bytes(map(f, iter_split__num_rows_(num_bytes4row, segments8row_pad)))
        ...
    elif num_bits4segment == 8:
        bs = bytes(segments8row_pad)
    elif num_bits4segment == 16:
        bs = encode__seq_(encode__uint_2byte_BE_, segments8row_pad)
    else:
        raise Error__num_bits4segment(num_bits4segment)
    bs
    return bs

def filterX_(filter_method, num_bytes4filter_gap, jpass2jrow2bytes7reduced_image, /):
    #inv_filterX_
    if not filter_method == 0:raise NotImplementedError(f'filter_method={filter_method}')
    777;filter_method0_,filter_method0__adaptive_
    jpass2jrow2filtered_bytes7reduced_image = tuple(filter0__reduced_image_(num_bytes4filter_gap, jrow2bytes7reduced_image) for jrow2bytes7reduced_image in jpass2jrow2bytes7reduced_image)
    return jpass2jrow2filtered_bytes7reduced_image
def filter0__reduced_image_(num_bytes4filter_gap, jrow2bytes7reduced_image, /):
    #inv_filter0__reduced_image_
    #FilterType4filter_method0
    if not (jrow2bytes7reduced_image and jrow2bytes7reduced_image[0]):
        jrow2filtered_bytes7reduced_image = mk_tuple(jrow2bytes7reduced_image)
    else:
        jrow2filtered_bytes7reduced_image = []
        may_payload_bs8prev_row = None
        for payload_bs8row in jrow2bytes7reduced_image:
            assert payload_bs8row
            typed_bs4filtered_row = filter_method0__adaptive_(num_bytes4filter_gap, may_payload_bs8prev_row, payload_bs8row)
            jrow2filtered_bytes7reduced_image.append(typed_bs4filtered_row)
            777; may_payload_bs8prev_row = payload_bs8row
        jrow2filtered_bytes7reduced_image = tuple(jrow2filtered_bytes7reduced_image)
    return jrow2filtered_bytes7reduced_image
def join_bytesss_(bsss, /):
    return b''.join(bs for bss in bsss for bs in bss)
def compressX_(compression_method, filtered_bytes4scanlines4interlaced_png_image, /):
    #decompressX_
    if not compression_method == 0:raise NotImplementedError(f'compression_method={compression_method}')
    cobj = zlib.compressobj()
    bs = cobj.compress(filtered_bytes4scanlines4interlaced_png_image)
    bs += cobj.flush()
    compressed_bytes4scanlines4interlaced_png_image = bs
    return compressed_bytes4scanlines4interlaced_png_image


def cut_into_chunks_(compressed_bytes4scanlines4interlaced_png_image, /):
    max_len4data = 0x80_00_00_00-1
    #chunk_data_seq4IDAT = [*iter_split__num_columns__last_row_incomplete__5iterator_(max_len4data, iter(compressed_bytes4scanlines4interlaced_png_image), mk_row_=bytes)]
    chunk_data_seq4IDAT = [*iter_split__num_columns__last_row_incomplete__5seq_(max_len4data, compressed_bytes4scanlines4interlaced_png_image)]
    if not chunk_data_seq4IDAT[-1]:
        chunk_data_seq4IDAT.pop()
    chunk_data_seq4IDAT = tuple(chunk_data_seq4IDAT)
    return chunk_data_seq4IDAT

r'''[[[
alpha_separation
    LA->L
    RGBA->RGB
indexing or ( [RGB_merging] [alpha_compaction] )
    RGB_merging
        RGBA -> LA
        RGB -> L
    indexing
        RGBA -> P+palette7A
        RGB -> P
        LA -> P+palette7A
        xxx:L -> P
        P
    alpha_compaction
        LA->L+fully_transparent
        RGBA->RGB+fully_transparent
sample_depth_scaling
    may_sample_depths7XXX4src -> bit_depth

#]]]'''#'''
def mk_may_set__size_le_(max_sz, xs, /):
    check_int_ge(0, max_sz)
    s = set()
    for x in xs:
        s.add(x)
        if len(s) > max_sz:
            return None
    assert len(s) <= max_sz
    return s
def mk_may_counter__size_le_(max_sz, xs, /):
    c = mk_Counter_()
    check_int_ge(0, max_sz)
    for x in xs:
        c[x] += 1
        if len(c) > max_sz:
            return None
    assert len(c) <= max_sz
    return c

def mk_scale_sample_depth__std_(sample_depth7src, sample_depth7dst, /):
    check_int_ge(1, sample_depth7src)
    check_int_ge(sample_depth7src, sample_depth7dst)
    d = sample_depth7dst -sample_depth7src
    if not d >= 0:raise 000#Error__sample_depth
    if d == 0:
        # !! [sample7dst := sample7src]
        scale_sample_depth__std_ = force_lazy_imported_func_(echo)
    else:
        max_sample7src = mk_max_sample5depth_(sample_depth7src)
        max_sample7dst = mk_max_sample5depth_(sample_depth7dst)
        def scale_sample_depth__std_(sample7src, /):
            # [sample7dst := floor(0.5 + sample7src / max_sample7src * max_sample7dst)]
            # [sample7dst == floor(1/2 + sample7src * max_sample7dst / max_sample7src)]
            # [sample7dst == (max_sample7src + 2*sample7src*max_sample7dst) // (2*max_sample7src)]
            sample7dst = (max_sample7src + 2*sample7src*max_sample7dst) // (2*max_sample7src)
            return sample7dst
        scale_sample_depth__std_
    scale_sample_depth__std_
    return scale_sample_depth__std_
def alpha_separation_(sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, /):
    max_alpha = mk_max_sample5depth_(sample_depths7RGBA4src[-1])
    mx7RGBA = jrow2pixels7RGBA7src_image
    color_type4png = ColorType4png.Truecolor_with_alpha
    alpha_used = not all(pixel7RGBA[-1] == max_alpha for row in mx7RGBA for pixel7RGBA in row)
    if not alpha_used:
        #alpha_separation
        color_type4png = ColorType4png.Truecolor
        mx7XXX4src = fmap__lsls_(lambda pixel7RGBA:pixel7RGBA[:-1], mx7RGBA)
        sample_depths7XXX4src = sample_depths7RGBA4src[:-1]
        assert len(sample_depths7XXX4src) == 3
    else:
        mx7XXX4src = mx7RGBA
        sample_depths7XXX4src = sample_depths7RGBA4src
        assert len(sample_depths7XXX4src) == 4
    assert alpha_used is color_type4png.alpha_used
    assert len(sample_depths7XXX4src) in (3,4)
    return (color_type4png, sample_depths7XXX4src, mx7XXX4src)
def alpha_compaction_(color_type4png, sample_depths7XXX4src, mx7XXX4src, /):
    if color_type4png.alpha_used:
        #RGBA
        assert len(sample_depths7XXX4src) == 4
        mx7RGBA = mx7XXX4src
        sample_depths7RGBA4src = sample_depths7XXX4src
        #########
        sample_depth7A = sample_depths7RGBA4src[3]
        max_sample7A = mk_max_sample5depth_(sample_depth7A)
        iter_pixels7RGBA = (pixel7RGBA for row in mx7RGBA for pixel7RGBA in row)
        n = 0
        for (R,G,B,A) in iter_pixels7RGBA:
            RGB = (R,G,B)
            if A == 0:
                if n == 0:
                    n += 1
                    pixel7RGB8fully_transparent = RGB
                elif pixel7RGB8fully_transparent == RGB:
                    pass
                else:
                    n += 1
                    ok = False
                    break
            elif A == max_sample7A:
                pass
            else:
                ok = False
                break
        else:
            ok = True
            if n==0:raise Error__alpha_separation
            if not n==1:raise 000
            pixel7RGB8fully_transparent
            iter_pixels7RGBA = (pixel7RGBA for row in mx7RGBA for pixel7RGBA in row)
            ok = all((A==0) is (RGB==pixel7RGB8fully_transparent) for (*RGB,A) in iter_pixels7RGBA)
        ok, n
        #########
        may_pixel7RGB8fully_transparent4src = pixel7RGB8fully_transparent if ok else None
        if ok:
            #alpha_compaction
            color_type4png = ColorType4png.Truecolor
            mx7XXX4src = fmap__lsls_(lambda pixel7RGBA:pixel7RGBA[:-1], mx7RGBA)
            sample_depths7XXX4src = sample_depths7RGBA4src[:-1]
            assert len(sample_depths7XXX4src) == 3
        #########
        (color_type4png, sample_depths7XXX4src, mx7XXX4src)
        may_pixel7RGB8fully_transparent4src
    else:
        #RGB
        assert len(sample_depths7XXX4src) == 3
        may_pixel7RGB8fully_transparent4src = None
    assert len(sample_depths7XXX4src) in (3,4)
    tmay_pixel7RGB8fully_transparent4src = may2tmay_(may_pixel7RGB8fully_transparent4src)
    return (color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src)
def try_indexing_(color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src, tmay_pixel7RGB8background_color4src, /):
    #########
    if len(sample_depths7XXX4src) == 3:
        tmay_pixel7XXX8background_color4src = tmay_pixel7RGB8background_color4src
    elif len(sample_depths7XXX4src) == 4:
        max_sample7A = mk_max_sample5depth_(sample_depths7XXX4src[3])
        tmay_pixel7XXX8background_color4src = fmap_tmay_(lambda RGB:(*RGB,max_sample7A), tmay_pixel7RGB8background_color4src)
    else:
        raise 000
    tmay_pixel7XXX8background_color4src
    #########
    iter_pixels7XXX4src = chain(tmay_pixel7XXX8background_color4src, (pixel7XXX4src for row in mx7XXX4src for pixel7XXX4src in row))
    if max(sample_depths7XXX4src) <= 8 and not None is (pixel_set7XXX4src:=mk_may_set__size_le_(256, iter_pixels7XXX4src)):
        palette7XXX4src = sorted(pixel_set7XXX4src, key=lambda pixel7XXX4src:pixel7XXX4src[::-1])
        d = {pixel7XXX4src:(j,) for j, pixel7XXX4src in enumerate(palette7XXX4src)}
        mx7P = fmap__lsls_(d.__getitem__, mx7XXX4src)
        tmay_xpixel7P8background_color4src = fmap_tmay_(d.__getitem__, tmay_pixel7XXX8background_color4src)
        #xxx:may_pixel7P8fully_transparent = None if may_pixel7RGB8fully_transparent4src is None else (d[may_pixel7RGB8fully_transparent4src],)
        #   !! may_palette7A

        sample_depth7dst = 8
        if not min(sample_depths7XXX4src) == sample_depth7dst:
            scales_ = [mk_scale_sample_depth__std_(sample_depth7src, sample_depth7dst) for sample_depth7src in sample_depths7XXX4src]
            def f(pixel7XXX4src, /):
                pixel7XXX4png = tuple(scale_sample_depth__std_(sample7src)for scale_sample_depth__std_, sample7src in zip(scales_, pixel7XXX4src))
                return pixel7XXX4png
            palette7XXX4png = tuple(map(f, palette7XXX4src))
        else:
            palette7XXX4png = palette7XXX4src
        palette7XXX4png
        if color_type4png.alpha_used:
            # RGBA
            sample_depths7XXX4src = sample_depths7XXX4src[:-1]
            palette7RGBA = palette7XXX4png
            palette7RGB = _extract(slice(0,3), palette7RGBA)
            palette7A = _extract(3, palette7RGBA)
            #.sample_depth7A = sample_depths7RGBA4src[3]
            #.max_sample7A = mk_max_sample5depth_(sample_depth7A)
            if palette7A[-1] == max_sample7A:
                j = palette7A.index(max_sample7A)
                palette7A = palette7A[:j]
            else:
                palette7A
                pass
            palette7A
            may_palette7A = palette7A
        else:
            # RGB
            palette7RGB = palette7XXX4png
            may_palette7A = None
        color_type4png = ColorType4png.Indexed_color
        sample_depths7XXX4src
        assert len(sample_depths7XXX4src) == 3
        palette7RGB, may_palette7A
        may_palette7RGB = palette7RGB
        return (color_type4png, sample_depths7XXX4src, palette7RGB, may_palette7A, mx7P, tmay_xpixel7P8background_color4src)
    else:
        return None

def sample_depth_scaling_(color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src, tmay_pixel7RGB8background_color4src, /):
    'called only if try_indexing_() fail'
    assert not color_type4png.palette_used
    lowerbound4sample_depth7uniform = mk_lowerbound4sample_depth7uniform5sample_depths7XXX4src_(sample_depths7XXX4src)
    if lowerbound4sample_depth7uniform > 16:raise Error__sample_depths7XXX4src
    sample_depth7uniform = lowerbound4sample_depth7uniform
        # !! not Indexed_color
    sample_depth7dst = sample_depth7uniform
    assert max(sample_depths7XXX4src) <= sample_depth7dst
    if not min(sample_depths7XXX4src) == sample_depth7dst:
        #sample_depth_scaling
        scales_ = [mk_scale_sample_depth__std_(sample_depth7src, sample_depth7dst) for sample_depth7src in sample_depths7XXX4src]
        def f(pixel7XXX4src, /):
            pixel7XXX4png = tuple(scale_sample_depth__std_(sample7src)for scale_sample_depth__std_, sample7src in zip(scales_, pixel7XXX4src))
            return pixel7XXX4png
        mx7XXX4png = fmap__lsls_(f, mx7XXX4src)
        scales_ = scales_[:3]
        assert len(scales_) == 3
        777;tmay_pixel7RGB8fully_transparent4png = fmap_tmay_(f, tmay_pixel7RGB8fully_transparent4src)
        777;tmay_pixel7RGB8background_color4png = fmap_tmay_(f, tmay_pixel7RGB8background_color4src)
    else:
        #no scale
        tmay_pixel7RGB8fully_transparent4png = tmay_pixel7RGB8fully_transparent4src
        tmay_pixel7RGB8background_color4png = tmay_pixel7RGB8background_color4src
        mx7XXX4png = mx7XXX4src
    mx7XXX4png
    return (color_type4png, sample_depth7uniform, mx7XXX4png, tmay_pixel7RGB8fully_transparent4png, tmay_pixel7RGB8background_color4png)
def rgb_merging_(color_type4png, sample_depth7uniform, mx7XXX4png, tmay_pixel7RGB8fully_transparent4png, tmay_pixel7RGB8background_color4png, /):
    assert color_type4png.truecolor_used
    iter_pixels7RGB4png = chain(tmay_pixel7RGB8fully_transparent4png, tmay_pixel7RGB8background_color4png, (pixel7XXX4png[:3] for row in mx7XXX4png for pixel7XXX4png in row))
    tmay_pixel7XXX8fully_transparent4png = tmay_pixel7RGB8fully_transparent4png
    tmay_pixel7XXX8background_color4png = tmay_pixel7RGB8background_color4png
    # !! sample_depth7uniform
    # => (R,G,B) compareable
    if all(R==G==B for (R,G,B) in iter_pixels7RGB4png):
        #RGB_merging
        tmay_pixel7XXX8fully_transparent4png = fmap_tmay_(lambda RGB:RGB[:1], tmay_pixel7RGB8fully_transparent4png)
        tmay_pixel7XXX8background_color4png = fmap_tmay_(lambda RGB:RGB[:1], tmay_pixel7RGB8background_color4png)
        mx7XXX4png = fmap__lsls_(lambda pixel7XXX4png:pixel7XXX4png[::3], mx7XXX4png)
        color_type4png = color_type4png.without_truecolor_used
        sample_depths7XXX4src = sample_depths7XXX4src[::3]
        assert len(sample_depths7XXX4src) in (1,2)
    else:
        assert len(sample_depths7XXX4src) in (3,4)
    assert len(sample_depths7XXX4src) in (1,2,3,4)
    return (color_type4png, sample_depths7XXX4src, sample_depth7uniform, mx7XXX4png, tmay_pixel7XXX8fully_transparent4png, tmay_pixel7XXX8background_color4png)
def preprocess__pixel_matrix7RGBA4src_(wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, may_pixel7RGB8background_color4src, /):
    #pixel_matrix7RGBA4src~jrow2pixels7RGBA7src_image
    check_wh_size4canvas(wh_size4canvas)
    check_sample_depths7RGBA4src_(sample_depths7RGBA4src)
    check_pixel_matrix7XXX_(wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image)
    check_may_pixel7XXX_(sample_depths7RGBA4src[:-1], may_pixel7RGB8background_color4src)
    tmay_pixel7RGB8background_color4src = may2tmay_(may_pixel7RGB8background_color4src)
        #-->may_xpixel7XXX8background_color
        #   * may_xpixel7P8background_color
        #   * may_pixel7L8background_color
        #   * may_pixel7RGB8background_color

    #update:sample_depths7XXX4src
    (color_type4png, sample_depths7XXX4src, mx7XXX4src) = alpha_separation_(sample_depths7RGBA4src, jrow2pixels7RGBA7src_image)
    assert len(sample_depths7XXX4src) in (3,4)
    777;tmay_pixel7RGB8background_color4src

    (color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src) = alpha_compaction_(color_type4png, sample_depths7XXX4src, mx7XXX4src)
    assert len(sample_depths7XXX4src) in (3,4)
    777;tmay_pixel7RGB8background_color4src


    m = try_indexing_(color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src, tmay_pixel7RGB8background_color4src)
    if not None is m:
        (color_type4png, sample_depths7XXX4src, palette7RGB, may_palette7A, mx7P, tmay_xpixel7P8background_color4src) = m
        assert len(sample_depths7XXX4src) == 3
        may_palette7RGB = palette7RGB
        may_palette7A
        (may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent) = (None, None)

        may_xpixel7P8background_color = may5tmay_(tmay_xpixel7P8background_color4src)
        (may_pixel7L8background_color, may_pixel7RGB8background_color) = (None, None)
        assert 1 <= len(palette7RGB) <= 256
        min_num_bits4palette_index = ceil_log2(len(palette7RGB))
        num_bits4segment = 1<<ceil_log2(min_num_bits4palette_index)
        jrow2xpixels7spng_image = mx7P
        #########
        #########
    else:
        assert len(sample_depths7XXX4src) in (3,4)
        (color_type4png, sample_depth7uniform, mx7XXX4png, tmay_pixel7RGB8fully_transparent4png, tmay_pixel7RGB8background_color4png) = sample_depth_scaling_(color_type4png, sample_depths7XXX4src, mx7XXX4src, tmay_pixel7RGB8fully_transparent4src, tmay_pixel7RGB8background_color4src)
        (color_type4png, sample_depths7XXX4src, sample_depth7uniform, mx7XXX4png, tmay_pixel7XXX8fully_transparent4png, tmay_pixel7XXX8background_color4png) = rgb_merging_(color_type4png, sample_depth7uniform, mx7XXX4png, tmay_pixel7RGB8fully_transparent4png, tmay_pixel7RGB8background_color4png)
        assert len(sample_depths7XXX4src) in (1,2,3,4)
        may_palette7RGB = None
        may_palette7A = None
        (may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent) = (None, may5tmay_(tmay_pixel7XXX8fully_transparent4png))[::(1 if color_type4png.truecolor_used else -1)]

        may_xpixel7P8background_color = None
        (may_pixel7L8background_color, may_pixel7RGB8background_color) = (None, may5tmay_(tmay_pixel7XXX8background_color4png))[::(1 if color_type4png.truecolor_used else -1)]
        num_bits4segment = sample_depth7uniform
        jrow2xpixels7spng_image = mx7XXX4png
        #########
        #########
    may_sample_depths7XXX4src = sample_depths7XXX4src
    bit_depth = num_bits4segment
    may_palette7RGB
    may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent
    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color

    return (jrow2xpixels7spng_image, (bit_depth, color_type4png,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color))


def dump_png_file__pixel_matrix7RGBA4src_(may_obfile_or_opath8png_file, wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, /, *, may_pixel7RGB8background_color4src=None, compression_method=0, filter_method=0, interlace_method=1, force=False):
    '[interlace_method == (0/no_interlace|1/Adam7_interlace)]'
    #pixel_matrix7RGBA4src~jrow2pixels7RGBA7src_image
    (jrow2xpixels7spng_image, (bit_depth, color_type4png,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color)) = preprocess__pixel_matrix7RGBA4src_(wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, may_pixel7RGB8background_color4src)

    color_type = color_type4png.value
    sf = Writer4png(bit_depth, color_type, compression_method, filter_method, interlace_method,     may_sample_depths7XXX4src, may_palette7RGB, may_palette7A, may_pixel7L8fully_transparent, may_pixel7RGB8fully_transparent,    may_xpixel7P8background_color, may_pixel7L8background_color, may_pixel7RGB8background_color)
    #.if 0b00001:assert force
    with open4wb_(may_obfile_or_opath8png_file, force=force) as obfile:
        sf.write__xpixel_matrix7png_(obfile, wh_size4canvas, jrow2xpixels7spng_image)




def convert_png_file__switch01_interlace_method_(may_ibfile_or_ipath8png_file, may_obfile_or_opath8png_file, /, *, force=False):
    #.if 0b00001:assert force
    (result4decode_IDAT, image_info_dict) = load_png_file__both_mx8src_and_mx8png_(may_ibfile_or_ipath8png_file, with_image_info_dict=True)
    ((sample_depths7RGBA4src, jrow2pixels7RGBA7src_image), (sample_depths7RGBA4png, jrow2pixels7RGBA7spng_image)) = result4decode_IDAT
    d = image_info_dict
    wh_size4canvas = d['wh_size4canvas']
    interlace_method = d['interlace_method']
    may_pixel7RGB8background_color4png = d.get('pixel7RGB8background_color')
    may_pixel7RGB8background_color4src = None
    dump_png_file__pixel_matrix7RGBA4src_(may_obfile_or_opath8png_file, wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, may_pixel7RGB8background_color4src=may_pixel7RGB8background_color4src, interlace_method=1-interlace_method, force=force)



__all__
from script.png.simple_reader_writer4png import load_png_file__both_mx8src_and_mx8png_
from script.png.simple_reader_writer4png import dump_png_file__pixel_matrix7RGBA4src_, preprocess__pixel_matrix7RGBA4src_

from script.png.simple_reader_writer4png import BaseError
from script.png.simple_reader_writer4png import ColorType4png, FilterType4filter_method0

from script.png.simple_reader_writer4png import Reader4png, decode_IDAT_
from script.png.simple_reader_writer4png import Writer4png, encode_IDAT_

from script.png.simple_reader_writer4png import *
