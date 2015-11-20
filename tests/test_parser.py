import pytest
from fenicsbot.parser import excise, parser

@pytest.mark.parametrize(("s", "s_excised"), [
    ("@fenicsbot Solve text", "text"),
    ("a @fenicsbot Solve b", "a b"),
])
def test_excise(s, s_excised):
    assert s_excised == excise(s)


@pytest.mark.parametrize("tweet", [
    "@fenicsbot Solve Poisson with f=1",
    "@fenicSbot Solve Poisson",
    "@FEniCSbot Solve Poisson with f=1 and D=2",
    "@feNicsBot Solve Stokes",
])
def test_parsing_of_good_tweets(tweet):
    # Checks that these tweets are parsed and result in some output
    parser(tweet)


@pytest.mark.parametrize("tweet", [
    "@fenisbot Solve Poisson with f=1",
    "Solve Poisson",
    "@fenicsbot Poisson with g=1 and D=2",
    "@fenicsbot Solve with f=1 and n=2",
    "@fenicsbot Solve",
    "@fenicsbot ",
    "@FEnCSbot Solve Poisson with f=1 and D=2",
])

def test_parsing_of_bad_tweets(tweet):
    # Checks that tweets which are not written properly raise exceptions
    with pytest.raises(Exception) as e_info:
        parser(tweet)



    
# if __name__=="__main__":
#     tweet = "@FEniCSbot Poisson2D"
#     # tweet = "@FEniCSbot Poisson with  D=1 and f=1"
#     # img_fn = parser(tweet)
#     # print img_fn
    
#     tweets = [
#         "@fenicsbot Solve Poisson with f=1",
#         "@fenicsbot Solve Poisson",
#         "@fenicsbot Solve Poisson with f=1 and D=2",
#         "@fenicsbot Solve Stokes"
#     ]


    # for t in tweets:
    #     parser(t)
    
    # for s, s_e in [
    #         ("@fenicsbot Solve text", "text"),
    #         ("text @fenicsbot Solve text", "text text")]:
    #     # print s_e
    #     # print s
    #     # print excise(s)
    #     assert s_e == excise(s)