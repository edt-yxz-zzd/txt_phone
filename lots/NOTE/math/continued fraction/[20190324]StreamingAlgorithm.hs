

{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE TypeFamilyDependencies #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}
{-# LANGUAGE ExplicitForAll #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE AllowAmbiguousTypes #-}
{-# LANGUAGE DefaultSignatures #-}


{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE StandaloneDeriving #-}
{-# LANGUAGE UndecidableInstances #-}


{-
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE TypeSynonymInstances #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE UndecidableSuperClasses #-}
{-# LANGUAGE FlexibleInstances #-}
-}
{-
see:
    "[A001203]pi.txt"
        matrix as linear fractional transformation
    https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
        "Unbounded Spigot Algorithms for the Digits of Pi (2006)(Gibbons).pdf"


    usage:

        constant_outputs = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_???
        float_part_number_convertor (mkRadixBaseFloatPartNumber baseI [???]) baseO

        > runghc StreamingAlgorithm.hs
        > ghci StreamingAlgorithm.hs
        > StreamingAlgorithm.hs
        :re
        main_fastest
        Ctrl+C
        main
        Ctrl+C
        main_all
        :quit

-}


{-
    grep "^[a-z]\w* *\($\|=\|::\)" StreamingAlgorithm.hs
    grep "^class" StreamingAlgorithm.hs
    grep "^data" StreamingAlgorithm.hs
    grep "^newtype" StreamingAlgorithm.hs
    grep "^type" StreamingAlgorithm.hs
-}

module StreamingAlgorithm
    (Callable(..)
    ,PartialCallable(..)
    ,Transform(..)
    ,PartialTransform(..)
    ,Standardizable(..)
    ,EqStandardizable(..)
    ,StreamingAlgorithm(..)

    ,streaming
    ,LinearFractionalTransformation(..)
    -- ,call_LinearFractionalTransformation
    ,RadixBases4Convert(..)
    ,FloatPartRadixBaseConvertorState(..)

    ,RadixBaseFloatPartNumber() -- Nothing
    ,unRadixBaseFloatPartNumber
    ,mkRadixBaseFloatPartNumber
    ,finite_maybe_mkRadixBaseFloatPartNumber
    ,float_part_number_convertor
    -- ,float_part_digits_convertor
    ,finite_float_part_number2rational
    -- ,finite_float_part_digits2rational

    ,Label(..)
    ,unLabel
    ,mkLabel_
    ,change_label
    ,change_label_

    ,ConstantStreamingAlgorithm(..)
    ,the_labelled_constant_outputs
    ,the_constant_inputs_
    ,the_constant_outputs_

    ,Configure4ConstantStreamingAlgorithm(..)
    ,Generator4ConstantStreamingAlgorithm(..)
    ,FloorOutput4ConstantStreamingAlgorithm(..)
    ,the_labelled_output_digit2inv_output_func_

    ,BasicState4ConstantStreamingAlgorithm(..)
    ,Configure4LinearFractionalTransformation()
    ,FloorOutput__continued_fraction()
    ,FloorOutput__base10()
    ,FloorOutput__base16()
    ,FloorOutput__base2()
    ,FloorOutput__base3()
    ,FloorOutput__base7()
    ,Generator4Pi__Rabinowitz_and_Wagon()
    ,Generator4Pi__Lambert()
    ,Generator4Pi__Gosper()

    ,State4ConstantStreamingAlgorithm(..)

    -- ,Pair
    ,IO_Type4Transform
    ,Type4PartialTransform
    ,Number4ConstantStreamingAlgorithm
    ,Number4Generator4ConstantStreamingAlgorithm
    ,InputCallable4ConstantStreamingAlgorithm
    ,Number4FloorOutput4ConstantStreamingAlgorithm
    ,OutputCallable4ConstantStreamingAlgorithm
    ,State4Pi_base10__Rabinowitz_and_Wagon
    ,State4Pi_base10__Lambert
    ,State4Pi_base10__Gosper
    ,State4Pi_continued_fraction__Rabinowitz_and_Wagon
    ,State4Pi_continued_fraction__Lambert
    ,State4Pi_continued_fraction__Gosper

    ,the_digits_of_pi_base10__Rabinowitz_and_Wagon
    ,the_digits_of_pi_base10__Lambert
    ,the_digits_of_pi_base10__Gosper
    ,the_digits_of_pi_continued_fraction__Rabinowitz_and_Wagon
    ,the_digits_of_pi_continued_fraction__Lambert
    ,the_digits_of_pi_continued_fraction__Gosper


    -- e_base3 e_base7
    ,the_digits_of_pi_continued_fraction__from_A001203
    ,the_digits_of_pi_base10__from_A000796
    ,main
    {-
    ,main_fastest_cf
    ,main_all
    ,main1__radix_base_convert
    ,main2__show_all_pi
    ,main3__test_all_pi_base10
    ,main4__test_all_pi_cf
    -}
    )
where

--import Control.Category
--  ==>> Monoid
import Control.Exception(assert)
import Data.Semigroup
-- import Data.Traversable (forM)
import Control.Monad (forM_, unless, when, guard, mzero)
import Data.List (zip4)

class Callable a where
    type InputType4Callable a :: *
    type OutputType4Callable a :: *
    call :: a -> InputType4Callable a -> OutputType4Callable a
class (Callable a
        , OutputType4Callable a ~ Maybe (PartialOutputType4Callable a)
    ) => PartialCallable a where
    type PartialOutputType4Callable a :: *
    partial_call :: a -> InputType4Callable a -> Maybe (PartialOutputType4Callable a)
    partial_call = call

type IO_Type4Transform a = OutputType4Callable a
type Type4PartialTransform a = PartialOutputType4Callable a
class (Callable a
        , InputType4Callable a ~ OutputType4Callable a
        , Semigroup a
        , Monoid a
    ) => Transform a where
    transform :: a -> IO_Type4Transform a -> IO_Type4Transform a
    transform = call


class (PartialCallable a
        , InputType4Callable a ~ PartialOutputType4Callable a
        , Semigroup a
        , Monoid a
    ) => PartialTransform a where
    partial_transform :: a -> Type4PartialTransform a -> Maybe (Type4PartialTransform a)
    partial_transform = partial_call





class Standardizable a where
    -- std . std == std
    std :: a -> a
class Standardizable a => EqStandardizable a where
    -- nonstd_eq a a == True
    -- nonstd_eq a b == nonstd_eq b a
    -- [nonstd_eq a b][nonstd_eq b c] ==>> [nonstd_eq a c]
    -- [nonstd_eq a b] ==>> [std_eq a b]
    -- [std_eq a b] <==> [nonstd_eq (std a) (std b)]
    nonstd_eq :: a -> a -> Bool
    std_eq :: a -> a -> Bool
    std_eq lhs rhs = nonstd_eq (std lhs) (std rhs)



class Standardizable state => StreamingAlgorithm state where
    {- # MINIMAL
            update_after_consume
            , (maybe_poll | maybe_peek, unsafe_update_after_poll)
        # -}

    type OutputType4StreamingAlgorithm state :: *
    type InputType4StreamingAlgorithm state :: *

    maybe_poll
        :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    update_after_consume
        :: state -> InputType4StreamingAlgorithm state -> state

    {-
    type PseudoOutputType4StreamingAlgorithm state :: *
    pseudo_peek
        :: state -> PseudoOutputType4StreamingAlgorithm state
    pseudo_output2maybe_output
        :: state -> PseudoOutputType4StreamingAlgorithm state
        -> Maybe (OutputType4StreamingAlgorithm state)
    -}

    {-
    maybe_peek
        :: state -> Maybe (OutputType4StreamingAlgorithm state)
    unsafe_update_after_poll
        :: state -> OutputType4StreamingAlgorithm state -> state

    maybe_poll state = do
        output <- maybe_peek state
        return $ (unsafe_update_after_poll state output, output)
    maybe_peek state = do
        (state', output) <- maybe_poll state
        return output
    unsafe_update_after_poll state output
        = maybe undefined fst $ maybe_poll state
    -}

streaming
    :: StreamingAlgorithm state
    => state -> [InputType4StreamingAlgorithm state]
    -> [OutputType4StreamingAlgorithm state]
streaming _state inputs = let state = std _state in
    case maybe_poll state of
        Just (state', output) -> output : streaming state' inputs
        Nothing -> case inputs of
            (h:inputs') -> streaming (update_after_consume state h) inputs'
            [] -> []
















data LinearFractionalTransformation
    = LinearFractionalTransformation
        {up_left :: Integer
        ,up_right :: Integer
        ,down_left :: Integer
        ,down_right :: Integer
        }
        deriving (Read, Show)
    {-
    matrix[ul, ur; dl, dr](x) = (ul*x+ur)/(dl*x+dr)
    I = matrix[1,0; 0,1]
    I(x) = (1*x+0)/(0*x+1) = x
    -}


-- call_LinearFractionalTransformation :: LinearFractionalTransformation -> Rational -> Rational
instance Callable LinearFractionalTransformation where
    type InputType4Callable LinearFractionalTransformation = Rational
    type OutputType4Callable LinearFractionalTransformation = Maybe Rational
    call
        LinearFractionalTransformation
            {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
        x
        = if denominator == 0 then Nothing
            else Just $ numerator/denominator
        where
            f l r x = toRational l * x + toRational r
            numerator  = f ul ur x
            denominator = f dl dr x
instance PartialCallable LinearFractionalTransformation where
    type PartialOutputType4Callable LinearFractionalTransformation = Rational
instance PartialTransform LinearFractionalTransformation where


instance Standardizable LinearFractionalTransformation where
    std LinearFractionalTransformation
            {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
        = if (dl == 0 && dr == 0) then _mkLFT (0,0,0,0) else
            let g = gcd ul . gcd ur $ gcd dl dr
                -- sign of (dl, dr) <- [0+, +0, ++, +-]
                to_neg = if dr < 0 then dl <= 0 else dl < 0
                g' = if to_neg then -g else g
            in  _mkLFT . _divLFT g' $ (ul, ur, dl, dr)
_unLFT LinearFractionalTransformation
    {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
    = (ul, ur, dl, dr)
_mkLFT (ul, ur, dl, dr) = LinearFractionalTransformation
    {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
_divLFT g (ul, ur, dl, dr) = (div ul g, div ur g, div dl g, div dr g)
_negLFT (ul, ur, dl, dr) = (-ul, -ur, -dl, -dr)

instance EqStandardizable LinearFractionalTransformation where
    nonstd_eq lhs rhs = _unLFT lhs == _unLFT rhs
instance Semigroup LinearFractionalTransformation where
    (<>) = mappend
instance Monoid LinearFractionalTransformation where
    mempty = LinearFractionalTransformation
        {up_left=1, up_right=0, down_left=0, down_right=1}

    mappend
        LinearFractionalTransformation
            {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
        LinearFractionalTransformation
            {up_left=ul', up_right=ur', down_left=dl', down_right=dr'}
        = LinearFractionalTransformation
            {up_left  =ul*ul' + ur*dl', up_right  =ul*ur' + ur*dr'
            ,down_left=dl*ul' + dr*dl', down_right=dl*ur' + dr*dr'
            }


data RadixBases4Convert
    = RadixBases4Convert
        {from_radix_base :: Integer
        ,to_radix_base :: Integer
        }
        deriving (Read, Show)
data FloatPartRadixBaseConvertorState
    = FloatPartRadixBaseConvertorState
        {radix_bases4convert :: RadixBases4Convert
        ,outer_mul_number :: Rational
        ,inner_add_number :: Rational
        }
        deriving (Read, Show)

instance Standardizable FloatPartRadixBaseConvertorState where
    std = id
instance StreamingAlgorithm FloatPartRadixBaseConvertorState where
    {-
    float_point_number :: (radix_base, [digit])
        0 <= digit < radix_base
        to_float_point_number radix_base digits
            = 1/radix_base * (digits[0] + 1/radix_base * (...))
            = II matrix[1/radix_base, digits[i]/radix_base; 0, 1] {i <- 0}

        [how (radix_base, radix_base', digits) -> digits']?
            [to_float_point_number radix_base digits == to_float_point_number radix_base' digits']
            to_float_point_number radix_base digits
            = 1/radix_base * (digits[0] + 1/radix_base * (...))
            = 1/radix_base' * (digits'[0] + 1/radix_base' * (...))

            # streaming
            # let remain[i] = to_float_point_number radix_base digits[i:]
            #   remain[i] = 1/radix_base * (digits[i] + remain[i+1])
            # let tail[j,i] = u[j,i]*(v[j,i] + remain[i])
            # let head[j](tail) = 1/radix_base' * (digits'[0] + 1/radix_base' * (...(digits'[j] + tail)))
            = head[j](tail[j,i])

            # consume; not output; consume first
            = head[j](tail[j,i+1])
                #tail[j,i] == tail[j,i+1]
            # poll; 1 more output; not consume input
            = head[j+1](tail[j+1,i])
                #tail[j,i]*radix_base' == digits'[j+1] + tail[j+1,i]
                #                           floor       float_part

            # init
            = head[-1](tail[-1,0])
            ==>>
                u[-1,0] == 1
                v[-1,0] == 0

            ==>>
                [@j,i: tail[j,i] <= 1]
                # NOTE: [0.9999... == 1]
            ==>>
                * poll
                    j' = j+1
                    i' = i
                    digits'[j+1] = floor(tail[j,i]*radix_base')
                    tail[j,i] = u[j,i]*(v[j,i] + remain[i])
                    0 <= remain[i] <= 1
                    # we donot know tail[j,i], but we know its range:
                    u[j,i]*v[j,i] <= tail[j,i] <= u[j,i]*(v[j,i]+1)
                    lower_bound = u[j,i]*v[j,i]*radix_base'
                    upper_bound = u[j,i]*(v[j,i]+1)*radix_base'
                    digits'[j+1] <- [floor lower_bound .. floor upper_bound]
                * consume
                    j' = j
                    i' = i+1
                ???[poll or consume]???
                    consume first
                        if floor lower_bound == floor upper_bound:
                            #poll
                            D' = digits'[j+1] = floor lower_bound
                            tail[j,i]
                                = u[j,i]*(v[j,i] + remain[i])
                                = 1/radix_base'*(D' + u[j+1,i]*(v[j+1,i] + remain[i]))
                            # coeff of remain[i]
                            u[j,i] = 1/radix_base'*u[j+1,i]
                            u[j+1,i] = u[j,i]*radix_base'
                            # not coeff of remain[i]
                            u[j,i]*v[j,i]
                            = 1/radix_base'*(D' + u[j+1,i]*v[j+1,i])
                            u[j+1,i]*v[j,i] = D' + u[j+1,i]*v[j+1,i]
                            v[j+1,i] = v[j,i] - D'/u[j+1,i]

                            ==>>
                            D' = digits'[j+1] = floor lower_bound
                            u[j+1,i] = u[j,i]*radix_base'
                            v[j+1,i] = v[j,i] - D'/u[j+1,i]
                        else:
                            #consume
                            tail[j,i] = u[j,i]*(v[j,i] + remain[i])
                            = tail[j,i+1] = u[j,i+1]*(v[j,i+1] + remain[i+1])
                            remain[i] = 1/radix_base * (digits[i] + remain[i+1])
                            D = digits[i]
                            # coeff of remain[i+1]
                            u[j,i]*1/radix_base = u[j,i+1]
                            u[j,i+1] = u[j,i]/radix_base
                            # not coeff of remain[i+1]
                            u[j,i]*(v[j,i]+1/radix_base * D) = u[j,i+1]*v[j,i+1]
                            u[j,i]*v[j,i]+ u[j,i+1]*D = u[j,i+1]*v[j,i+1]
                            v[j,i+1] = u[j,i]*v[j,i]/u[j,i+1] + D
                            v[j,i+1] = radix_base*v[j,i] + D

                            ==>>
                            D = digits[i]
                            u[j,i+1] = u[j,i]/radix_base
                            v[j,i+1] = v[j,i]*radix_base + D

    -}

    type OutputType4StreamingAlgorithm FloatPartRadixBaseConvertorState = Integer
    type InputType4StreamingAlgorithm FloatPartRadixBaseConvertorState = Integer

    -- maybe_poll :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    maybe_poll
        FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =bases@RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
            ,outer_mul_number=u
            ,inner_add_number=v
            }
        = if ok then Just (state', d') else Nothing
        where
            baseO_r = toRational baseO
            lower_bound = u*v*baseO_r
            upper_bound = lower_bound + u*baseO_r
            lower_digit, upper_digit :: Integer
            lower_digit = floor lower_bound
            upper_digit = floor upper_bound
            ok = lower_digit == upper_digit

            -- if ok, poll
            -- poll
            {-
            D' = digits'[j+1] = floor lower_bound
            u[j+1,i] = u[j,i]*radix_base'
            v[j+1,i] = v[j,i] - D'/u[j+1,i]
            -}
            d' = lower_digit
            u' = u*baseO_r
            v' = v - (toRational d')/u'
            state' = FloatPartRadixBaseConvertorState
                {radix_bases4convert=bases
                ,outer_mul_number=u'
                ,inner_add_number=v'
                }


    -- update_after_consume :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume
        FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =bases@RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
            ,outer_mul_number=u
            ,inner_add_number=v
            }
        input_digit
        = state'
        where
            baseI_r = toRational baseI
            -- consume
            {-
            D = digits[i]
            u[j,i+1] = u[j,i]/radix_base
            v[j,i+1] = v[j,i]*radix_base + D
            -}
            d = input_digit
            u' = u/baseI_r
            v' = v*baseI_r + (toRational d)
            state' = FloatPartRadixBaseConvertorState
                {radix_bases4convert=bases
                ,outer_mul_number=u'
                ,inner_add_number=v'
                }

-- ----------------------------------
finite_float_part_digits2rational :: Integer -> [Integer] -> Rational
finite_float_part_digits2rational baseI input_float_part_digits
    = output_rational
    where
        output_rational = f input_float_part_digits
        baseI_r = toRational baseI
        f (h:ts) = (toRational h + f ts) / baseI_r
        f [] = 0


data RadixBaseFloatPartNumber
    = RadixBaseFloatPartNumber
        {radix_base :: Integer
        ,float_part_digits :: [Integer]
            -- maybe infinite
        }
        deriving (Read, Show)

unRadixBaseFloatPartNumber :: RadixBaseFloatPartNumber -> (Integer, [Integer])
mkRadixBaseFloatPartNumber :: Integer -> [Integer] -> RadixBaseFloatPartNumber
finite_maybe_mkRadixBaseFloatPartNumber :: Integer -> [Integer] -> Maybe RadixBaseFloatPartNumber

unRadixBaseFloatPartNumber
    RadixBaseFloatPartNumber
        {radix_base=radix_base
        ,float_part_digits=float_part_digits
        }
    = (radix_base, float_part_digits)

finite_maybe_mkRadixBaseFloatPartNumber radix_base float_part_digits
    = if radix_base >= 2 && all is_ok float_part_digits
    then return $ RadixBaseFloatPartNumber
        {radix_base = radix_base
        ,float_part_digits = float_part_digits
        }
    else Nothing
    where
        is_ok x = (0<=x && x <radix_base)

mkRadixBaseFloatPartNumber radix_base float_part_digits
    = RadixBaseFloatPartNumber
        {radix_base = radix_base'
        ,float_part_digits = float_part_digits'
        }
    where
        radix_base' = assert (radix_base >= 2) radix_base
        float_part_digits' = do
            -- maybe infinite
            x <- float_part_digits
            return $ assert (0<=x && x <radix_base') x

finite_float_part_number2rational :: RadixBaseFloatPartNumber -> Rational
float_part_number_convertor :: RadixBaseFloatPartNumber -> Integer -> [Integer]

finite_float_part_number2rational
    RadixBaseFloatPartNumber
        {radix_base=radix_base
        ,float_part_digits=float_part_digits
        }
    = finite_float_part_digits2rational radix_base float_part_digits

float_part_number_convertor
    RadixBaseFloatPartNumber
        {radix_base=baseI
        ,float_part_digits=float_part_digits
        }
    baseO
    = float_part_digits_convertor (baseI, float_part_digits) baseO


float_part_digits_convertor :: (Integer, [Integer]) -> Integer -> [Integer]
float_part_digits_convertor (baseI, input_float_part_digits) baseO
    = output_float_part_digits
    where
        state0 = FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
                {-
                u[-1,0] == 1
                v[-1,0] == 0
                -}
            ,outer_mul_number=1
            ,inner_add_number=0
            }
        output_float_part_digits = streaming state0 input_float_part_digits

e_base3 = [1,0,0,2,2,1,0,1,1,2]
e_base7 = [2,4,0,1,1,6,4,3,5,2]
main1__radix_base_convert :: IO ()
main1__radix_base_convert = do
    print "e_base3 -> e_base7"
    print e_base7
    print $ float_part_digits_convertor (3, e_base3) 7
    print $ float_part_number_convertor (mkRadixBaseFloatPartNumber 3 e_base3) 7

    print "e_base7 -> e_base3"
    print e_base3
    print $ float_part_digits_convertor (7, e_base7) 3
    print $ float_part_number_convertor (mkRadixBaseFloatPartNumber 7 e_base7) 3

-- ----------------------------




newtype Label label a = Label a
    deriving (Show, Read)
unLabel :: forall label a. Label label a -> a
unLabel (Label a) = a
mkLabel_ :: forall label a. a -> Label label a
-- mkLabel_ a = Label @label a
mkLabel_ a = (Label a :: Label label a)
change_label :: Label label a -> Label label' a
change_label (Label a) = Label a
change_label_ :: forall label' label a. Label label a -> Label label' a
change_label_ (Label a) = mkLabel_ @label' a
instance Functor (Label label) where
    fmap f (Label a) = Label (f a)




class StreamingAlgorithm state => ConstantStreamingAlgorithm state where
    the_initial_state :: state
    the_labelled_constant_inputs :: Label state [InputType4StreamingAlgorithm state]

the_constant_inputs_
    :: forall state. ConstantStreamingAlgorithm state
    => [InputType4StreamingAlgorithm state]
the_constant_outputs_
    :: forall state. ConstantStreamingAlgorithm state
    => [OutputType4StreamingAlgorithm state]
the_constant_inputs_ = unLabel $ the_labelled_constant_inputs @state
the_constant_outputs_ = unLabel $ the_labelled_constant_outputs @state

the_labelled_constant_outputs
    :: forall state. ConstantStreamingAlgorithm state
    => Label state [OutputType4StreamingAlgorithm state]
the_labelled_constant_outputs = Label constant_outputs
    where
        initial_state = (the_initial_state
            :: forall. state)
        Label constant_inputs = (the_labelled_constant_inputs
            :: forall. Label state [InputType4StreamingAlgorithm state])
        constant_outputs = (streaming initial_state constant_inputs
            :: forall. [OutputType4StreamingAlgorithm state])





-- type family Callable4ConstantStreamingAlgorithm :: * -> *
type Number4ConstantStreamingAlgorithm algorithm_configure
    = Type4PartialTransform (Callable4ConstantStreamingAlgorithm algorithm_configure)

type Number4Generator4ConstantStreamingAlgorithm generate_algorithm
    = Number4ConstantStreamingAlgorithm (Configure4Generator4ConstantStreamingAlgorithm generate_algorithm)
type InputCallable4ConstantStreamingAlgorithm generate_algorithm
    = Callable4ConstantStreamingAlgorithm (Configure4Generator4ConstantStreamingAlgorithm generate_algorithm)

type Number4FloorOutput4ConstantStreamingAlgorithm output_algorithm
    = Number4ConstantStreamingAlgorithm (Configure4FloorOutput4ConstantStreamingAlgorithm output_algorithm)
type OutputCallable4ConstantStreamingAlgorithm output_algorithm
    = Callable4ConstantStreamingAlgorithm (Configure4FloorOutput4ConstantStreamingAlgorithm output_algorithm)


class (PartialTransform (Callable4ConstantStreamingAlgorithm algorithm_configure)
    ) => Configure4ConstantStreamingAlgorithm algorithm_configure where
    type Callable4ConstantStreamingAlgorithm algorithm_configure :: *
    -- type Number4ConstantStreamingAlgorithm algorithm_configure :: *

type Pair a = (a, a)
class (Configure4ConstantStreamingAlgorithm (Configure4Generator4ConstantStreamingAlgorithm generate_algorithm)
    ) => Generator4ConstantStreamingAlgorithm generate_algorithm where
    {-
        constant_number = II constant_input_funcs
        constant_number = LIMIT lower_bound i {i <- [0..]}
        all (\i -> lower_bound i <= constant_number <= upper_bound i) [0..]
        where
            lower_arg_numbers :: [number]
            upper_arg_numbers :: [number]
            initial_func :: func
            constant_input_funcs :: [func]
            parital_func i = foldr (<>) initial_func $ take i constant_input_funcs
            lower_bound i = call (parital_func i) (index i lower_arg_numbers)
            upper_bound i = call (parital_func i) (index i upper_arg_numbers)
    -}
    type Configure4Generator4ConstantStreamingAlgorithm generate_algorithm :: *
    the_initial_basic_state :: BasicState4ConstantStreamingAlgorithm generate_algorithm
    the_constant_input_basic_states :: [BasicState4ConstantStreamingAlgorithm generate_algorithm]


class FloorOutput4ConstantStreamingAlgorithm output_algorithm where
    {-
        constant_number = II constant_output_funcs
        but constant_output_funcs is unknown
        we assume that constant_output_funcs[i] depends on floor of (parital_func i)

        let output_digit2inv_output_func :: Integer -> output_func

        II constant_input_funcs == II constant_output_funcs
        state_func * II constant_input_funcs[i:] == II constant_output_funcs[j:]
        if floor(state_func(lower_arg_numbers[i])) == floor(state_func(upper_arg_numbers[i])):
            output_digit = floor(state_func(lower_arg_numbers[i]))
            constant_output_funcs[j]^(-1) = output_digit2inv_output_func output_digit
            state_func' = constant_output_funcs[j]^(-1) * state_func
            i' = i
            j' = j+1
        else:
            state_func' = state_func*constant_output_funcs[i]
            i' = i+1
            j' = j

    -}
    type Configure4FloorOutput4ConstantStreamingAlgorithm output_algorithm :: *
    the_labelled_output_digit2inv_output_func :: Label output_algorithm
        (Integer -> OutputCallable4ConstantStreamingAlgorithm output_algorithm)
the_labelled_output_digit2inv_output_func_
    :: forall output_algorithm.
    (FloorOutput4ConstantStreamingAlgorithm output_algorithm)
    => (Integer -> OutputCallable4ConstantStreamingAlgorithm output_algorithm)
the_labelled_output_digit2inv_output_func_
    = unLabel $ (the_labelled_output_digit2inv_output_func
        :: Label output_algorithm (Integer -> OutputCallable4ConstantStreamingAlgorithm output_algorithm))









data BasicState4ConstantStreamingAlgorithm generate_algorithm
    = BasicState4ConstantStreamingAlgorithm
        -- func (lower_arg_number, upper_arg_number)
        (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
        (Pair(Number4Generator4ConstantStreamingAlgorithm generate_algorithm))
    -- deriving (Show, Read)
newtype State4ConstantStreamingAlgorithm generate_algorithm output_algorithm
    = State4ConstantStreamingAlgorithm (BasicState4ConstantStreamingAlgorithm generate_algorithm)
    -- deriving (Show, Read)

instance
    (Standardizable (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
    ) => Standardizable (BasicState4ConstantStreamingAlgorithm generate_algorithm) where
    std (BasicState4ConstantStreamingAlgorithm func arg_pair)
        = BasicState4ConstantStreamingAlgorithm (std func) arg_pair
deriving instance
    (Standardizable (BasicState4ConstantStreamingAlgorithm generate_algorithm)
    ) => Standardizable (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm)



deriving instance
    (Show (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
    ,Show (Number4Generator4ConstantStreamingAlgorithm generate_algorithm)
    ) => Show (BasicState4ConstantStreamingAlgorithm generate_algorithm)
deriving instance
    (Read (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
    ,Read (Number4Generator4ConstantStreamingAlgorithm generate_algorithm)
    ) => Read (BasicState4ConstantStreamingAlgorithm generate_algorithm)

deriving instance
    (Show (BasicState4ConstantStreamingAlgorithm generate_algorithm)
    ) => Show (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm)
deriving instance
    (Read (BasicState4ConstantStreamingAlgorithm generate_algorithm)
    ) => Read (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm)


instance
    (Generator4ConstantStreamingAlgorithm generate_algorithm
    ,FloorOutput4ConstantStreamingAlgorithm output_algorithm
    ,Standardizable (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
    ,InputCallable4ConstantStreamingAlgorithm generate_algorithm
        ~ OutputCallable4ConstantStreamingAlgorithm output_algorithm
    , Rational
        ~ Number4Generator4ConstantStreamingAlgorithm generate_algorithm
    , Rational
        ~ Number4FloorOutput4ConstantStreamingAlgorithm output_algorithm
    -- ,Configure4Generator4ConstantStreamingAlgorithm generate_algorithm
    -- ~ Configure4FloorOutput4ConstantStreamingAlgorithm output_algorithm
    ) => StreamingAlgorithm (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm) where
    type OutputType4StreamingAlgorithm
        (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm)
        = Integer
    type InputType4StreamingAlgorithm
        (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm)
        = State4ConstantStreamingAlgorithm generate_algorithm output_algorithm

    -- :: state -> Maybe (state, OutputType4StreamingAlgorithm state)

    maybe_poll (State4ConstantStreamingAlgorithm(BasicState4ConstantStreamingAlgorithm
                func
                arg_pair@(lower_arg_number, upper_arg_number)
      )) = do
        lower_bound <- partial_transform func lower_arg_number
        upper_bound <- partial_transform func upper_arg_number
        let lower_digit = floor lower_bound
            upper_digit = floor upper_bound
            ok = lower_digit == upper_digit
            -- if ok
            output_digit = lower_digit
            inv_output_func = the_labelled_output_digit2inv_output_func_ @output_algorithm output_digit
            func' = inv_output_func <> func
            state' = State4ConstantStreamingAlgorithm (BasicState4ConstantStreamingAlgorithm func' arg_pair)
        if ok then Just (state', output_digit) else Nothing

    -- :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume
        state@(State4ConstantStreamingAlgorithm (BasicState4ConstantStreamingAlgorithm state_func _))
        next_input@(State4ConstantStreamingAlgorithm (BasicState4ConstantStreamingAlgorithm next_input_func arg_pair))
        = State4ConstantStreamingAlgorithm (BasicState4ConstantStreamingAlgorithm
            (state_func <> next_input_func)
            arg_pair
            )


instance
    (Generator4ConstantStreamingAlgorithm generate_algorithm
    ,FloorOutput4ConstantStreamingAlgorithm output_algorithm
    ,Standardizable (InputCallable4ConstantStreamingAlgorithm generate_algorithm)
    ,InputCallable4ConstantStreamingAlgorithm generate_algorithm
        ~ OutputCallable4ConstantStreamingAlgorithm output_algorithm
    , Rational
        ~ Number4Generator4ConstantStreamingAlgorithm generate_algorithm
    , Rational
        ~ Number4FloorOutput4ConstantStreamingAlgorithm output_algorithm
    ) => ConstantStreamingAlgorithm (State4ConstantStreamingAlgorithm generate_algorithm output_algorithm) where
    {-
  from:
    the_initial_basic_state :: BasicState4ConstantStreamingAlgorithm generate_algorithm
    the_constant_input_basic_states :: [BasicState4ConstantStreamingAlgorithm generate_algorithm]
  to:
    the_initial_state :: state
    the_labelled_constant_inputs :: Label state [InputType4StreamingAlgorithm state]
    -}

    the_initial_state = State4ConstantStreamingAlgorithm the_initial_basic_state
    the_labelled_constant_inputs = Label $ map State4ConstantStreamingAlgorithm the_constant_input_basic_states





_subtract_then_lshift :: Integer -> Integer -> LinearFractionalTransformation
    {-
        assume
            remain = digit + remain_
            remain' = radix_base*remain_
        digit :: Integer
        remain_, remain' :: Rational
        0 <= digit < radix_base
        0 <= remain_ < 1
        0 <= remain' < radix_base
        digit = floor remain
        remain' = radix_base*(remain - floor remain)
            = radix_base*remain + (-radix_base*digit)

        ==>> matrix[radix_base, -radix_base*digit; 0, 1]
    -}
_subtract_then_lshift radix_base digit =
        LinearFractionalTransformation
        {up_left = radix_base
        ,up_right = -radix_base*digit
        ,down_left = 0
        ,down_right = 1
        }
_subtract_then_inverse :: Integer -> LinearFractionalTransformation
    {-
        assume
            remain = digit + remain_
            remain' = 1/remain_
        digit :: Integer
        remain_, remain' :: Rational
        1 <= digit < +oo
        0 < remain_ < 1
        1 < remain' < +oo
        digit = floor remain
        remain' = 1/(remain - floor remain)
            = (0*remain + 1)/(1*remain + (-digit))

        ==>> matrix[0, 1; 1, -digit]
        fact: matrix[0, 1; 1, -digit]*matrix[digit, 1; 1,0] == I
    -}
_subtract_then_inverse digit =
        LinearFractionalTransformation
        {up_left = 0
        ,up_right = 1
        ,down_left = 1
        ,down_right = -digit
        }




data Configure4LinearFractionalTransformation

instance Configure4ConstantStreamingAlgorithm Configure4LinearFractionalTransformation where
    type Callable4ConstantStreamingAlgorithm Configure4LinearFractionalTransformation = LinearFractionalTransformation


data FloorOutput__continued_fraction
data FloorOutput__base10
data FloorOutput__base16
data FloorOutput__base2
data FloorOutput__base3
data FloorOutput__base7

instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__continued_fraction where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__continued_fraction = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label _subtract_then_inverse
instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__base10 where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__base10 = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label (_subtract_then_lshift 10)
instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__base16 where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__base16 = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label (_subtract_then_lshift 16)
instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__base2 where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__base2 = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label (_subtract_then_lshift 2)
instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__base3 where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__base3 = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label (_subtract_then_lshift 3)
instance FloorOutput4ConstantStreamingAlgorithm FloorOutput__base7 where
    type Configure4FloorOutput4ConstantStreamingAlgorithm FloorOutput__base7 = Configure4LinearFractionalTransformation
    the_labelled_output_digit2inv_output_func
        = Label (_subtract_then_lshift 7)


data Generator4Pi__Rabinowitz_and_Wagon
data Generator4Pi__Lambert
data Generator4Pi__Gosper
type State4Pi_base10__Rabinowitz_and_Wagon
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Rabinowitz_and_Wagon
        FloorOutput__base10
type State4Pi_base10__Lambert
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Lambert
        FloorOutput__base10
type State4Pi_base10__Gosper
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Gosper
        FloorOutput__base10

type State4Pi_continued_fraction__Rabinowitz_and_Wagon
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Rabinowitz_and_Wagon
        FloorOutput__continued_fraction
type State4Pi_continued_fraction__Lambert
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Lambert
        FloorOutput__continued_fraction
type State4Pi_continued_fraction__Gosper
    = State4ConstantStreamingAlgorithm
        Generator4Pi__Gosper
        FloorOutput__continued_fraction



instance Generator4ConstantStreamingAlgorithm Generator4Pi__Rabinowitz_and_Wagon where
    -- Rabinowitz_and_Wagon
    {-
    # Rabinowitz_and_Wagon_spigot
    pi = 2 + 1/3*(2 + 2/5*(2 + 3/7*(2 + ...)))
        = (2 + 1/3*) (2 + 2/5*) (2 + 3/7*) ...
        = II (2 + k/(2*k+1)*) {k <- 1..}
        = II matrix[k, 4*k+2; 0, 2*k+1] {k <- 1..}
        #pi === 1*Rabinowitz_and_Wagon_spigot(1)
        #Rabinowitz_and_Wagon_spigot(k) <- range[3,4]
        fact: st(3) <= digit <= st(3)
    -}
    type Configure4Generator4ConstantStreamingAlgorithm Generator4Pi__Rabinowitz_and_Wagon = Configure4LinearFractionalTransformation
    the_initial_basic_state
        = BasicState4ConstantStreamingAlgorithm mempty (3, 4)
    the_constant_input_basic_states =
        [BasicState4ConstantStreamingAlgorithm mx (3,4)
        | k <- [1..]
        , let dr = 2*k+1
        , let mx = LinearFractionalTransformation
                {up_left=k, up_right=2*dr, down_left=0, down_right=dr}
        ]

_mk_arg_pair__Lambert :: Rational -> Pair Rational
_mk_arg_pair__Lambert k = (offset, offset+k/2)
    where offset = 2*k-1
instance Generator4ConstantStreamingAlgorithm Generator4Pi__Lambert where
    -- Lambert
    {-
    # Lambert_expression
    pi = 4/(1+1^2/(3+2^2/(5+3^2/(7+...))))
        = 4/( (1+1^2/) (3+2^2/) (5+3^2/) ... )
        = 4 / II (2*k-1 + k^2/) {k <- 1...}
        = matrix[0, 4; 1, 0] * II matrix[2*k-1, k^2; 1, 0] {k <- 1..}
        #pi === 4/Lambert_expression(1)
        #Lambert_expression(k) <- range[2*k-1, 2*k-1+k/2]
        fact: st(2*k-1) <= digit <= st(2*k-1+k/2)
    -}

    type Configure4Generator4ConstantStreamingAlgorithm Generator4Pi__Lambert = Configure4LinearFractionalTransformation
    the_initial_basic_state
        = BasicState4ConstantStreamingAlgorithm mx arg_pair
        where
            mx = LinearFractionalTransformation
                {up_left=0, up_right=4, down_left=1, down_right=0}
            arg_pair = _mk_arg_pair__Lambert 1

    the_constant_input_basic_states =
        [BasicState4ConstantStreamingAlgorithm mx arg_pair
        | k <- [1..]
        , let mx = LinearFractionalTransformation
                {up_left=2*k-1, up_right=k^2, down_left=1, down_right=0}
        , let arg_pair = _mk_arg_pair__Lambert (toRational $ k+1)
        ]



_27_5 = toRational 27 / 5
_12_5 = toRational 12 / 5
_6_5_3 = (toRational 6 / 5)^3
_mk_arg_pair__Gosper :: Rational -> Pair Rational
_mk_arg_pair__Gosper k = (_27_5*k-_12_5, _27_5*k-_6_5_3)
        -- 27/5 * k - 12/5
        -- 27/5 * k - (6/5)^3
instance Generator4ConstantStreamingAlgorithm Generator4Pi__Gosper where
    -- Gosper
    {-
    # Gosper_series
    pi = 3 + (1*1)/(3*4*5) * (8 + (2*3)/(3*7*8) * (...(5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) * (...)))
        = (3 + (1*1)/(3*4*5) *) (8 + (2*3)/(3*7*8) *) ... ((5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) *) ...
        = II ((5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) *) {k <- 1..}
        = II matrix[(k*(2*k-1), 3*(3*k+1)*(3*k+2)*(5*k-2); 0, 3*(3*k+1)*(3*k+2)] {k <- 1..}
        #pi === 1*Gosper_series(1)
        #Gosper_series(k) <- [27/5 * k - 12/5, 27/5 * k - (6/5)^3]
        fact: st(27/5 * k - 12/5) <= digit <= st(27/5 * k - (6/5)^3)
    -}

    type Configure4Generator4ConstantStreamingAlgorithm Generator4Pi__Gosper = Configure4LinearFractionalTransformation
    the_initial_basic_state
        = BasicState4ConstantStreamingAlgorithm mx arg_pair
        where
            mx = mempty
            arg_pair = _mk_arg_pair__Gosper 1

    the_constant_input_basic_states =
        [BasicState4ConstantStreamingAlgorithm mx arg_pair
        | k <- [1..]
        , let kkk = 3*(3*k+1)*(3*k+2)
        , let mx = LinearFractionalTransformation
                    {up_left=k*(2*k-1), up_right=kkk*(5*k-2)
                    ,down_left=0, down_right=kkk
                    }
        , let arg_pair = _mk_arg_pair__Gosper (toRational $ k+1)
        ]










the_digits_of_pi_continued_fraction__from_A001203 = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1]
the_digits_of_pi_base10__from_A000796 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9, 8, 2, 1, 4]

main2__show_all_pi :: IO ()
main2__show_all_pi = do
    print "the_digits_of_pi_base10__from_A000796"
    print the_digits_of_pi_base10__from_A000796
    print "decimal digits of pi Rabinowitz_and_Wagon"
    print $ take 100 the_digits_of_pi_base10__Rabinowitz_and_Wagon
    print "decimal digits of pi Lambert"
    print $ take 100 the_digits_of_pi_base10__Lambert
    print "decimal digits of pi Gosper"
    print $ take 100 the_digits_of_pi_base10__Gosper

    print ""
    print "the_digits_of_pi_continued_fraction__from_A001203"
    print the_digits_of_pi_continued_fraction__from_A001203
    print "continued_fraction digits of pi Rabinowitz_and_Wagon"
    print $ take 10 the_digits_of_pi_continued_fraction__Rabinowitz_and_Wagon
    print "continued_fraction digits of pi Lambert"
    print $ take 10 the_digits_of_pi_continued_fraction__Lambert
    print "continued_fraction digits of pi Gosper"
    print $ take 10 the_digits_of_pi_continued_fraction__Gosper

the_digits_of_pi_base10__Rabinowitz_and_Wagon
    = the_constant_outputs_ @State4Pi_base10__Rabinowitz_and_Wagon
the_digits_of_pi_base10__Lambert
    = the_constant_outputs_ @State4Pi_base10__Lambert
the_digits_of_pi_base10__Gosper
    = the_constant_outputs_ @State4Pi_base10__Gosper

the_digits_of_pi_continued_fraction__Rabinowitz_and_Wagon
    = the_constant_outputs_ @State4Pi_continued_fraction__Rabinowitz_and_Wagon
the_digits_of_pi_continued_fraction__Lambert
    = the_constant_outputs_ @State4Pi_continued_fraction__Lambert
the_digits_of_pi_continued_fraction__Gosper
    = the_constant_outputs_ @State4Pi_continued_fraction__Gosper




























-- -------------------------------
main :: IO ()
main = main_fastest_cf

main_fastest_cf :: IO ()
main_fastest_cf = do
    let constant_outputs_cf_G = the_digits_of_pi_continued_fraction__Gosper
        pairs = zip [0..] constant_outputs_cf_G
    print "the_digits_of_pi_continued_fraction__Gosper"
    forM_ pairs print

main_all :: IO ()
main_all = do
    main1__radix_base_convert
    main2__show_all_pi
    main3__test_all_pi_base10
    main4__test_all_pi_cf

main3__test_all_pi_base10 :: IO ()
main3__test_all_pi_base10 = do
    let constant_outputs_RW = the_digits_of_pi_base10__Rabinowitz_and_Wagon
        constant_outputs_L = the_digits_of_pi_base10__Lambert
        constant_outputs_G = the_digits_of_pi_base10__Gosper
        cmp constant_outputs = take (length the_digits_of_pi_base10__from_A000796) constant_outputs == the_digits_of_pi_base10__from_A000796
    let tuple4s = zip4 [0..] constant_outputs_RW constant_outputs_L constant_outputs_G
        -- triples = zip3 constant_outputs_RW constant_outputs_L constant_outputs_G

    {-
    print "guard True"
    guard True
    print "guard False"
    guard False
    -}
    guard (cmp constant_outputs_RW)
    guard (cmp constant_outputs_L)
    guard (cmp constant_outputs_G)

    forM_ tuple4s $ \tuple4@(i, a, b, c) -> do
        -- unless (a == b && b == c) $ print tuple4
        -- if (a == b && b == c) then print i else print tuple4
        --
        -- guard (a == b && b == c)
        -- print i
        --
        if (a == b && b == c) then print (i, a) else do
            print tuple4
            mzero


main4__test_all_pi_cf :: IO ()
main4__test_all_pi_cf = do
    let constant_outputs_RW = the_digits_of_pi_continued_fraction__Rabinowitz_and_Wagon
        constant_outputs_L = the_digits_of_pi_continued_fraction__Lambert
        constant_outputs_G = the_digits_of_pi_continued_fraction__Gosper
        cmp constant_outputs = take (length the_digits_of_pi_continued_fraction__from_A001203) constant_outputs == the_digits_of_pi_continued_fraction__from_A001203
    let tuple4s = zip4 [0..] constant_outputs_RW constant_outputs_L constant_outputs_G

    guard (cmp constant_outputs_RW)
    guard (cmp constant_outputs_L)
    guard (cmp constant_outputs_G)

    forM_ tuple4s $ \tuple4@(i, a, b, c) -> do
        if (a == b && b == c) then print (i, a) else do
            print tuple4
            mzero




-- -------------------------------


