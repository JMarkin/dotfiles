import json


def word(f: str, g: int):
    pass


def rst_test(a):
    """This should be shown in rst formatting

    Args:
        a: The parameter

    Example:
        This is how you can use this function:

        .. code-block:: python

            result = test(3)
            print(result)
            nestedcss = "color: red"

        The injections are nested by nvim-treesitter
    """
    testcss = "background-color: pink"
    testhtml = "<p>very great html</p>"
    testjs = "const x=5"
    json.loads('{"s": 1}')

    s_json = '{"s": 1}'
    json.loads(s_json)

    text("select * from table")
    s.execute("select * from table")
    sa.text("select * from table")
    return [testcss, testhtml, testjs]


assert rs
