from typing import AnyStr

from .impl.parser_impl import ParserImpl


def main(res_src_dir: AnyStr, res_out_dir: AnyStr):
    parser = ParserImpl(res_src_dir, res_out_dir)
    parser.parse_tests()
