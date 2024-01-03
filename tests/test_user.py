import pytest


class MyTester:
    def __init__(self, arg=["var0", "var1"]):
        self.arg = arg
        # self.use_arg_to_init_logging_part()

    def dothis(self):
        print("this")

    def dothat(self):
        print("that")


@pytest.fixture
def tester(request):
    """Create tester object"""
    return MyTester(request.param)


class TestIt:
    @pytest.mark.parametrize("tester", [["var1", "var2"]], indirect=True)
    def test_tc1(self, tester):
        tester.dothis()
        assert 1


class TimeLine:
    def __init__(self, instances):
        self.instances = instances


@pytest.fixture
def timeline(request):
    return TimeLine(request.param)


@pytest.mark.parametrize("timeline", ([1, 2, 3], [2, 4, 6], [6, 8, 10]), indirect=True)
def test_timeline(timeline):
    for instance in timeline.instances:
        assert instance % 2 == 0


if __name__ == "__main__":
    pytest.main([__file__])


# https://stackoverflow.com/questions/42228895/how-to-parametrize-a-pytest-fixture
