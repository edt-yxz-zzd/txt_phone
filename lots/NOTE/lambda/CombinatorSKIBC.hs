
{-

combinators

    r'''
T[x] => x
T[(f e)] => (T[f] T[e])
T[\x->e] => (K T[e]) (if x is not free in e)
T[\x->x] => I
T[\x->\y->e] => T[\x->T[\y->e]] (if x is free in e)
+ eta-reduction: T[\x->(f x)] = T[f] (if x is not free in f)
    <==> B I e == e; B e I == e
    B is composition, i.e. (.)
    C is flip
T[\x->(f e)] => (S T[\x->f] T[\x->e]) (if x is free in both f and e)
T[\x->(f e)] => (C T[\x->f] T[e]) (if x is free in f but not e)
T[\x->(f e)] => (B T[f] T[\x->e]) (if x is free in e but not f)
'''



-}

module Lambda.CombinatorSKIBC where
import Lambda.UntypedLambdaTerm
    ( Term(..), TermWO(..), FV
    , untyped_lambda_term_parse, is_closed_term
    , left_most_eval_lambda_term
    , left_most_eval_lambda_termIO
    , mkApp, mkVal, mkAbs
    , show_lambda
    , lambdaI, lambdaS, lambdaK, lambdaB, lambdaC
    , str_const, str_K
    , str_flip, str_C
    , str_composition, str_B
    , str_I, str_S
    , str_app
    )
import Lambda.OpFreshID hiding (ID)
import qualified Data.Set as S
import Data.List (foldl1')
type ID = IDEX

data CombinatorPrimitive = S | K | I | B | C
    deriving (Read, Show)
data Combinator
    = P CombinatorPrimitive
    | AppC Combinator Combinator
    deriving (Read, Show)
data TermNoAbs id
    = TP CombinatorPrimitive
    | TermNoAbs (FV id) (TermNoAbsWO id)
    deriving (Read, Show)
data TermNoAbsWO id = TValC id | TAppC (TermNoAbs id) (TermNoAbs id)
    deriving (Read, Show)
show_combinator :: Combinator -> String
show_combinator = f False where
    f b (AppC c1 c2)= s where
        s1 = f False c1
        s2 = f True c2
        s = if b then '(' : s1 ++ ' ' : s2 ++ ")" else s1 ++ ' ' : s2
    f _ (P t) = show t
eval_combinator :: Combinator -> Combinator
eval_combinator = ff where
    ff (AppC c1 c2) = r where
        a1 = ff c1
        a2 = ff c2
        c = case a1 of
            -- primitive reduce
            -- I x = x
            -- S f g x = (f x) (g x)
            -- K a b = a
            -- B f g x = f (g x)
            -- C f g x = (f x) g
            (P I) -> a2
            AppC (P K) a1' -> a1'
            AppC (P S) f `AppC` g -> ff $ AppC (AppC f a2) (AppC g a2)
            --AppC (P S) (P K) `AppC` _ -> a2
            --AppC (P S) (AppC (P K) f) `AppC` AppC (P K) a -> AppC f a
            AppC (P B) f `AppC` g -> ff $ AppC f (AppC g a2)
            AppC (P C) f `AppC` g -> ff $ AppC (AppC f a2) g
            _ -> AppC a1 a2
        r = case c of
            -- eta-reduce - with \x. E x = E where x not in FV(E)
            -- B I = I
            -- B x I = x
            -- S K = K I
            -- C K = K I        -- = \_x y -> y
            -- -- B K           = \x y _z -> x y
            -- -- B (K a)       = \_x _y z -> a z
            -- B (S x) K = C x  -- = B (S x) K y = S x (K y) = C x y
            -- C B I = I
            -- C (B B x) I = x
            -- S (K a) (K b) = K (a b)
            -- S (K a) b = B a b
            -- S a (K b) = C a b
            -- C (K a) b = K (a b)
            -- B a (K b) = K (a b)
            AppC (P B) (P I) -> P I
            AppC (P B) x `AppC` P I -> x
            AppC (P S) (P K) -> AppC (P K) (P I)
            AppC (P C) (P K) -> AppC (P K) (P I)
            AppC (P B) (P S `AppC` x) `AppC` P K -> AppC (P C) x

            AppC (P C) (P B) `AppC` P I -> P I
            (P C `AppC` AppC (P B `AppC` P B) x) `AppC` P I -> x
            (P S `AppC` AppC (P K) a) `AppC` AppC (P K) b -> ff $ P K `AppC` AppC a b
            (P S `AppC` AppC (P K) a) `AppC` b -> ff $ AppC (P B) a `AppC` b
            (P S `AppC` a) `AppC` AppC (P K) b -> ff $ AppC (P C) a `AppC` b
            (P C `AppC` AppC (P K) a) `AppC` b -> ff $ P K `AppC` AppC a b
            (P B `AppC` a) `AppC` AppC (P K) b -> ff $ P K `AppC` AppC a b
            _ -> c
    ff c = c

(<<<<<) :: a -> a -> a
(<<<<<) = const

infixl 8 <<<<<
infixl 8 `AppC`

_S0 = P S
_S1 = AppC _S0
_S2 = AppC . _S1
_K0 = P K
_K1 = AppC _K0
_I0 = P I
_B0 = P B
_B1 = AppC _B0
_B2 = AppC . _B1
_C0 = P C
_C1 = AppC _C0
_C2 = AppC . _C1
combinator2lambda :: OpFreshID id => Combinator -> Term id
combinator2lambda = f where
    f (AppC t1 t2) = mkApp (f t1) (f t2)
    f (P p) = g p where
        g I = lambdaI
        g S = lambdaS
        g K = lambdaK
        g B = lambdaB
        g C = lambdaC


lambda2combinator :: (Monad m, Ord id) => Term id -> m Combinator
lambda2combinator = f where
    f t = if is_closed_term t
            then term_no_abs2combinator $ remove_abs t
            else fail "lambda2combinator: input term is not closed"
term_no_abs2combinator :: Monad m => TermNoAbs id -> m Combinator
term_no_abs2combinator = f where
    f (TermNoAbs fv wo) =
        if S.null fv then wo2c wo else fail "FV /= { }"
    f (TP p) = return (P p)
    wo2c (TAppC t1 t2) = do
        t1' <- f t1
        t2' <- f t2
        return $ AppC t1' t2'


_TK, _TS :: TermNoAbs id
_TK = TP K
_TS = TP S
_TI = TP I


mkTValC :: id -> TermNoAbs id
mkTValC id = TermNoAbs (S.singleton id) (TValC id)
getFVC :: TermNoAbs id -> FV id
getFVC (TermNoAbs fv _) = fv
getFVC _ = S.empty
mkTAppC :: Ord id => TermNoAbs id -> TermNoAbs id -> TermNoAbs id
mkTAppC t1 t2 = TermNoAbs (fv1 `S.union` fv2) (TAppC t1 t2) where
    fv1 = getFVC t1
    fv2 = getFVC t2

{-
    remove_abs :: space O(n) -> O(f(n))
    sub :: 1 -> O(n) -> O(g(n))
    remove_abs
        Val :: 1 -> f 1
        App :: 1+n+m -> f n + f m <= f (1+n+m)
        Abs :: 1+n -> g (f n) <= f (1+n)
    sub
        TS :: 1 -> 1
        TK :: 1 -> 1
        TermNoAbs
            TValC :: 1 -> 1
            TAppC :: 1+n+m -> 3 + g n + g m <= g (1+n+m)
    ==>> g n = 3*n
    ==>> 3*(f n) <= f (1+n)
    ==>> f n = 3^n
    O(3^n)!!
    O(n^2)!!

    ------------

    size_L :: LambdaTerm -> Nat
    -- size_L t = numSub_L t + sum (numFVs_L t)
    size_L x = 2
    size_L (t1 t2) = 1 + size FV(t1 t2) + size_L t1 + size_L t2
    size_L (\x. t) = 1 + size FV(\x. t) + size_L t

    -- to find out min numSub_L, max size_L when size FV is 0
    size_L3 t = (numSub_L t, size FV(t), size_L t)
    size_L3 x = (1, 1, 2)
    size_L3 (\x.t) =
        let (n, f, s) = size_L3 t in
        if x in FV(t)
        then (n+1, f-1, f+s)
        else (n+1, f, 1+f+s)
    size_L3 (t1 t2) =
        let (n1, f1, s1) = size_L3 t1 in
        let (n2, f2, s2) = size_L3 t2 in
        let m = size (FV(t1) /-\ FV(t2)) in
        (n1+n2+1, f1+f2-m, 1+f1+f2-m+s) -- 0 <= m <= min(f1, f2)

    size_LX :: LambdaTerm -> (Nat, [Nat])
    size_LX t = (numSub_L t, numFVs_L t)
    -- numSub_L t = number of subterms of t
    -- numFVs_L t = all FVs of subterms of t
    numSub_L x = 1
    numSub_L (t1 t2) = 1 + numSub_L t1 + numSub_L t2
    numSub_L (\x. t) = 1 + numSub_L t
    numFVs_L x = [1] -- [size FV(x)]
    numFVs_L (t1 t2) = size FV(t1 t2) : numFVs_L t1 ++ numFVs_L t2
    numFVs_L (\x. t) = size FV(\x.t) : numFVs_L t


    Combinator  = I
                | K Combinator
                | S Combinator Combinator
                | B Combinator Combinator
                | C Combinator Combinator
                | A Combinator Combinator -- application
    -- size_C = node of CombinatorTerm
    size_C I = 1
    size_C (K c) = 1 + size_C c
    size_C (S/B/C/A c1 c2) = 1 + size_C c1 + size_C c2

    remove_abs
    f
        x -> x
            1 -> 1
        t1 t2 -> (f t1) `A` (f t2)
            1 A -> 1 A
        \x.t -> sub x (f t)
            1 x -> 0
            each LambdaTerm map into a CombinatorTerm
            except this one, the abstraction!!!
            CombinatorTerm has one lesser term
    sub x c
        x not in FV(c) -> K c
            0 -> 1 K
            each sub preserve numTerm
            except this one!
            CombinatorTerm has one more K!
            if this 'sub' call was the one in "\x.t -> sub x (f t)"
            then the removed x in LambdaTerm meet this K
            else this 'sub' call was from below "c1 c2 -> ..." where
                each 'sub' meet one FV
            ==>> size_C (remove_abs t) <= size_L t
        case c of
            x -> I
                1 x -> 1 I
            c1 c2 -> case (x in FV(c1), x in FV(c2)) of
                T, T -> S (sub x c1) (sub x c2)
                    1 A -> 1 S
                    -2 x in FVs
                F, T -> B         c1 (sub x c2)
                    1 A -> 1 B
                    -1 x in FVs
                T, F -> C (sub x c1) c2
                    1 A -> 1 C
                    -1 x in FVs

    ? [FV(t) == {}] ==>> [numSub_L t ~ size_L t]
    ? numSub_L t ~ size_L t
    1 ->
        x
        [1] -> 2
    2 ->
        \x. x
        [0,1] -> 3
        \x. y
        [1,1] -> 4
    3 ->
        \x.\x.x
        [0, ...] -> 4 -- 4 < 5 ; removed
        \y.\x.y
        [0, ...] -> 5
        \z.\x.y
        [1, ...] -> 6
        x x
        [1, ...] -> 6
        x y
        [2, ...] -> 7
    4 ->
        

-}
remove_abs :: Ord id => Term id -> TermNoAbs id
remove_abs (Term _ _ (Val id)) = mkTValC id
remove_abs (Term _ _ (App t1 t2)) = mkTAppC (remove_abs t1) (remove_abs t2)
remove_abs (Term _ _ (Abs id _t)) = sub id (remove_abs _t) where
    sub id t = case t of
        TermNoAbs fv wo -> sub_ id t fv wo
        p@(TP _) -> mkTAppC _TK p
    sub_ id t fv wo = if not $ id `S.member` fv then mkTAppC _TK t else
      case wo of
        TValC id' -> -- I
            -- assert id == id'
            if id == id' then _TI
                else error "ValueError: FV(\\x.y) == { }"
        TAppC t1 t2 ->
          let using = S.member id . getFVC
              -- f p = foldl1' mkTAppC [TP p, sub id t1, sub id t2]
          in  case (using t1, using t2) of
            (True, True) -> -- S
                foldl1' mkTAppC [TP S, sub id t1, sub id t2]
            (False, True) -> -- B
                foldl1' mkTAppC [TP B,        t1, sub id t2]
            (True, False) -> -- C
                foldl1' mkTAppC [TP C, sub id t1,        t2]
            (False, False) ->
                error "ValueError: FV(t s) /= FV(t) \\-/ FV(s)"



_parse :: Monad m => String -> m (Term ID, Combinator, Combinator, Term ID, Term ID)
_parse s = do
    let Right t = untyped_lambda_term_parse "<>" s
        Right c = lambda2combinator t
        c' = eval_combinator c
        v = left_most_eval_lambda_term $ combinator2lambda c
        v' = left_most_eval_lambda_term $ combinator2lambda c'
    return (t, c, c', v, v')
_parseIO :: String -> IO (Term ID, Combinator, Combinator, Term ID, Term ID)
_parseIO s = do
    let Right t = untyped_lambda_term_parse "<>" s
        Right c = lambda2combinator t
        c' = eval_combinator c
    v <- left_most_eval_lambda_termIO $ combinator2lambda c
    v' <- left_most_eval_lambda_termIO $ combinator2lambda c'
    return (t, c, c', v, v')
_parse_and_print :: String -> IO ()
_parse_and_print s = do
    --(t, c, c', v, v') <- _parseIO s
    --(t, c, c', v, v') <- _parse s
    (t, c, c', v, v') <- _parse s
    print $ show_lambda t
    print $ show_combinator c
    print $ show_lambda v
    print $ show_combinator c'
    print $ show_lambda v'

main :: IO ()
main = do
    {-
    let Right t = untyped_lambda_term_parse "<>" $
                    "(\\A.\\B.\\C.A (B C)) \\A.\\B.\\C.A (B C)"
                    {-
                    "(\\A.\\B.\\C.A (B C)) \\A.\\B.\\C.A (B C)"
                    "\\B.\\C.(\\A.\\B.\\C.A (B C)) (B C)"
                    "\\B.\\C.(\\A.\\B0.\\C0.A (B0 C0)) (B C)"
                    "\\B.\\C.\\B0.\\C0.(B C) (B0 C0)"
                     -}
    left_most_eval_lambda_termIO t
    return ()
    -}

    let Right t = untyped_lambda_term_parse "<>"
         "\\x2x. (\\rec_x. x2x (rec_x rec_x)) (\\rec_x. x2x (rec_x rec_x))"
        Right c = lambda2combinator t
    print "fix"
    print $ show_combinator c
    print $ show_combinator $ eval_combinator c
    print "I"
    _parse_and_print str_I
    print "B"
    _parse_and_print str_B
    print "C"
    _parse_and_print str_C
    print "K"
    _parse_and_print str_K
    print "S"
    _parse_and_print str_S
    print "app"
    _parse_and_print str_app
    _parse_and_print "\\x.\\y. y x" -- C I
    -- (S (K (S I)) (S (K K) I))
    let _CI_1 = (_S2 (_K1 (_S1 _I0)) (_S2 (_K1 _K0) _I0))
    print $ show_combinator _CI_1
    print $ show_combinator $ eval_combinator _CI_1
    -- (S (K (S I)) K)
    --}

{-
"fix"
"S (C (B B I) (S I I)) (C (B B I) (S I I))"
"S (C B (S I I)) (C B (S I I))"
"I"
"I"
"\\x.x"
"B"
"C (B B B) (C B I)"
    B f g x = f (g x)
    C B I x = B x I = x ==>> C B I = I
    "C (B B B) (C B I) f g x" =
    "   B B B  f (C B I) g x" =
    "     B(B  f)(C B I) g x" =
    "       B  f (C B I  g)x" =
    "       B  f (  B g  I)x" =
    "       B  f (    g   )x" =
"\\f.\\g.\\x.f (g x)"
"C"
"C (B B (B C (C B I))) I"
"\\f.\\x.\\y.f y x"
"K"
"K"
"\\x.\\y.x"
"S"
"C (B B (B S (C B I))) (C B I)"
"\\f.\\g.\\x.f x (g x)"


-}

--}
--}
--}
--}
--}
