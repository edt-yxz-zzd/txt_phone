{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE MultiParamTypeClasses #-}
-- type eq
type family F :: * -> *
type family G :: * -> *
class (F a ~ G b) => C a b where
    f :: a -> b -> F a

