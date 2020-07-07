
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE ExplicitForAll #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE AllowAmbiguousTypes #-}


{-
    TypeApplications
    func @type
-}




newtype Label label a = Label a
    deriving (Show, Read)
unLabel :: forall label a. Label label a -> a
unLabel (Label a) = a

class C a where
    type Data a :: *
    the_data :: Label a (Data a)


get_the_data :: forall a. C a => Data a
    {-
        requires AllowAmbiguousTypes
            since (Data a) ==xx==>> a
    -}
get_the_data = unLabel (the_data :: forall. Label a (Data a))
    {-
        requires ExplicitForAll&ScopedTypeVariables
            ==>> this inner 'a' is the outer 'a' above
    -}

data A
instance C A where
    type Data A = String
    the_data = Label "the_data of A"
main = do
    print $ get_the_data @A
    {-
        requires TypeApplications
            ==>> allow "get_the_data @A"
    -}

