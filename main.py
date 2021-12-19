if __name__ == '__main__':
    from sys import path
    from os import getcwd
    from os.path import join
    from const import PARSER_PATH
    from const import RES_SRC_PATH
    from const import RES_OUT_PATH

    path.append(join(getcwd(), PARSER_PATH))

    from test_parser.invocation import main

    res_src, res_out = join(getcwd(), RES_SRC_PATH), join(getcwd(), RES_OUT_PATH)
    print('\n' + res_src + '\n')
    print('\n' + res_out + '\n')
    main(res_src, res_out)
